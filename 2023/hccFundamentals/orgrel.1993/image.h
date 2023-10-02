#ifndef __VPIMAGE__
#define __VPIMAGE__

//Bring an image into the physical environment, probably
//through texture mapping or lrectwrite inputs

#ifdef INVENTOR

#include <Inventor/nodes/SoTexture2.h>

class VpiBase 
{ public:
    VpiBase();
    VpiBase(char *filename);

    void setFilename(char *nfilename)
      {filename = nfilename;}

    char* getFilename()
      {return filename;}

    virtual void bindImage() {}
  protected:
    char *filename;
};

class VpiTexture : public VpiBase
{ public:
    VpiTexture() : VpiBase() {}
    VpiTexture(char *filename) : VpiBase(filename) { texture=NULL; }

    virtual void bindImage();
    SoTexture2* getBoundImage();

  protected:
    SoTexture2 *texture;
};

class VpiPixmap : public VpiBase
{ public:
    VpiPixmap() : VpiBase() { image = NULL; }
    VpiPixmap(char *filename) : VpiBase(filename) { readFile(); }
    VpiPixmap(VpiPixmap *base, float scale=1.);

    virtual void bindImage();
    virtual void readFile();
    virtual unsigned long* getImageData() {return image;}

    int getDimX() {return dimX;}
    int getDimY() {return dimY;}

    virtual int scalingAvailable() {return 0;}

  protected:
    unsigned long *image; //SGI image format; 24 bit col + alpha
    int dimY, dimX;
    
};

class VpiPixmapMS : public VpiPixmap
{ public:
    VpiPixmapMS(char *filename, int numIncs = 4, float scaleIncs = 0.66);

    virtual unsigned long* getImageData(int num=0);

    virtual int scalingAvailable() {return 1;} //Should be gradation
    virtual void setLevel(int num=0);
    int getLevels() {return numIncs;}

  protected:
    int numIncs;
    float scaleIncs;
    VpiPixmap **pixmaps;
};

#endif
#endif
