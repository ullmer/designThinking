//Test of SimpleVisualEnvironment with sparsely populated first-trial sim.
//Brygg Ullmer; 06/04/1993

// DTM-driven remote request handler

#define __DTMCPP__

#include "vp.h"
#include "vis.h"
#include "forces.h"
#include "objects.h"
#include "dtm.h"
#include <stdlib.h>

VpveEvent Env;

VpVec PrimaryDirection;

VpDtmSimpleObjReader *netReader;


static char *StrDB[] = 
  {"Absolutely", "Positively", "Unquestionably", "No doubt"};

int StrDBsize = 3;


inline float frand() //Returns a float from 0 to 1
{ return (float) rand() / (float) RAND_MAX; }



static void
bubbler( void *data, SoSensor * )
{ VpVec loc, vel;
  VpSimpleObjStruct *objStruct;

  if (!netReader->dataAvailable()) return;
  
  objStruct = netReader->readRecord();

  loc[0] = (frand() - 0.5) * 30;
  loc[1] = (frand() - 0.5) * 30;
  loc[2] = -70;

//  for (int i=0; i<3; i++)
//    loc[i] = objStruct->location[i];

  char *Name = (char *) objStruct;

  printf("New object \"%s\" received from net\n",Name);
//  printf("Location: %f, %f\n", loc[0], loc[1]);

  for (int i=0; i<3; i++)
    vel[i] = PrimaryDirection[i] + 
      (frand() - 0.5) * 5;

  Env.AssertObject(new VpoText(loc, vel, Name));
}    


main()
{
  PrimaryDirection.setValue(0,0,7);
  netReader = new VpDtmSimpleObjReader;

  Env.getTime()->SetScale(1);
  Env.getTime()->SetFrequency(5);

  VpTime timer;
  timer.AssertCallback(bubbler);
  timer.StartTime();

  Env.StartVis();
  Env.StartSim();
}










