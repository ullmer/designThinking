// Tst12 with Fly viewer
// 07/22/93

#include "vp.h"
#include "vis.h"
#include "visenv.h"
#include "visobj.h"
#include "forces.h"
#include "objects.h"

#include <stdlib.h>
#include <Inventor/viewers/SoXtFlyViewer.h>
#include "menu.h"

VpveEvent Env;

VpVec PrimaryDirection;

float speed = 90; //60; //30; //15;
float volume = 32; //64; //16; //8; //4;
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

void fixSpeed();
void fixVolume();

static float colA[3] = {0,0,0.2}, colB[3] = {1,0,0};
static float c2A[3] = {0,1,1}, c2B[3] = {1,1,0};

VpTime timer;

main()
{
  ///Basic setup

  Env.getTime()->SetScale(1);
  Env.getTime()->SetFrequency(12);

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

//  vsa->activateProcessing(Env.getObjects(), 0.1);
//  vsa->setColorBounds(c2A, c2B, 3);

//  Env.AssertVpvObject(vsa);
  Env.AssertVpvObject(vsa2);

  ///Set up bubblers, executioners, camera crew

  timer.AssertCallback(bubbler);
  timer.SetFrequency(volume);
  timer.StartTime();

  VpTime timesUp;
  timesUp.AssertCallback(execution);
  timesUp.StartTime();

  ///Window size

  SbVec2s winsize(900, 750);
  SoXt::setWidgetSize(*(Env.getWindow()), winsize);

  ///Add sliders

  VpuScrollbarList sbl;
  
  sbl.addEntry("Speed", &speed, 0.1, 150, 90, fixSpeed);
  sbl.addEntry("Volume", &volume, 0.1, 90, 32, fixVolume);
  sbl.addEntry("Alignment", &vspread, 0, 20, 10);
  sbl.addEntry("Breadth", &wspread, 0, 60, 40);
  sbl.go();

/*
float speed = 90; //60; //30; //15;
float volume = 32; //64; //16; //8; //4;
float vspread = 10; //6; //4
float wspread = 40; //20;
float depth = -240; //-120;
*/

  ///Go

  Env.StartVis();
  Env.StartSim();
}

void fixSpeed()
{ PrimaryDirection.setValue(0,0,speed); }

void fixVolume()
{ timer.SetFrequency(volume); }


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
