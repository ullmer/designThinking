//// Wish3 Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95

#include "w3shift.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

typedef struct {
  SbVec3f *dest;
  SbVec3f *currentLoc;
  SbVec3f *moveIncrement;
  SoTranslation *trans;
  float interval;
  int callbacksRemaining;
  SoTimerSensor *timerSensor;
} shifttoRecord;


////////////////////////// Tcl MoveNObj //////////////////////////
// syntax:  moveNObj named-obj {point 1} 

int TclMoveNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{

  if (argc != 3) {
    interp->result = 
      "bad # args; moveNObj objtrans point";
    return TCL_ERROR;
  }

  char *transname = argv[1];
  char *Cpoint1 = argv[2];

  SbVec3f *point1 = convTcl2Iv_vert(Cpoint1);

//Look for existing trans.  If present, use; if not, create.
  SoNode *targetnode = getNamedNode(transname);
  SoTranslation *targettrans;
  if (targetnode != NULL) {targettrans = (SoTranslation *)targetnode;}
  else { //create node
    SoSeparator *parent = getParentFrame(transname);
    targettrans = new SoTranslation;
    targettrans->setName(transname);
    parent->insertChild(targettrans, 0); //prepend
  }

  targettrans->translation.setValue(*point1);

  return TCL_OK;
}

////////////////////////// Tcl Shift NObj //////////////////////////
// syntax:  shiftNObj named-obj {point 1} {point 2} duration steps

int TclShiftNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
//defaults
   const int defaultSteps = 10;
   const float defaultDuration = 3.;

  if (argc > 6 || argc < 4) {
    interp->result = 
      "bad # args; shiftNObj objtrans point1 point2 [duration] [steps]";
    return TCL_ERROR;
  }

  char *transname = argv[1];
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
  SoNode *targetnode = getNamedNode(transname);
  SoTranslation *targettrans;
  if (targetnode != NULL) {targettrans = (SoTranslation *)targetnode;}
  else { //create node
    SoSeparator *parent = getParentFrame(transname);
    targettrans = new SoTranslation;
    targettrans->setName(transname);
    parent->insertChild(targettrans, 0); //prepend
  }

  ShiftObj(targettrans, point1, point2, steps, duration);

  return TCL_OK;
}


void ShiftObj(SoTranslation *trans, 
  SbVec3f *basevec, SbVec3f *targetvec, int steps, float duration)
{

// Calculate movement increment

//printf("ShiftObj invoked (%i/%f)\n", steps, duration);

  SbVec3f *currentPosition = basevec;

  SbVec3f *increment = new SbVec3f;
  *increment = ((*targetvec - *basevec)/(float)steps);

// Set up callback info record

  shifttoRecord *record = new shifttoRecord;
  record->trans = trans;
  record->currentLoc = currentPosition;
  record->dest = targetvec;
  record->moveIncrement = increment;
  record->interval = duration / steps;
  record->callbacksRemaining = steps;

// Set up Inventor timer callback
  SoTimerSensor *timer = new SoTimerSensor;
  record->timerSensor = timer;

  timer->setInterval(record->interval); 
  timer->setFunction(shiftobjCallback);
  timer->setData(record);
  timer->schedule();
  
//  printf("ShiftObj scheduled\n");
}

void shiftobjCallback(void *data, SoSensor *)
{ 
  shifttoRecord *record = (shifttoRecord *)data;

//Calculate new position
  SbVec3f *currentPosition = record->currentLoc;
  *currentPosition += *(record->moveIncrement);

  SoTranslation *trans = record->trans;
  trans->translation.setValue(*currentPosition);
  
/*  printf("shiftto setup (%f %f %f)\n",
    (*currentPosition)[0], (*currentPosition)[1], (*currentPosition)[2]);
     
*/
  (record->callbacksRemaining)--;

//Clean up if we've reached where we're headed.
  if (record->callbacksRemaining == 0) {

    record->timerSensor->unschedule();
    delete record->dest;
    delete record;
  }
}

////////////////////////// Tcl MoveTo//////////////////////////
// moveTo {x y z} -- moves camera

int TclMoveTo(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
//defaults
   const int defaultSteps = 10;
   const float defaultDuration = 3.;

//Convert arguments

   if (argc != 2) {
     interp->result = "bad # args; moveTo point";
     return TCL_ERROR;
   }

  char *Spoint = argv[1];
  SbVec3f *point = convTcl2Iv_vert(Spoint);

  myViewer->getCamera()->position.setValue(*point);
  //delete point;

  return TCL_OK;
}

////////////////////////// Tcl ShiftTo//////////////////////////
// shiftTo {x y z} duration steps -- shifts camera

int TclShiftTo(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
//defaults
   const int defaultSteps = 10;
   const float defaultDuration = 3.;

//Convert arguments

   if (argc > 4 || argc < 2) {
     interp->result = "bad # args; shiftTo point {duration 3} {steps 10}";
     return TCL_ERROR;
   }

  char *Spoint = argv[1];
  SbVec3f *point = convTcl2Iv_vert(Spoint);

  float duration;
  if (argc > 2) {duration = atof(argv[2]);}
  else {duration = defaultDuration;}

  int steps;
  if (argc > 3) {steps = atoi(argv[3]);}
  else {steps = defaultSteps;}

  ShiftCamTo(point, steps, duration);
  return TCL_OK;
}


void ShiftCamTo(SbVec3f *destination, int steps, float duration)
{

/*   printf("shiftto setup (%f %f %f) %i %f\n",
     (*destination)[0], (*destination)[1], (*destination)[2],
     steps, duration);
*/
// Calculate movement increment

  SoCamera *camera = myViewer->getCamera();
  SbVec3f currentPosition = camera->position.getValue();

  SbVec3f *increment = new SbVec3f;
  *increment = ((*destination - currentPosition)/(float)steps);

// Set up callback info record

  shifttoRecord *record = new shifttoRecord;
  record->dest = destination;
  record->moveIncrement = increment;
  record->interval = duration / steps;
  record->callbacksRemaining = steps;

// Set up Inventor timer callback
  SoTimerSensor *timer = new SoTimerSensor;
  record->timerSensor = timer;

  timer->setInterval(record->interval); 
  timer->setFunction(shiftcamCallback);
  timer->setData(record);
  timer->schedule();
  
}

void shiftcamCallback(void *data, SoSensor *)
{ 
  shifttoRecord *record = (shifttoRecord *)data;

//Calculate new position
  SbVec3f currentPosition = myViewer->getCamera()->position.getValue();
  currentPosition += *(record->moveIncrement);

  myViewer->getCamera()->position.setValue(currentPosition);

//  printf("shiftto callback\n");

  (record->callbacksRemaining)--;

//Clean up if we've reached where we're headed.
  if (record->callbacksRemaining == 0) {

    record->timerSensor->unschedule();
    delete record->dest;
    delete record;
  }
}

