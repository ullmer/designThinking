#include "visenv.h"

/*
void VpvExtendedEnv::AssertObject(VpvNewsBit *obj)
{ Bases->append(obj);
  VpEnvironment::AssertObject(obj->getObj());
  VisEnvironment->addChild(obj->getShell());
}
*/

void VpvExtendedEnv::AssertObject(VpoText *Object)
{ VpvText *TextObject;

  TextObject = new VpvText(Object);
  Bases->append(TextObject);
  VpEnvironment::AssertObject(Object);
  VisEnvironment->addChild(TextObject->getShell());
}

void VpvExtendedEnv::AssertObject(VpObject *Object, float r, float g, float b)
{ VpvCoCube *SimpleObject;

  SimpleObject = new VpvCoCube(Object, r,g,b);
  Bases->append(SimpleObject);
  VpEnvironment::AssertObject(Object);
  VisEnvironment->addChild(SimpleObject->getShell());
}

void VpvExtendedEnv::AssertTextObject(VpoText *Object,
                                               float r, float g, float b, int dim)
{ VpvBase *TextObject;

  if (dim)
    TextObject = new VpvCoText(Object, r,g,b);
  else
    TextObject = new VpvText2(Object, r,g,b);

  Bases->append(TextObject);
  VpEnvironment::AssertObject(Object);
  VisEnvironment->addChild(TextObject->getShell());
}

void VpvExtendedEnv::AssertImageObject(VpObject *Object,
                                                char *filename)
{ VpiPixmap *pix = new VpiPixmap(filename);
  AssertImageObject(Object, pix);
}

void VpvExtendedEnv::AssertImageObject(VpObject *Object, VpiPixmap *pix)
{ 
  VpvImage *obj = new VpvImage(Object, pix, getCamera(), this);
  Bases->append(obj);
  VpEnvironment::AssertObject(Object);
  VisEnvironment->addChild(obj->getShell());
}

/// Only VpvImageEnv declaration follows, with ExtendedEnv 
// continuing thereafter

void VpvImageEnv::AssertImageObject(VpObject *Object, VpiPixmap *pix)
{ 
  VpvImageD *obj = new VpvImageD(Object, pix);
  imageBank->AddImage(obj);
  VpEnvironment::AssertObject(Object);
}

void VpvExtendedEnv::AssertSoundObject(VpObject *Object,
                                                char *filename)
{ VpvSCube *obj;

  obj = new VpvSCube(Object, filename);
  Bases->append(obj);
  VpEnvironment::AssertObject(Object);
  VisEnvironment->addChild(obj->getShell());
}

void VpvExtendedEnv::AssertVpvObject(VpvBase *obj)
{ Bases->append(obj);
  VisEnvironment->addChild(obj->getShell());
  VpEnvironment::AssertObject(obj->getObj());
}

//// VpveEvent  Visual Environment /////

void VpveEvent::InventorVis(int cameraModel)
{

   if (highlightSelection) selection = new SoSelection(new SoBoxHighlight);
   else selection = new SoSelection;

   selection->ref();
   selection->addObjectSelectedCallback((void (*)(void *, SoPath *)
                                         )SelectionCallback, this);
   selection->setSelectionPolicy(SoSelection::SINGLE);
   printf("Selection policy executed\n");
   
   SoSeparator *root = new SoSeparator;
   selection->addChild(root);

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
   (void) renderArea->build( appWindow );
   renderArea->setSceneGraph( selection );
   renderArea->show();

   SoXt::show( appWindow );
 }

void VpveEvent::SelectionCallback(void *, SoPath *selectionPath)
{ int length = selectionPath->getLength(), i=0;
  SoNode *retrieved;

  while
    (!(selectionPath->getNodeFromTail(i)->isOfType(
                        SoSeparator::getClassTypeId())) && i < length)
      i++;

  if (i == length) return;
  retrieved = selectionPath->getNodeFromTail(i);

  VpvBase *object = findObject(retrieved);
  if (object == NULL) return;

  object->selected();

}


VpvBase* VpveEvent::findObject(SoNode *node)
{
  if (Bases->length() < 1) return NULL;

  Bases->resetMarker();

  VpvBase *ptr = Bases->first();
  while (ptr != NULL && node != ptr->getShell())
    ptr = Bases->next();

  if (ptr == NULL) return NULL;
  else return ptr;
}


