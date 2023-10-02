#include "vp.h"
#include "vis.h"
#include "visobj.h"
#include "visenv.h"
#include "forces.h"
#include "objects.h"
#include <stdlib.h>

#include <Inventor/viewers/SoXtExaminerViewer.h>
#include <Inventor/viewers/SoXtFullViewer.h>
#include "menu.h"

VpveEvent Env;

VpVec randomLoc();
void readData(int numPeople, char *filename);

const int centerZ = -40;
const int bounds = 5;

const float peopleApart = 150.;
const float coreVal = 100; //Attraction of core to other objects

void zeroVel(void *, SoSensor *);
void focusCam(void *, SoSensor *);

inline void printV(VpVec p);

VpObject *focus;

VpTime timer;
float timerFreq = 1.0; //This will get longer
float timerInc = 0.2;

PosBlender dirBlender(20), posBlender(20);


VpfGravity *peopleRepulsion;
float PRepulsionConst = -0.01; 
float PRC = -2;

VpfGravity *groupRepulsion;
float GRepulsionConst = -0.1;
float GRC = -1;

MakeList(VpfBand, VpfBands);
VpfBands bands;
float BRepulsionConst = 1e-3;
float BRC = -3;

void fixPeople();
void fixGroup();
void fixBand();

main(int argc, char **argv)
{
///Parameter initiation

  if (argc < 3) {fprintf(stderr,"Please tell me the # people!\n"); exit(-1);}

  int numPeople = atoi(argv[1]);
  char *filename = argv[2];

  if (argc >= 4) 
    { unsigned int n = atoi(argv[3]);
      
//    printf("Seeded %i\n", n); 
//Uncommenting the prev line kills the program

      srand(n);
    }

  readData(numPeople, filename);

///Set environmental controls, focus timers, etc.

  Env.getTime()->SetFrequency(20);
  Env.getTime()->SetScale(0.1);

  timer.AssertCallback(zeroVel);
//  timer.SetFrequency(1./timerFreq);
  timer.SetFrequency(10);
  timer.StartTime();

  VpTime focusTimer;
  focusTimer.AssertCallback(focusCam);
//  focusTimer.SetScale(1, Env.getTime());
  focusTimer.SetFrequency(15);
  focusTimer.StartTime();

///Window size

  SbVec2s winsize(900, 750);
  SoXt::setWidgetSize(*(Env.getWindow()), winsize);


///Viewer
/*
  SoXtExaminerViewer *flyView = new SoXtExaminerViewer;
  flyView->build(*(Env.getWindow()));
  flyView->setSceneGraph(Env.getShell());
  flyView->show();
*/

  ///Add sliders

  VpuScrollbarList sbl;

  sbl.addEntry("People repulsion", &PRC, -6, 6, -1, fixPeople);
  sbl.addEntry("Group repulsion", &GRC, -6, 6, -2, fixGroup);
  sbl.addEntry("Band attraction", &BRC, -6, 6, -3, fixBand);
  sbl.go();


///Go

  Env.StartVis();
  Env.StartSim();

}

void fixPeople()
{ PRepulsionConst = - pow(10,PRC);
  peopleRepulsion->setConst(PRepulsionConst); //Antigravity
}

void fixGroup()
{ GRepulsionConst = -pow(10,GRC);
  groupRepulsion->setConst(GRepulsionConst);
}

void fixBand()
{ BRepulsionConst = pow(10, BRC);
  bands.resetMarker();
  VpfBand *ptr= bands.next();

  while (ptr != NULL)
   { ptr->setConst(BRepulsionConst);
     ptr = bands.next();
   }
}

void focusCam(void *, SoSensor *)
{  
  //Interesting... if you reference the following blend sequence
  // (direction, then position) the propagation of errors REALLY
  // screws things up radically!

  if (focus != NULL && Env.getCamera() != NULL) 
    { 
      VpVec pos = focus->GetLoc(); 
      pos[2] -= centerZ; //pos[1] += 5;

      posBlender.setVec(pos);
      Env.getCamera()->position.setValue(posBlender.getVec());


//      float x,y,z;
//      focus->GetLoc().getValue(x,y,z);
//      printf("%f %f %f\n", x,y,z);

      dirBlender.setVec(focus->GetLoc());
      Env.getCamera()->pointAt(dirBlender.getVec());
    }  
}
  
void zeroVel(void *, SoSensor *)
{ VpVec Zero;

  VpObjects *objects = Env.getObjects();

//  timerFreq += timerInc;
  timer.SetFrequency(1./timerFreq);

  objects->resetMarker();
  VpObject *ptr = objects->first(); objects->next();

  while (ptr != NULL)
    { 
      ptr->ApplyVel(Zero);
      //ptr->ApplyVel(ptr->GetVel() * 0.1);

      ptr = objects->next();
    }
}

void readData(int numPeople, char *filename)
{
  FILE *in = fopen(filename,"rt");

  VpoText **people = (VpoText **)malloc(numPeople * sizeof(VpoText *));
  //new VpObject*[numPeople];
  VpVec Zero;

  peopleRepulsion = new VpfGravity;
//  peopleRepulsion->setConst(-0.1); //Antigravity
  peopleRepulsion->setConst(PRepulsionConst); //Antigravity
  peopleRepulsion->setPower(1.5);
  Env.AssertForce(peopleRepulsion);
  
//  char **names = new (char **)[numPeople];

  //Read People

  for(int i=0; i<numPeople; i++)
    { char *bname = new char[15];
      fscanf(in, "%s", bname); printf("%s\n", bname);
      people[i] = new VpoText(randomLoc(), Zero, bname);
      people[i]->setProperty(peopleRepulsion, peopleApart);
      Env.AssertTextObject(people[i], 0,0,1, 0);
    }

  //Read Groups

  float *values = new float[numPeople];

  groupRepulsion = new VpfGravity;
  groupRepulsion->setConst(GRepulsionConst); //Antigravity
  groupRepulsion->setPower(1.1);
  Env.AssertForce(groupRepulsion);

  int objNum = 0;

  while (!feof(in))
    { char *name = new char[20];
      fscanf(in, "%s", name);

      if (*name == NULL) continue;

      for(i=0; i<numPeople; i++)
	{ fscanf(in, "%f", &(values[i])); printf("%f ", values[i]); }
      
      VpoText *text = new VpoText(randomLoc(), Zero, name);
      Env.AssertTextObject(text, 0,1,0, 0);

      if (++objNum == 1) focus = text; 
        //Focus on first object (probably infoNots)

      VpfBand *band = new VpfBand;
      band->setConst(BRepulsionConst); //This value, tweaked an order of mag, can 
      //cause an explosion

      bands.append(band);

      int j=0;

      for(i=0; i<numPeople; i++)
	if (values[i] > 0)
	  { people[i]->setProperty(band, pow(values[i],2)); j++; }

      printf("Group %s, %i relations\n", name, j);

      if (j > 0) 
	{ text->setProperty(band, coreVal);
	  text->setProperty(groupRepulsion, coreVal*10);
	  Env.AssertForce(band);
	}
    }
}

inline float frand() //Returns a float from 0 to 1
{ return (float) rand() / (float) RAND_MAX; }

VpVec randomLoc()
{ float ret[3];

  for(int i=0; i<3; i++) ret[i] = 2*(frand() - 0.5)*bounds;
  ret[2] += centerZ;

  VpVec result(ret);

//  printV(result);

  return result;
}

void printV(VpVec v)
{ printf("<%f %f %f>\n", v[0], v[1], v[2]);
}
