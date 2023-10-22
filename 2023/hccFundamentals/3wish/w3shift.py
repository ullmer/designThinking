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
  viewer        = None
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
  try:
    # initially, accept two versions of destination: list of floats or SbVec3f
    if isinstance(dest, list):
      dest3f = coin.SbVec3f(dest)
    elif dest.isOfType(coin.SbVec3f.getClassTypeId()):
      dest3f = dest
    else:
      print("convertDest3f error: destination does not appear to be of type list or SbVec3f");
      return None

    return dest3f
  except:
    print("convertDest3f exception:"); traceback.print_exc()
    return None

################# moveNObj ################# 
# syntax:  moveNObj named-obj point1

def moveNObj(root, objName, dest):
  try:
    dest3f = convertDest3f(dest)

    #Look for existing trans.  If present, use; if not, create.
    transName  = genTransName(objName)
    targetNode = getNamedNode(root, transName)

    if targetNode is not None:
      targetTrans = targetNode
    else:
      parent = getParentFrame(root, objName)
      targetTrans = coin.SoTranslation()
      targetTrans.setName(transName)
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

    print(pointA3f.type(), pointB3f.type())

    incr3f     = (pointB3f - pointA3f)/steps

    #Set up callback info record
    timer    = coin.SoTimerSensor()
    interval = duration/steps

    shifttoRec = w3Shift(trans=transNode, pointA=pointA, pointB=pointB, timerSensor=timer,
                         moveIncr=incr3f, callbacksRemaining=steps, interval=interval)

    #Set up Inventor timer callback
    timer.setInterval(interval)
    timer.setFunction(shiftobjCallback)
    timer.setData(shiftToRec)
    timer.schedule()

    #print("shiftObj scheduled")
  except:
    print("shiftObj exception:"); traceback.print_exc()
    return False

################# shift object callback ################# 

def shiftobjCallback(data, sensor):
  try:
    shiftToRecord = data

    #Calculate new position
    shiftToRecord.currentLoc += shiftToRecord.moveIncrement

    shiftToRecord.trans.setValue(shiftToRecord.currentLoc)
    shiftToRecord.callbacksRemaining -= 1

    #Clean up if we've reached where we're headed.
    if shiftToRecord.callbacksRemaining == 0:
      shiftToRecord.timerSensor.unschedule()
  except:
    print("shiftObjCallback exception:"); traceback.print_exc()
    return False
  
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

def shiftCamera(viewer, root, pointA, pointB, duration=3., steps=10):
  try:
    pointA3f = convertDest3f(pointA)
    pointB3f = convertDest3f(pointB)
    moveCamera(root, pointA, duration, steps)

    shiftCamTo(viewer, point, steps, duration);
    return True
  except:
    print("shiftCamera exception:"); traceback.print_exc()
    return False

############## shift camera to... ############## 

def shiftCamTo(viewer, destination, steps, duration):
  #printf("shiftto setup (%f %f %f) %i %f\n",
  #  (*destination)[0], (*destination)[1], (*destination)[2],
  #  steps, duration);

  try:
    #Calculate movement increment
    camera     = viewer.getCamera()
    currentPos = camera.position.getValue()
    increment  = (destination-currentPos) / steps

    #Set up callback info record
    timer    = coin.SoTimerSensor()
    shifttoRec = w3Shift(trans=transNode, pointB=destination, timerSensor=timer, viewer=viewer,
                         moveIncr=increment3f, callbacksRemaining=steps, interval=interval)

    timer.setInterval(interval)
    timer.setFunction(shiftCamCallback)
    timer.setData(shiftToRec)
    timer.schedule()
  except:
    print("shiftCamTo exception:"); traceback.print_exc()
    return False

############## shift camera callback ############## 

def shiftCamCallback(data, sensor):
  try:
    shiftToRecord = data
    shiftToRecord.currentLoc += shiftToRecord.moveIncrement
    viewer.getCamera().position.setValue(shiftToRecord.currentLoc)

    #print("shiftto callback");
    shiftToRecord.callbacksRemaining -= 1

    #Clean up if we've reached where we're headed.
    if shiftToRecord.callbacksRemaining == 0:
      shiftToRecord.timerSensor.unschedule()

  except:
    print("shiftCamCallback exception:"); traceback.print_exc()
    return False

################# shift object callback ################# 

def shiftobjCallback(data, sensor):
  try:
    #Calculate new position
    shiftToRecord.trans.setValue(shiftToRecord.currentLoc)
    shiftToRecord.callbacksRemaining -= 1

    #Clean up if we've reached where we're headed.
    if shiftToRecord.callbacksRemaining == 0:
      shiftToRecord.timerSensor.unschedule()
  except:
    print("shiftObjCallback exception:"); traceback.print_exc()
    return False
  
### end ###
