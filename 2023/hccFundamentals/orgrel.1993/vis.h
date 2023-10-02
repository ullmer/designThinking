// Virtual Physics code, Visualizations header file
// Code by Brygg Ullmer, begun 06/01/1993
// This file intended for SGI Inventor implementation

#ifndef __VIRT_VIS__
#define __VIRT_VIS__

#include "vp.h"

#ifdef INVENTOR
//If we don't have it, we're not going very far!

#include <Inventor/nodes/SoSeparator.h>
#include <Inventor/nodes/SoMaterial.h>
#include <Inventor/nodes/SoCube.h>
#include <Inventor/nodes/SoNode.h>
#include <Inventor/nodes/SoCylinder.h>
#include <Inventor/nodes/SoTransform.h>
#include <Inventor/nodes/SoTranslation.h>
#include <Inventor/nodes/SoRotation.h>
#include <Inventor/nodes/SoMatrixTransform.h>
#include <Inventor/nodes/SoPerspectiveCamera.h>
#include <Inventor/nodes/SoOrthographicCamera.h>
#include <Inventor/nodes/SoDirectionalLight.h>
#include <Inventor/nodes/SoComplexity.h>
#include <Inventor/nodes/SoCallback.h>
#include <Inventor/nodes/SoLineSet.h>
#include <Inventor/nodes/SoIndexedLineSet.h>
#include <Inventor/SoDB.h>
#include <Inventor/SoSensor.h>
#include <Inventor/SbLinear.h>
#include <Inventor/SoSensor.h>
#include <Inventor/SoBoxHighlight.h>
#include <Inventor/SoSelection.h>
#include <Inventor/SoXtRenderArea.h>
#include <math.h>

//// VpBaseObj ////
/// Base for Inventor visualization of Vp objects

// Just use nodes.  Also, have object bound in, rather than direct
// dependency; allows grouped and descendant objects to be uniformly 
// represented.

// Put off binding of particular shape at this point.  Use particular
// shapes for descendant classes...

class VpvBase
{ protected:

    VpObject *obj; //The object which is being represented
    SoSeparator *ObjSep;
    SoTranslation *transl;
    char *name;

  public:

    VpvBase();
    VpvBase(VpObject *newObj);
    ~VpvBase();

    virtual void bindObj(VpObject *newObj);
    VpObject* getObj();
    SoSeparator* getShell();
    virtual void update();
    
    void setName(char *nname) 
      {name=nname;}
    char* getName() 
      {return name;}

    virtual void selected() 
      { if (name != NULL) printf("<%s> selected\n", name); }
};

class VpvCube : public VpvBase
{ protected:
    SoCube *cube;
 
  public:
    VpvCube();
    VpvCube(VpObject *newObj);
    virtual void bindObj(VpObject *newObj);
};

class VpvLink : public VpvBase //doesn't follow from base so well, but...
{ VpObject *obj2;
  SoCylinder *cylinder;
  SoRotation *rotation;
  SbRotation *rot;
  SoComplexity *complex;
  SbVec3f NullVec;

 public:
   VpvLink(VpObject *a, VpObject *b);
   virtual void bindObj(VpObject *a, VpObject *b);
   virtual void update();

};

class VpvPropertiesBase : public VpvBase
{ 
};

MakeList(VpvBase, VpvBases);


//// VpvShapedVis  ////
/// Object shape is passed in explicitly

class VpvShaped : public VpvBase
{ protected:
    SoNode *node;

  public:
    VpvShaped();
    VpvShaped(VpObject *newObj, SoNode *newShape);
    virtual void bindObj(VpObject *newObj);
    SoNode *getLObj() //return local object
      { return node; }

    virtual void readShape(char *filename);

};


/// ****NOTE****
/// SimpleVisEnv must be physically declared (or at least allocated)
/// earlier than other vis-related variables, as it init's the 
/// Inventor SoDB databases

class VpvSimpleEnv: public VpEnvironment
{ protected:
     SoSeparator *VisEnvironment;
     VpvBases *Bases;
     Widget appWindow;
     SoCamera *camera;

     void EnvCallback(void *, VpSchedulerBase *);
     virtual void InventorVis(int cameraModel);

     SbVec2s windowSize;

     int Generation; //0 for first window, 1 for subsequent windows
     SoXtRenderArea *renderArea;

  public:
     VpvSimpleEnv(int Generation = 0);

     virtual void AssertObject(VpObject *Object);
     virtual void AssertLink(VpObject *A, VpObject *B);
     virtual void RetractVObject(VpvBase *Object);

     Widget* getWindow()
       { return &appWindow; }

     virtual SoCamera* getCamera()
       { return camera;}

     SoSeparator* getShell()
       { return VisEnvironment; }
     VpvBases* getBases()
       { return Bases; }

     void calcWindowSize()
       {windowSize = SoXt::getWidgetSize(appWindow);}

     SbVec2s getWindowSize()
       {return windowSize;}

     virtual void systemInit();
     virtual void StartVis(int cameraModel=0);
     virtual void StartSim(int startMainloop=1);
};

#endif //Inventor code
#endif //Vis header





