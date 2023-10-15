# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import pygame as pg
import sys, time, traceback
from   functools       import partial
from   pgzero.builtins import Actor, animate, keyboard
import pgzero

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

#https://github.com/MariwanJ/COIN3D_Snippet/blob/main/02.1.HelloCone.py

global cubeActor, t1, anima, lastTime

cubeActor = {}

t1 = coin.SoTranslation()
t1.translation.setValue([5,5,5])

#pgzero.loaders.set_root('/home/bullmer/git/designThinking/2023/hccFundamentals/freecadPgz')

DISPLAY_FLAGS = pg.SHOWN
pg.display.set_mode((100,100), flags=(DISPLAY_FLAGS & ~pg.SHOWN) | pg.HIDDEN,)
pg.display.init()
pgzero.loaders.set_root('c:/git/designThinking/2023/hccFundamentals/freecadPgz/')

a = Actor(pos=(0,0), image='single_pix')
cubeActor[0] = a

anima = animate(a, pos=(20,0), tween='accel_decel', duration=1)
lastTime  = time.time()

############ update cube ############ 

def updateCube(unsureArg, whichCube):
  global cubeActor, t1, lastTime, anima
  nt = time.time()
  dt = nt-lastTime
  lastTime = nt

  try:    
    anima.update(dt)
    x, y = cubeActor[0].pos
    t1.translation.setValue([x, y, 0])
    #view.redraw()
  except: pass
    #print("updateCube exception:")
    #print(traceback.print_exc());


############ mouse callback ############ 
# see https://github.com/coin3d/pivy/blob/master/examples/Mentor/09.4.PickAction.py

def myMousePressCB(userData, eventCB): 
  root  = userData
  event = eventCB.getEvent()

  if coin.SoMouseButtonEvent.isButtonPressEvent(event, coin.SoMouseButtonEvent.ANY):
    print("mouse pressed") 
    myRegion = eventCB.getAction().getViewportRegion()
    writePickedPath(root, myRegion, event.getPosition(myRegion))
    eventCB.setHandled()

############ write picked path ############ 
# see https://github.com/coin3d/pivy/blob/master/examples/Mentor/09.4.PickAction.py

def writePickedPath(root, viewport, cursorPosition): 
  myPickAction = coin.SoRayPickAction(viewport)
  myPickAction.setPoint(cursorPosition)
  myPickAction.setRadius(8.0) #8 pixel radius around selected pixel

  myPickAction.apply(root)
  myPickedPoint = myPickAction.getPickedPoint()
  if myPickedPoint is None: return False

  myWriteAction = coin.SoWriteAction()
  myWriteAction.apply(myPickedPoint.getPath())
  return True

############ main ############ 

view = Gui.ActiveDocument.ActiveView
sg = view.getSceneGraph()

root = coin.SoSeparator()
sg.addChild(root)

# see https://github.com/coin3d/pivy/blob/master/examples/Mentor/09.4.PickAction.py

myEventCB = coin.SoEventCallback()
root.addChild(myEventCB)

mbe = coin.SoMouseButtonEvent.getClassTypeId()
myEventCB.addEventCallback(mbe, myMousePressCB, sg)

c1 = coin.SoCube()
c2 = coin.SoCube()

C1 = coin.SoMaterial()
C1.diffuseColor.setValue([1,0,0])

for child in [c1, t1, C1, c2]: root.addChild(child)

view.redraw()
Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

#idleSensor = coin.SoIdleSensor(updateCube, 0)  #I regard idle sensors as preferable over timer sensors,
#idleSensor.schedule()                          # but they don't seem to be retriggering reliably in FreeCAD

ts = coin.SoTimerSensor(updateCube, 0)
ts.schedule()

### end ###
