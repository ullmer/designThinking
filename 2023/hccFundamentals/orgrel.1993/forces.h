// Virtual Physics library
// Forces headers
// Code by Brygg Ullmer, begun 05/16/1993

#ifndef __VP_FORCES__
#define __VP_FORCES__

#include "vp.h"

class VpfGravity : public VpForce //Can be positive or negative
{ private:
    float Gconst;
    float gravPow;
  public:
    VpfGravity();
    virtual VpVec Apply(VpObject *host, VpObject *applied);

    void setConst(float num)
      {Gconst = num; }
    float getConst()
      {return Gconst; }

    virtual void setPower(float num) 
      {gravPow = num; }
    virtual float getPower() 
      {return gravPow;}
};

class VpfBand : public VpForce //Can be positive or negative
{ private:
    float Bconst;
    float Bpower;
  public:
    VpfBand();
    virtual VpVec Apply(VpObject *host, VpObject *applied);

    void setConst(float num)
      {Bconst = num; }
    float getConst()
      { return Bconst; }

    void setPower(float num)
      {Bpower = num;}
    float getPower()
      {return Bpower;}
};


class VpfSpring : public VpForce
{};

class VpfString : public VpForce
{};

class VpfRod : public VpForce
{};

#endif
