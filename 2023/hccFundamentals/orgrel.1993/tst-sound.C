//Test of SimpleVisualEnvironment with sparsely populated first-trial sim.
//Brygg Ullmer; 06/04/1993

//Operational 06/15
// Bubbles cubes from background.

#include "vp.h"
#include "vis.h"
#include "visobj.h"
#include "visenv.h"
#include "forces.h"
#include "objects.h"
#include "sound.h"
#include <stdlib.h>

static char *SoundFDB[] = {
"belltree_up2.aiff",
"harp_glis.Cmj.aiff",
"jar.aiff",
"orch_hit.aiff",
"slinky_slap.aiff",
"stereo_uparp.aiff",
"tag2.aiff",
"tag3.aiff"};

int numSound = 7;

VpveEvent Env;

VpfGravity gravity;

VpVec PrimaryDirection;

inline float frand() //Returns a float from 0 to 1
{ return (float) rand() / (float) RAND_MAX; }

static void
bubbler( void *data, SoSensor * )
{ VpVec loc, vel;
  char *string;
  
  loc[0] = (frand() - 0.5) * 30;
  loc[1] = (frand() - 0.5) * 30;
  loc[2] = -70;

  printf("Location: %f, %f\n", loc[0], loc[1]);

  vel[2] = PrimaryDirection[2] + (frand() - 0.5) * 2;
  
  VpObject *obj = new VpObject(loc, vel);
  obj->setProperty(&gravity, 500);

  int num = (int)(frand()*numSound);
//  printf("Sound %i attached (%s)\n", num, SoundFDB[num]);
  
  string = new char[50];
  sprintf(string, "sounds/%s", SoundFDB[num]);
  Env.AssertSoundObject(obj, string);
}    


main()
{
  printf(" %f %f %f\n", frand(), frand(), frand());
  
  PrimaryDirection.setValue(0,0,5);

  Env.getTime()->SetScale(1);
  Env.getTime()->SetFrequency(15);
  Env.AssertForce(&gravity);

  VpTime timer;
  timer.AssertCallback(bubbler);
//  timer.SetFrequency(0.5);
  timer.StartTime();

  ///Window size

  SbVec2s winsize(900, 750);
  SoXt::setWidgetSize(*(Env.getWindow()), winsize);


  Env.StartVis();
  Env.StartSim();
}










