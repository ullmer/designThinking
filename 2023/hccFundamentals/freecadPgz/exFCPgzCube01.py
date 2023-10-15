# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import pygame as pg
import sys
from   functools       import partial
from   pgzero.builtins import Actor, animate, keyboard

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

#https://github.com/MariwanJ/COIN3D_Snippet/blob/main/02.1.HelloCone.py

cubeActor = {}

#cubeActor[0] Actor(pos=winCoord, image='single_pix'
#animate(a, pos=newCoord, tween='accel_decel', duration=.7)

####### pygame zero update loop ####### 
#def update(): 
#  root.update() #keeps TkInter alive
#root.mainloop()

view = Gui.ActiveDocument.ActiveView
sg = view.getSceneGraph()

root = coin.SoSeparator()
sg.addChild(root)

t1 = coin.SoTranslation()
c1 = coin.SoCube()

root.addChild(t1)
root.addChild(c1)

#idlecallback to drive animation updates

### end ###
