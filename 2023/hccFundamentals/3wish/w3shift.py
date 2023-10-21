# 3Wish Python port
# By Brygg Ullmer (orig version @MIT Media Lab, port @Clemson University)
# Originally disaggregated from tcl_examp3 1995-11-24
# Python port begun 2023-10-20

import pivy.coin as coin
import traceback
from   w3core import *

################# shift data ################# 

class w3Shift:

  dest          = None # SbVec3f *dest;
  currentLoc    = None # SbVec3f *currentLoc;
  moveIncrement = None # SbVec3f *moveIncrement;
  trans         = None # SoTranslation *trans;
  interval      = None # float interval;
  timerSensor   = None  #SoTimerSensor *timerSensor;
  callbacksRemaining = None #int callbacksRemaining;

################# generate translation node name ################# 

def genTransName(objName):
  global HIERSEP_CHAR
  transName = objName + HIERSEP_CHAR + 'trans'
  return transName
  
def convertDest3f(dest):
  # initially, accept two versions of destination: list of floats or SbVec3f
  if dest.isOfType(coin.SbVec3f.getClassTypeId()):
    dest3f = dest
  elif isinstance(dest, list):
    dest3f = coin.SbVec3f(dest)
  else:
    print("convertDest3f error: destination does not appear to be of type list or SbVec3f");
    return None

  return dest3f

################# moveNObj ################# 
# syntax:  moveNObj named-obj point1

def moveNObj(root, objName, dest):
  try:
    dest3f = convertDest3f(dest)

    #Look for existing trans.  If present, use; if not, create.
    transName  = genTransName(objName)
    targetNode = getNamedNode(transName)

    if targetNode is not None:
      targetTrans = targetNode
    else:
      parent = getParentFrame(root, objName)
      targetTrans = coin.SoTranslation()
      targettrans.setName(transName)
      parent.insertChild(targetTrans, 0) #prepend

    targetTrans.translation.setValue(dest3f)
  except:
    print("moveNObj exception:"); traceback.print_exc()
    return False

  return True

################# Shift Named Obj ################# 
# syntax:  shiftNObj named-obj {point1} {point2} duration steps

def shiftNObj(root, name, pointA, pointB, duration = 3., step=10):
  try:
    pointA3f = convertDest3f(pointA)
    pointB3f = convertDest3f(pointB)

  char *transname = argv[1];
  char *Cpoint1 = argv[2], *Cpoint2 = argv[3];


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

    shiftObj(targetTrans, pointA3f, pointB3f, steps, duration)
    return True
  except:
    print("moveNObj exception:"); traceback.print_exc()
    return False

################# shift object ################# 

def shiftObj(transNode, pointA3f, pointB3f, duration=3., steps=10):

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

### end ###
