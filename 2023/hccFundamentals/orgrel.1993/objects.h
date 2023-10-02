//Derivatives of class Object

#ifndef __VP_OBJ__
#define __VP_OBJ__

#include "geom.h"
#include "vp.h"

class VpoPlanar : public VpObject, public VpgPlane
{ public: 
    VpoPlanar(VpVec loc, VpVec normal); 

//    int Above(VpVec P) 
//      { if (whichSide(P)==1) return 1; return 0; }

    virtual float dist(VpVec p) {return VpgPlane::dist(p);}

    virtual void setProperty(VpForce *force, float val, int affectedBy=1)
      { VpObject::setProperty(force, val, affectedBy); }

};

class VpoLine : public VpObject, public VpgLine
{ public:
    VpoLine(VpVec loc, VpVec orientation);

    virtual float dist(VpVec p) {return VpgLine::dist(p);}
    
    virtual void setProperty(VpForce *force, float val, int affectedBy=1)
      { VpObject::setProperty(force, val, affectedBy); }
};

/*
class VpoPlanarDirectional : public VpoPlanar
{ public:
    VpoPlanarDirection(VpVec loc, VpVec normal) : VpoPlanar(loc,normal) {}

    virtual VpVec direction(VpVec P);
};
*/

class VpoTubular : public VpObject, public VpgLine
{
};

class VpoText : public VpObject
{ protected:
    char *string;

  public:
    VpoText(char *string);
    VpoText(VpVec &loc, VpVec &vel, char *string);
    
    char* WrapText(int length=30);

    void  SetText(char *string);
    char* GetText();
};

#endif
