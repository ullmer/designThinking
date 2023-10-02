// Virtual Physics code, Visualizations subclasses header file
// Split from vis.h, 07/05/93
// This file intended for SGI Inventor implementation

#ifndef __VPVISOBJ__
#define __VPVISOBJ__

#include "vis.h"
#include "vp.h"

#include "objects.h"
#include "sound.h"
#include "image.h"
#include "doc.h"

#include <Inventor/nodes/SoCoordinate3.h>
#include <Inventor/actions/SoGetMatrixAction.h>

#include <Inventor/nodes/SoFont.h>
#include <Inventor/nodes/SoText2.h>
#include <Inventor/nodes/SoText3.h>
#include <Inventor/nodes/SoScale.h>

/////////////////////////// Cubes //////////////////////////

class VpvCoCube : public VpvBase //Colored cube (cube with SoMaterial)
{ protected:
    SoCube *cube;
    SoMaterial *material;
    SoSelection *selection;

  public:
    VpvCoCube(SoSelection *selection);
    VpvCoCube(VpObject *newObj, SoSelection *selection);
    VpvCoCube(VpObject *newObj, float r, float g, float b);
     //With this one, I'm sort of ignoring the old selection basis
     // for VpvCoCube's existence... c'est le vie! ;-)

    void setColor(float r, float g, float b);
    inline void setSelection(SoSelection *selection);
    virtual void bindObj(VpObject *newObj);

    void bright();
    void dim();
};

class VpvTCube : public VpvCube, public VpdText
{ public:
    VpvTCube(VpObject *object, char *text) :
      VpvCube(object), VpdText(text) {}

    virtual void selected();
};

class VpvSCube : public VpvCube, public VpsBase
{ public:
    VpvSCube(VpObject *object, char *soundFilename) : VpvCube(object),
      VpsBase(soundFilename)
        {}

    virtual void selected();
};

class VpvICube : public VpvCube, public VpiTexture
{ public:
    VpvICube(VpObject *object, char *filename);

  //virtual void selected();
};

class VpvTSCube : public VpvCube, public VpsBase, public VpdText
{ public:
    VpvTSCube(VpObject *object, char *soundfile, char *textfile) :
      VpvCube(object), VpsBase(soundfile), VpdText(textfile)
        {}

    virtual void selected();
};

/////////////////// Text ///////////////////

//// VpvText ////

class VpvText : public VpvBase
{ protected:
    SoFont *font;
    SoText3 *text;
    void FixText(); //Puts the text from the VpoText into SoText3 form
    void init(VpoText *obj, int frontOnly=1);

  public:
    VpvText() {}
    VpvText(VpoText *obj, int frontOnly=1);
    virtual void bindObj(VpoText *newObj);
};

class VpvCoText : public VpvText
{ public:
    VpvCoText(VpoText *obj);
    VpvCoText(VpoText *obj, float r, float g, float b);

    virtual void bindObj(VpoText *newObj);

    void setColor(float r, float g, float b);

  protected:
    SoMaterial *material;

};

class VpvText2 : public VpvBase
{ protected:
    SoFont *font;
    SoText2 *text;
    SoMaterial *material;
    void FixText();
    void init(VpoText *obj, float r, float g, float b);
    
  public:
    VpvText2() {font=NULL; text=NULL; material=NULL;}
    VpvText2(VpoText *obj, float r=1, float g=1, float b=1);
    virtual void bindObj(VpoText *newObj);

    void setColor(float r, float g, float b);
    void setSize(float n);

};

///class PosBlender
/// returns the average of the last N submitted vals as the current val

class PosBlender
{ public:
    PosBlender(int windowSize);

    void setSize(int windowSize);

    void  setVec(VpVec p);
    VpVec getVec();

  private:
    VpVecList *vecList;
    int WindowSize;

};

/////

class VpvImage : public VpvBase
{ public:
    VpvImage() {}

    VpvImage(VpObject *object, VpiPixmap *npixmap, SoCamera *camera, 
	     VpvSimpleEnv *env);
      //By passing VpiPixmap instead of filename, we can have multiple
      //rendered images per single datastore
      //Use Env link so that we can obtain window size in non-repetitive
      //manner

    void show(int x, int y, float scale);
    SoCallback* getCallback() {return CB;}

  protected:
    VpiPixmap *pixmap;
    SoCallback *CB;
    SoCamera *camera;
    VpvSimpleEnv *env;
    SbViewVolume ViewVol;
    static void callback(void *, SoAction *);
};

class VpvImageD : public VpvBase //Not a VpvImage descendant; 
  //dependent for display upon VpvImageBank, hence D(ependent)
{ 
  protected:
    VpiPixmap *pixmap;

  public:
    VpvImageD(VpObject *object, VpiPixmap *npixmap);

    VpiPixmap* getPixmap() 
      {return pixmap;}
};

MakeList(VpvImageD, ImageDList);

class VpvImageBank 
{ protected:
    ImageDList *imageList;

    SoCallback *CB;
    SoCamera *camera;
    SoSeparator *sep;

    VpvSimpleEnv *env;
    SbViewVolume ViewVol;

    void show(VpiPixmap *pixmap, int x, int y);
    static void callback(void *, SoAction *);
   

  public:
    VpvImageBank(SoCamera *camera, VpvSimpleEnv *env);
    void AddImage(VpvImageD *newImage); //PREPEND to imageList
    SoSeparator* getSep()
      {return sep;}

    ImageDList *getList()
      {return imageList;}

};

class VpvSpiral : public VpvBase //It does not follow (Vpv from Vpo); correct
  //as descendant from VpvBase
{ public:
    VpoSpiral(VpVec loc, int number = 12, float dist = 0.2);

    void setNum(int num) {number = num;}
    int  getNum() {return number; }

    void  setDist(float num) {dist = num;}
    float getDist() {return dist;}
    
  protected:
    int number;
    float dist;
    float **points, *knots;

    SoNode* constructSpiral(int number, float dist);
    void genPoints(int number, float dist);
};

class VpvsSquare //Subclass - not a VpvBase descendant
{ public:
    VpvsSquare(VpVec loc, SoScale *scale, float r=1, float g=1, float b=1);
    void setColor(float r, float g, float b);
    virtual void bindLoc(VpVec loc);

    VpVec getLoc()
      {return loc;}
    void setLoc(VpVec a)
      {loc = a; transl->translation.setValue(loc);}

    SoSeparator *getShell()
      {return ObjSep;}

  protected:
    SoSeparator *ObjSep;
    VpVec loc;
    SoMaterial *material;
    SoScale *scale;
    SoTranslation *transl;

    void makeSquare();
};

class VpvSquareArray : public VpvBase
{ public:
   VpvSquareArray(VpObject *obj, int numSubDivs, float distance, 
		  float scale=1);

   virtual void bindObj(VpObject *obj);

  protected:
   int numDivs;
   float distance;
   VpvsSquare **squares;
   SoScale *scale;
};

class VpvPresenceIndicator : public VpvSquareArray
{ public:
    VpvPresenceIndicator(VpObject *obj, int numSubDivs, float distance,
		  float scale, VpVec orientation);

    void activateProcessing(VpObjects *objects, float timeBetweenUpdates);
    void setColorBounds(float a[3], float b[3], int maxCount);

  protected:
    VpObjects *objects;
    VpTime *scheduler;
    VpVec orientation; //Not yet supported graphically, but used for this
                       //implementation
    VpgPlane *planar; //Use this for distance segmentation; a real
                      //advantage when you have arbitrarily-oriented jobbers

    int *headCount;

    VpVec colorA, colorB, incremental; //Unusual use of Vec, but... it works!
    int headMax;

    static void update(void *data, VpSchedulerBase *);

};

class VpvPulsingShape : public VpvShaped
{ protected:
    float pulseFrequency;
    float callbackFrequency;
    VpTime *scheduler;

    float baseColor[3], selectedColor[3];
    float cycleState, cycleInc;

    SoMaterial *material;

    static void callback(void *data, SoSensor *);
    
    int selectCount;

  public:
    VpvPulsingShape() : VpvShaped() { scheduler = NULL; }
    VpvPulsingShape(VpObject *newObj, SoNode *newShape, 
		    float pulseFreq = 1., float callbackFreq = 10.);

    ~VpvPulsingShape() { if (scheduler != NULL) delete scheduler; }

    virtual void bindObj(VpObject *newObj);
    virtual void selected();
};

#endif

