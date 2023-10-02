// Virtual Physics library
// Forces coding
// Code by Brygg Ullmer, begun 05/16/1993

#include "vp.h"
#include "forces.h"

//// VpfGravity ////

VpfGravity::VpfGravity()
{ Gconst = 1e-2; setPower(2);}

VpVec VpfGravity::Apply(VpObject *host, VpObject *applied)
{ VpVec a =  host->direction(applied->getLoc()) * Gconst * 
                 (host->getProperties())->getProp(this) * 
		 (applied->getProperties())->getProp(this) /
		 pow(host->dist(applied->getLoc()),getPower());


#ifdef BDEBUG
  float x,y,z;
  a.getValue(x,y,z);

  printf("a = %f, b = %f, d = %f <%f %f %f>\n", 
	 (host->getProperties())->getProp(this),
	 (applied->getProperties())->getProp(this), 
	 host->dist(applied->getLoc()), x,y,z);
#endif BDEBUG

  return a;
}


//// VpfBand ////

VpfBand::VpfBand()
{ setConst(1e-4); }

VpVec VpfBand::Apply(VpObject *host, VpObject *applied)
{ VpVec a =  host->direction(applied->getLoc()) * Bconst * 
                 (host->getProperties())->getProp(this) * 
		 (applied->getProperties())->getProp(this) *
		 SQ(host->dist(applied->getLoc()));


#ifdef BDEBUG
  float x,y,z;
  a.getValue(x,y,z);

  printf("a = %f, b = %f, d = %f <%f %f %f>\n", 
	 (host.getProperties())->getProp(this),
	 (applied.getProperties())->getProp(this), 
	 host.dist(applied->getLoc()), x,y,z);
#endif BDEBUG

  return a;
}
