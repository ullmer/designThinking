#ifndef __VPGEOM__
#define __VPGEOM__

#include <stdio.h>
#include <math.h>
#include "list.h"

#ifdef INVENTOR

#include <Inventor/SbLinear.h> 

#define VpVec SbVec3f
MakeList(VpVec, VpVecList);

//Perhaps change above to arbitrary-length vector... except that doesn't
//work so well with Inventor and the SGI-specific hardware

#define VpMat4 SbMatrix

#endif

class VpgPoint //Vpg = Virtual Physics Geometry
{ public:
    VpgPoint() {}
    VpgPoint(VpVec loc)
      { setLoc(loc); }
    ~VpgPoint() {}

    virtual VpVec direction(VpVec p);
    virtual float dist(VpVec p);

    virtual VpVec getLoc() 
      {return loc; }
    virtual void setLoc(VpVec p)
      {loc = p;}

  protected:
    VpVec loc;
};

class VpgLine : public VpgPoint
{ public:
    VpgLine() {}
    VpgLine(VpVec nloc, VpVec ndir) : VpgPoint(nloc)
      {setDir(ndir);}

    virtual VpVec direction(VpVec p);
    virtual float dist(VpVec p);
    virtual VpVec closestP(VpVec p); //Closest Point

    void setDir(VpVec p) //Direction
      { orientation = p; }
    VpVec getDir()
      { return orientation; }

  protected:
    VpVec orientation;
};

class VpgPlane : public VpgLine
{ public:
    VpgPlane() : VpgLine() {}
    VpgPlane(VpVec loc, VpVec dir) : VpgLine(loc, dir) {}

    virtual VpVec direction(VpVec p);
    virtual float dist(VpVec p);

    int whichSide(VpVec p); // 1 if above (in direction of vect), -1 if below
    virtual VpVec closestP(VpVec p); //direction and dist come directly 
      //from this
  
};


#endif
