#include "geom.h"

//// VpgPoint ////

VpVec VpgPoint::direction(VpVec p)
{ VpVec ret = p - loc;
  ret.normalize(); return ret;
}

float VpgPoint::dist(VpVec p)
{ float ret=0;

  for(int i=0; i<3; i++)
    ret += pow(loc[i] - p[i], 2);

  return sqrt(ret);
}

//// VpgLine ////

VpVec VpgLine::closestP(VpVec p)
{ VpVec q = orientation;
  float r = q.dot(p - loc);
  VpVec s = orientation;

  q = orientation * r / s.dot(orientation);

  return q + loc;
}

VpVec VpgLine::direction(VpVec p)
{ VpVec ret = p - closestP(p);
  ret.normalize(); return ret;
}

float VpgLine::dist(VpVec p)
{ VpVec r = closestP(p);
  float ret = 0;
  
  for(int i=0; i<3; i++)
    ret += pow(r[i] - p[i], 2);

  return sqrt(ret);
}

//// VpgPlane ////

float VpgPlane::dist(VpVec p)
{ VpVec ret = VpgLine::closestP(p) - loc;
  return ret.length();
}

int VpgPlane::whichSide(VpVec p)
{ float num = dist(p);

  if (num > 0) return 1;
  if (num == 0) return 0;
  return -1;
}

VpVec VpgPlane::direction(VpVec p)
{ orientation.normalize();

  int direction = whichSide(p);

  if (direction < 0) return -orientation;
  return orientation; //Should consider returning 0 if whichSide() rets 0

}

VpVec VpgPlane::closestP(VpVec p)
{ VpVec a = VpgLine::closestP(p) - loc;

  return p - a;
}
  
  
