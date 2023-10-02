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

VpVec PrimaryDirection;

float speed = 90; //60; //30; //15;
float volume = 64; //16; //8; //4;
float vspread = 10; //6; //4
float wspread = 40; //20;
float depth = -240; //-120;

inline float frand() //Returns a float from 0 to 1
{ return (float) rand() / (float) RAND_MAX; }

static void
bubbler( void *, SoSensor * )
{ VpVec loc, vel;
  
  loc[0] = (frand() - 0.5) * wspread;
  loc[1] = (frand() - 0.5) * wspread;
  loc[2] = depth;

//  printf("Location: %f, %f\n", loc[0], loc[1]);

  for (int i=0; i<3; i++)
    vel[i] = PrimaryDirection[i] + 
      (frand() - 0.5) * vspread;
  
  Env.AssertObject(new VpObject(loc, vel), frand(), frand(), frand());
}    


VpVec focus(0,0,-40);
int step=0, cycle=200;
float magnitude=20, baseLevel=15;

static void
cameraControl( void *, SoSensor * );

static void
execution( void *, SoSensor * );

static float colA[3] = {0,0,0.2}, colB[3] = {1,0,0};
static float c2A[3] = {0,1,1}, c2B[3] = {1,1,0};

main()
{
  ///Basic setup

  Env.getTime()->SetScale(1);
  Env.getTime()->SetFrequency(20);

  PrimaryDirection.setValue(0,0,speed);

  /// Set-up info density frame

  VpVec SimCenter(0,1,-50), Orient(0,0,1); VpVec Zero; 

  VpvPresenceIndicator *vsa = 
    new VpvPresenceIndicator(new VpObject(SimCenter, Zero),
			     15, 5, 10, Orient);

  VpvPresenceIndicator *vsa2 = 
    new VpvPresenceIndicator(new VpObject(SimCenter, Zero),
			     10, 20, 30, Orient);

  vsa2->activateProcessing(Env.getObjects(), 0.2);
  vsa2->setColorBounds(colA, colB, 10);

  vsa->activateProcessing(Env.getObjects(), 0.1);
  vsa->setColorBounds(c2A, c2B, 3);

  Env.AssertVpvObject(vsa);
  Env.AssertVpvObject(vsa2);

  ///Set up bubblers, executioners, camera crew

  VpTime timer;
  timer.AssertCallback(bubbler);
  timer.SetFrequency(volume);
  timer.StartTime();

  VpTime timesUp;
  timesUp.AssertCallback(execution);
  timesUp.StartTime();

  VpTime cameraCrew;
  cameraCrew.AssertCallback(cameraControl);
  cameraCrew.SetFrequency(20);
  cameraCrew.StartTime();

  ///Window size

  SbVec2s winsize(900, 750);
  SoXt::setWidgetSize(*(Env.getWindow()), winsize);

  ///Go

  Env.StartVis();
  Env.StartSim();
}

static void
cameraControl( void *, SoSensor * )
{ float val=(float)(step++)/cycle;

  float locX = magnitude*sin(val*M_PI*2);
  float locY = magnitude*cos(val*M_PI*2);

  VpVec loc(locY, locY, baseLevel);

  if (Env.getCamera() != NULL)
    { Env.getCamera()->position.setValue(loc);
      Env.getCamera()->pointAt(focus);
    }

}

static void
execution( void *, SoSensor * ) 
   //execution in the capital, decapitate him sense! :-)
{ VpvBases *bases = Env.getBases();

  if (bases->length() < 1) return;

  bases->resetMarker();
  VpvBase *ptr = bases->first(); bases->next();

  VpVec guinea;


  while (ptr != NULL)
    { if (guinea = ptr->getObj()->getLoc(), guinea[2] > -5.)
	{ Env.RetractPObject(ptr->getObj());
	  delete ptr->getObj(); //Only one environment, so kick'em off
	  Env.RetractVObject(ptr);
	}
      ptr = bases->next();
    }
}
