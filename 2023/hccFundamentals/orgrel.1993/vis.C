// Virtual Physics code, Visualizations codeheader file
// Code by Brygg Ullmer, begun 06/01/1993
// This file intended for SGI Inventor implementation

// Vpv stands for Virtual Physics Visualization

#include "vis.h"

#define RENDERCONTROL 
//RENDERCONTROL supports forced renders (perhaps will reduce number of
// redundant renders, if such were being conducted)

//// VpvBase ////

VpvBase::VpvBase()
{ obj=NULL; 
  ObjSep = new SoSeparator;
  transl = new SoTranslation;
  name = "Unnamed object";
}

VpvBase::VpvBase(VpObject *newObj)
{ ObjSep = new SoSeparator;
  transl = new SoTranslation;
  
  bindObj(newObj);
}

VpvBase::~VpvBase()
{ ObjSep->unref();
}

void VpvBase::bindObj(VpObject *newObj)
{
  obj = newObj;
  transl->translation.setValue(obj->GetLoc());
  ObjSep->addChild(transl);
  //Continue with addition of shape and referencing of separator from
  //less general descendant
}
  
void VpvBase::update()
{ if (obj!=NULL)
    transl->translation.setValue(obj->GetLoc());
}

VpObject* VpvBase::getObj()
{ return obj; }

SoSeparator* VpvBase::getShell()
{ if (ObjSep == NULL)
    printf("Bad, BAD!  ObjSep == NULL!\n");
  return ObjSep; 
}

//// VpvCube ////

VpvCube::VpvCube()
{ cube = new SoCube;
  name = "Unnamed cube";
}

VpvCube::VpvCube(VpObject *obj)
{ cube = new SoCube;
//  cube->depth.setValue(0.1);
//  cube->width.setValue(0.1);
//  cube->height.setValue(0.1);
  bindObj(obj);
}

void VpvCube::bindObj(VpObject *newObj)
{ obj = newObj;
  transl->translation.setValue(obj->GetLoc());
  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(cube);
}


//// VpvLink //// Links two objects together

VpvLink::VpvLink(VpObject *a, VpObject *b)
{ cylinder = new SoCylinder;
  rotation = new SoRotation;
  rot = new SbRotation;
  complex = new SoComplexity;
  obj2 = NULL;
  name = "Unnamed link";
  NullVec.setValue(0,1,0);
  complex->value.setValue(0.1);

  cylinder->radius.setValue(0.075);

  bindObj(a, b);
}

void VpvLink::bindObj(VpObject *a, VpObject *b)
{ obj = a; obj2 = b;

  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(rotation);
  ObjSep->addChild(complex);
  ObjSep->addChild(cylinder);

  update();
}

void VpvLink::update()
{ if (obj != NULL && obj2 != NULL)
    { VpVec tmp = obj->GetLoc() - (obj->GetLoc() - obj2->GetLoc())/2;

      transl->translation.setValue(tmp);
      rot->setValue(NullVec, obj->direction(obj2->getLoc()));
      rotation->rotation = *rot;
      cylinder->height.setValue(obj->dist(obj2->getLoc()));
    }
} 

//// VpvShapedVis ////

VpvShaped::VpvShaped()
{ node=NULL; }

VpvShaped::VpvShaped(VpObject *obj, SoNode *newShape)
{ node = newShape; 
  bindObj(obj);
}

void VpvShaped::bindObj(VpObject *nobj)
{ obj = nobj;
  transl->translation.setValue(obj->GetLoc());

  ObjSep->ref();
  ObjSep->addChild(transl);
  ObjSep->addChild(node);
}

void VpvShaped::readShape(char *filename)
{ SoInput datafile;
  SoNode *nnode; 
// don't *THINK* this should be instantiated... (SoNode can't be, in any case)

  datafile.openFile(filename);
  SoDB::read(&datafile, nnode);

  node = nnode;
}

//// VpvSimpleEnv ////

VpvSimpleEnv::VpvSimpleEnv(int generationNum)
{ Generation = generationNum;

  if (Generation == 0) systemInit();

  VisEnvironment = new SoSeparator; 
  Bases = new VpvBases;
}

void VpvSimpleEnv::AssertObject(VpObject *Object)
{ VpvCube *SimpleObject;

  SimpleObject = new VpvCube(Object);
  Bases->append(SimpleObject);
  VpEnvironment::AssertObject(Object);
  VisEnvironment->addChild(SimpleObject->getShell());
}

void VpvSimpleEnv::AssertLink(VpObject *a, VpObject *b)
{ VpvLink *Link;

  Link = new VpvLink(a,b);
  Bases->append(Link);
  VisEnvironment->addChild(Link->getShell());
}


void VpvSimpleEnv::RetractVObject(VpvBase *Object)
{ Bases->del(Object);
  VisEnvironment->removeChild(Object->getShell());
//  delete Object;
}


void VpvSimpleEnv::StartSim(int startMainloop)
{ SystemTime.AssertCallback((void (*)(void *, 
		     VpSchedulerBase *))EnvCallback, this);

  SystemTime.StartTime();
  if (startMainloop) SoXt::mainLoop();
}

void VpvSimpleEnv::StartVis(int cameraModel)
{ 

#ifdef RENDERCONTROL
  renderArea = new SoXtRenderArea;
  renderArea->setSceneGraph(VisEnvironment);
  renderArea->setAutoRedraw(FALSE);
#endif

  InventorVis(cameraModel);
}

void VpvSimpleEnv::EnvCallback(void *data, VpSchedulerBase *)
{ VpvSimpleEnv *ptr =  (VpvSimpleEnv *) data;

  //update window size
  calcWindowSize();

  //Calculate accelerations for objects
  if (ForceList->length() > 0)
    { ForceList->resetMarker();
      VpForce *fptr = ForceList->first();
      while (fptr != NULL)
	{ fptr->Calc();
	  fptr = ForceList->next();
	}
    }

  //Derive current positions for objects
  if (ObjectList->length() > 0)
    { ObjectList->resetMarker();
      VpObject *optr = ObjectList->first();
      while (optr != NULL)
	{ optr->DeriveParams();

#ifdef DEBUG
	  float x,y,z;
	  (optr->GetLoc()).getValue(x,y,z);
	  /*printf("Location: %f, %f, %f\n", x,y,z);*/
#endif 

	  optr->ZeroAccel();
	  optr = ObjectList->next();
	}
    }

  //Update current visual positions of objects
  if (Bases->length() > 0)
    { Bases->resetMarker();
      VpvBase *vptr = Bases->first();
      while (vptr != NULL)
	{ vptr->update();
	  vptr = Bases->next();
	}
    }
#ifdef RENDERCONTROL
  renderArea->render();
#endif 

}


void VpvSimpleEnv::systemInit()
{  printf("Inventor initiation\n");
   char *name="Graphics Program";
   
   appWindow = SoXt::init(name);  // Init Inventor
   if ( appWindow == NULL ) exit( 1 );      // and Xt


}

void VpvSimpleEnv::InventorVis(int cameraModel)
{
   SoSeparator *root = new SoSeparator;
   root->ref();

   switch (cameraModel)
     {case 0: camera = new SoPerspectiveCamera; break;
      case 1: camera = new SoOrthographicCamera; break;
     }

   root->addChild( camera );
   root->addChild( new SoDirectionalLight );

   root->addChild(VisEnvironment);

//   SoCone *cone = new SoCone; // Test object
//   cone->height.setValue(0.05);
//   root->addChild(cone);

//   camera->viewAll(root);
   camera->position.setValue(0,0,0);

   camera->nearDistance.setValue(0.03);
   camera->farDistance.setValue(500);
   
   SoXtRenderArea *renderArea = new SoXtRenderArea;
   renderArea->setSize(SbVec2s(750, 750));

   if (Generation == 0) (void) renderArea->build( appWindow );
   else appWindow = renderArea->build();

   renderArea->setSceneGraph( root );
   renderArea->show();

   SoXt::show( appWindow );
 }

