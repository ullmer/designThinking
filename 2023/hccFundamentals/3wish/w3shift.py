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

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

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

def shiftNObj(root, objName, pointA, pointB, duration = 3., step=10):
  try:
    pointA3f = convertDest3f(pointA)
    pointB3f = convertDest3f(pointB)

    moveNObj(root, objName, pointA3f)
    transName   = genTransName(objName)
    targetTrans = getNObj(transName)

    shiftObj(targetTrans, pointA3f, pointB3f, steps, duration)
    return True
  except:
    print("moveNObj exception:"); traceback.print_exc()
    return False

################# shift object ################# 

def shiftObj(transNode, pointA, pointB, duration=3., steps=10, tween='linear'):

  try:
    #Calculate movement increment
    #printf("ShiftObj invoked (%i/%f)\n", steps, duration);

    pointA3f = convertDest3f(pointA)
    pointB3f = convertDest3f(pointB)

    currentPosition = pointA3f
    increment3f     = (pointB3f - pointA3f)/(float)steps

    #Set up callback info record

    timer    = coin.SoTimerSensor()
    interval = duration/steps

    shifttoRec = w3Shift(trans=transNode, pointA=pointA, pointB=pointB, timerSensor=timer,
                         moveIncr=increment3f, callbacksRemaining=steps, interval=interval)

    #Set up Inventor timer callback
    timer.setInterval(interval)
    timer.setFunction(shiftobjCallback)
    timer.setData(shitToRec)
    timer.schedule()

    #print("shiftObj scheduled")

################# shift object callback ################# 

def shiftobjCallback(data, sensor):
  shiftToRecord = (w3Shift) data

  #Calculate new position
  shiftToRecord.currentLoc += shiftToRecord.moveIncrement

  shiftToRecord.trans.setValue(shiftToRecord.currentLoc)
  shiftToRecord.callbacksRemaining -= 1

  #Clean up if we've reached where we're headed.
  if shiftToRecord.callbacksRemaining == 0:
    shiftToRecord.timerSensor.unschedule()

############## move Camera ############## 
# moveCamera {pointA} -- moves camera

def moveCamera(root, pointA, duration=3., steps=10):
  try:
    pointA3f = convertDest3f(pointA)
    root.getCamera().position.setValue(pointA3f)
    return True
  except:
    print("moveCamera exception:"); traceback.print_exc()
    return False

############## shift camera ############## 
# shiftTo {x y z} duration steps -- shifts camera

def shiftCamera(root, pointA, pointB, duration=3., steps=10):
  try:
    pointA3f = convertDest3f(pointA)
    pointB3f = convertDest3f(pointB)
    moveCamera(root, pointA, duration, steps)

    shiftCamTo(point, steps, duration);
    return True
  except:
    print("shiftCamera exception:"); traceback.print_exc()
    return False


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
