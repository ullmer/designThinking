# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import pygame as pg
import sys
from   functools       import partial
#from   pgzero.builtins import Actor, animate, keyboard
from   pgzero.builtins import Actor
import pgzero.builtins.animate as pgzAnimate

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

#https://github.com/MariwanJ/COIN3D_Snippet/blob/main/02.1.HelloCone.py

cubeActor = {}

t1 = coin.SoTranslation()
t1.translation.setValue([5,5,5])

global cubeActor, t1

a = cubeActor[0] = Actor(pos=winCoord, image='single_pix')

pgzAnimate(a, pos=(10,0), tween='accel_decel', duration=5)

def updateCube():
  global cubeActor, t1
  x, y = cubeActor[0].pos
  t1.translation.setValue([x, y, 0])

def update(): updateCube()

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

#idlecallback to drive animation updates

### end ###
