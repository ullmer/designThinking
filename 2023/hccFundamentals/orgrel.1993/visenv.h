// Virtual Physics Visualization Environments
// Split off from vis.h on 07/05/93

#ifndef __VPVISENV__
#define __VPVISENV__

#include "vis.h"
#include "visobj.h"
#include "objects.h"
#include "sound.h"
#include "image.h"
#include "doc.h"

class VpvExtendedEnv : public VpvSimpleEnv
{ public:
     VpvExtendedEnv(int generation = 0) : VpvSimpleEnv(generation) {}

     virtual void AssertObject(VpoText *Object); //Use AssertTextObject
     virtual void AssertObject(VpObject *Object) 
       { VpvSimpleEnv::AssertObject(Object); }
     virtual void AssertObject(VpObject *Object, float r, float g, float b);
 
     virtual void AssertTextObject(VpoText *Object, float r, float g, float b,
				   int dimension=1);
       //dim=1 does 3D text, dim=0 does 2D
     virtual void AssertSoundObject(VpObject *Object, char *filename);
     virtual void AssertImageObject(VpObject *Object, char *filename);
     virtual void AssertImageObject(VpObject *Object, VpiPixmap *pix);
     virtual void AssertVpvObject(VpvBase *obj);

//     virtual void AssertObject(VpvNewsBit *obj);

};

class VpvImageEnv : public VpvExtendedEnv
//Basically, a VpvExtendedEnv plus an ImageBank.  Could have been added
//directly into VpvExtendedEnv (and will need integration into VpveEvent
//descendant, I'm sure), but... we add it here for the present.
{  
  protected:
     VpvImageBank *imageBank;

  public:
     VpvImageEnv(int generation = 0) : VpvExtendedEnv(generation) 
       {imageBank = new VpvImageBank(camera, this);
        VisEnvironment->addChild(imageBank->getSep()); }
     
     virtual void AssertImageObject(VpObject *Object, VpiPixmap *pix);
     ImageDList* getImageList()
       {return imageBank->getList(); }
 
};

class VpveEvent : public VpvExtendedEnv
   //Vpve == Virtual physics visual environment
{public:
   SoSelection* getSelection()
     { return selection; }

 protected:
    int highlightSelection;
    SoSelection *selection;
    virtual void InventorVis(int cameraModel); //This function must match
      //ancestral prototypes, for in absence this as a virtual func won't
      //be executed.

    void SelectionCallback(void *data, SoPath *selectionPath);
    VpvBase* findObject(SoNode *node);

 public:
   VpveEvent(int Generation = 0, int hlSelect = 1) : VpvExtendedEnv(Generation)
     {highlightSelection = hlSelect;}

};

#endif
