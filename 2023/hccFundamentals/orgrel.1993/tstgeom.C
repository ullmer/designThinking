#include "geom.h"


main()
{
  VpVec a(1,1,0), b(0,0,0), d(1,0,0);

  VpgPlane pt(d,d);

  float num = pt.dist(a);

  VpVec r(0,0,0), s(0,0.1,1);

  VpgLine line(r,s);

  VpVec t = line.direction(a);
  t.print();

  printf("%f %f\n", num, line.dist(a));
}
