//// 3wish Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Inherited from w3shift.cc, 12/5/95

#include "w3rot.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

typedef struct {
  SoRotation *rot;
  SbVec3f *dest;
  SbVec3f *currentLoc;
  SbVec3f *moveIncrement;
  float interval;
  int callbacksRemaining;
  SoTimerSensor *timerSensor;
} rottoRecord;

typedef struct {
  SbRotation *orig;
  SbRotation *dest;
  float interp;
  float f;
  float increment;
  float interval;
  int callbacksRemaining;
  SoTimerSensor *timerSensor;
} camrottoRecord;

////////////////////// Do rotation by the angles /////////////////////

SbRotation *hprToRot(float heading, float pitch, float roll) {

  SbRotation tmp, r,p,h; 
// Heading = XZ, rot y
// Pitch   = YZ, rot x
// Roll    = XY, rot z

  r.setValue(SbVec3f(0,0,1), roll);

  p.setValue(SbVec3f(1,0,0), pitch);

  h.setValue(SbVec3f(0,1,0), heading);

  tmp = r*p*h;

  SbRotation *result = new SbRotation();
  result->setValue(tmp.getValue());

  float a,b,c,d;
  result->getValue(a,b,c,d);
//  printf("hprToRot: %f %f %f -> %f %f %f %f\n",
//    heading, pitch, roll,
//    a,b,c,d);

  return result; 
}

SbRotation *dhprToRot(float heading, float pitch, float roll) {

  return hprToRot(heading*M_PI/180., pitch*M_PI/180., roll*M_PI/180.);
}

////////////////////////// Tcl Rotate NObj //////////////////////////
// syntax:  rotNObj named-obj {rotation}

int TclRotNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
//defaults
   const int defaultSteps = 10;
   const float defaultDuration = 3.;

  if (argc != 3) {
    interp->result = 
      "bad # args; rotNObj objrot rot";
    return TCL_ERROR;
  }

  char *rotname = argv[1];
  char *Cpoint1 = argv[2];

  SbVec3f *point1 = convTcl2Iv_vert(Cpoint1);

//Look for existing rot.  If present, use; if not, create.
  SoNode *targetnode = getNamedNode(rotname);
  SoRotation *targetrot;
  if (targetnode != NULL) {targetrot = (SoRotation *)targetnode;}
  else { //create node
    SoSeparator *parent = getParentFrame(rotname);
    targetrot = new SoRotation;
    targetrot->setName(rotname);
    parent->insertChild(targetrot, 0); //prepend
  }

  SbVec3f *a=point1;
  SbRotation *srot = dhprToRot((*a)[0], (*a)[1], (*a)[2]);
  targetrot->rotation.setValue(srot->getValue());
  delete srot;

  return TCL_OK;
}

////////////////////////// Tcl Spin NObj //////////////////////////
// syntax:  shiftNObj named-obj {point 1} {point 2} duration steps

int TclSpinNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
//defaults
   const int defaultSteps = 10;
   const float defaultDuration = 3.;

  if (argc > 6 || argc < 4) {
    interp->result = 
      "bad # args; spinNObj objrot point1 point2 [duration] [steps]";
    return TCL_ERROR;
  }

  char *rotname = argv[1];
  char *Cpoint1 = argv[2], *Cpoint2 = argv[3];

  SbVec3f *point1 = convTcl2Iv_vert(Cpoint1);
  SbVec3f *point2 = convTcl2Iv_vert(Cpoint2);

  float duration;
  if (argc > 4) {duration = atof(argv[4]);}
  else {duration = defaultDuration;}

  int steps;
  if (argc > 5) {steps = atoi(argv[5]);}
  else {steps = defaultSteps;}

//Look for existing trans.  If present, use; if not, create.
  SoNode *targetnode = getNamedNode(rotname);
  SoRotation *targetrot;
  if (targetnode != NULL) {targetrot = (SoRotation *)targetnode;}
  else { //create node
    SoSeparator *parent = getParentFrame(rotname);
    targetrot = new SoRotation;
    targetrot->setName(rotname);
    parent->insertChild(targetrot, 0); //prepend
  }

  SpinObj(targetrot, point1, point2, steps, duration);

  return TCL_OK;
}

void SpinObj(SoRotation *rot, 
  SbVec3f *basevec, SbVec3f *targetvec, int steps, float duration)
{

// Calculate movement increment

//printf("RotObj invoked (%i/%f)\n", steps, duration);

  SbVec3f *currentPosition = basevec;

  SbVec3f *increment = new SbVec3f;
  *increment = ((*targetvec - *basevec)/(float)steps);

// Set up callback info record

  rottoRecord *record = new rottoRecord;
  record->rot = rot;
  record->currentLoc = currentPosition;
  record->dest = targetvec;
  record->moveIncrement = increment;
  record->interval = duration / steps;
  record->callbacksRemaining = steps;

// Set up Inventor timer callback
  SoTimerSensor *timer = new SoTimerSensor;
  record->timerSensor = timer;

  timer->setInterval(record->interval); 
  timer->setFunction(spinobjCallback);
  timer->setData(record);
  timer->schedule();
  
  //printf("RotObj scheduled\n");
}

void spinobjCallback(void *data, SoSensor *)
{ 
  rottoRecord *record = (rottoRecord *)data;

//printf ("rotobj callback\n");

//Calculate new position
  SbVec3f *currentPosition = record->currentLoc;
  *currentPosition += *(record->moveIncrement);
  SbVec3f *a = currentPosition;

  SbRotation *srot = dhprToRot((*a)[0], (*a)[1], (*a)[2]);

  SoRotation *rot = record->rot;
  rot->rotation.setValue(srot->getValue());
  delete srot;
  
  (record->callbacksRemaining)--;

//Clean up if we've reached where we're headed.
  if (record->callbacksRemaining == 0) {

    record->timerSensor->unschedule();
    delete record->dest;
    delete record;
  }
//  printf ("rotobj exiting (%i)\n", record->callbacksRemaining);
}

////////////////////////// Tcl RotTo//////////////////////////
// rotTo {x y z} -- rotates camera

int TclRotTo(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 

//Convert arguments

   if (argc != 2) {
     interp->result = "bad # args; rotTo [hpr orient]";
     return TCL_ERROR;
   }

  char *Spoint = argv[1];
  SbVec3f *rot= convTcl2Iv_vert(Spoint);

  SbRotation *destrot = new SbRotation;
  destrot = dhprToRot((*rot)[0], (*rot)[1], (*rot)[2]);

  myViewer->getCamera()->orientation.setValue(*destrot);

  return TCL_OK;
}

////////////////////////// Tcl SpinTo//////////////////////////
// spinTo {x y z} duration steps -- spins camera

int TclSpinTo(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 

//defaults
   const int defaultSteps = 30;
   const float defaultDuration = 1.5;

//Convert arguments

   if (argc > 4 || argc < 2) {
     interp->result = "bad # args; rotateTo vec {duration 1.5} {steps 30}";
     return TCL_ERROR;
   }

  char *Spoint = argv[1];
  SbVec3f *point = convTcl2Iv_vert(Spoint);
//printf("RotTo called, <%s>\n", Spoint);

  float duration;
  if (argc > 2) {duration = atof(argv[2]);}
  else {duration = defaultDuration;}

  int steps;
  if (argc > 3) {steps = atoi(argv[3]);}
  else {steps = defaultSteps;}

  //printf("<passing %f %f %f>\n", (*point)[0], (*point)[1], (*point)[2]);
  RotateCamTo(point, steps, duration);
  return TCL_OK;
}


void RotateCamTo(SbVec3f *dest, int steps, float duration)
{

// Calculate movement increment

  camrottoRecord *record = new camrottoRecord;

  SoCamera *camera = myViewer->getCamera();

  SbRotation *orig = new SbRotation;
  *orig = camera->orientation.getValue();

  record->orig = orig;
  record->interp = 0;
  record->f = 0;
  record->increment = 1./(float)steps;

//printf("increment %f\n", record->increment);

  record->callbacksRemaining = steps;
  record->interval = duration/(float)steps;
  
  SbRotation *destrot = new SbRotation;
  destrot = dhprToRot((*dest)[0], (*dest)[1], (*dest)[2]);
  record->dest = destrot;

float a,b,c,d;
record->orig->getValue(a,b,c,d);
//printf("orig %f %f %f %f\n", a,b,c,d);

record->dest->getValue(a,b,c,d);
//printf("dest %f %f %f %f\n", a,b,c,d);

// Set up callback info record

  SoTimerSensor *timer = new SoTimerSensor;
  record->timerSensor = timer;

  timer->setInterval(record->interval); 
  timer->setFunction(rotcamCallback);
  timer->setData(record);
  timer->schedule();
  
}

////////////////////// Rot Cam Callback /////////////////////

void rotcamCallback(void *data, SoSensor *)
{ 
  camrottoRecord *record = (camrottoRecord *)data;

//Spherically interpolate between origin and destination rotations.
  record->f += record->increment;
  SbRotation rot = SbRotation::slerp(*(record->orig), *(record->dest),
    record->f);

//Calculate new position

  myViewer->getCamera()->orientation.setValue(rot);

//  printf("camrotto callback, interp %f (%f)\n", record->f, record->increment);

  (record->callbacksRemaining)--;

//Clean up if we've reached where we're headed.
  if (record->callbacksRemaining == 0) {

    record->timerSensor->unschedule();
    delete record->orig;
    delete record->dest;
    delete record;
  }
}

