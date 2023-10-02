//Test of SimpleVisualEnvironment with sparsely populated first-trial sim.
//Brygg Ullmer; 06/04/1993

//Operational 06/15
// Bubbles cubes from background.

#include "vp.h"
#include "vis.h"
#include "visenv.h"
#include "visobj.h"
#include "forces.h"
#include "objects.h"
#include <stdlib.h>

VpveEvent Env;

VpfGravity gravity;

VpVec PrimaryDirection;

inline float frand() //Returns a float from 0 to 1
{ return (float) rand() / (float) RAND_MAX; }

static int objNum = 0;

static void
bubbler(void *, SoSensor * )
{ VpVec loc, vel;
  
  loc[0] = (frand() - 0.5) * 30;
  loc[1] = (frand() - 0.5) * 30;
  loc[2] = -70;

  printf("Obj %i: Location: %f, %f\n", ++objNum, loc[0], loc[1]);

  vel[2] = PrimaryDirection[2] + (frand() - 0.5) * 2;
  
  VpObject *obj = new VpObject(loc, vel);
  obj->setProperty(&gravity, 10, -1);

  Env.AssertObject(obj);
}    

VpObject *centerObj;

main()
{
  printf(" %f %f %f\n", frand(), frand(), frand());

  PrimaryDirection.setValue(0,0,6);

  Env.getTime()->SetScale(1);
  Env.getTime()->SetFrequency(20);
  Env.AssertForce(&gravity);

  VpVec Loc(0,0,-17);

  centerObj = new VpObject; //Front Center, 0 velocity
  centerObj->setLoc(Loc);
  centerObj->setProperty(&gravity, 5000, 1);
  Env.AssertObject(centerObj);

  VpTime timer;
  timer.AssertCallback(bubbler);
//timer.SetFrequency(0.5);
  timer.StartTime();

  Env.StartVis();
  Env.StartSim();
}










