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

def updateCube(val, whichCube):
  global cubeActor, t1, lastTime, anima
  nt = time.time()
  dt = nt-lastTime
  lastTime = nt

  try:    
    anima.update(dt)
    x, y = cubeActor[0].pos
    #print("x, y:", x, y)
    t1.translation.setValue([x, y, 0])
    #Gui.updateGui()
    #idleSensor = coin.SoIdleSensor(updateCube, 0)
    #idleSensor.schedule()
    view.redraw()
  except: pass
    #print("updateCube exception:")
    #print(traceback.print_exc());

#def update(): updateCube()

####### pygame zero update loop ####### 
#def update(): 
#  root.update() #keeps TkInter alive
#root.mainloop()

view = Gui.ActiveDocument.ActiveView
sg = view.getSceneGraph()

root = coin.SoSeparator()
sg.addChild(root)

c1 = coin.SoCube()
c2 = coin.SoCube()

C1 = coin.SoMaterial()
C1.diffuseColor.setValue([1,0,0])

for child in [c1, t1, C1, c2]: root.addChild(child)

view.redraw()
Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

#idleSensor = coin.SoIdleSensor(updateCube, 0)
#idleSensor.schedule()

ts = coin.SoTimerSensor(updateCube, 0)
ts.schedule()

#idlecallback to drive animation updates

### end ###
