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

cubeActor[0] Actor(pos=winCoord, image=None)

####### shift cube ####### 

def winShift(winId):
  global winState, winActors, winCoords, winCoordsBase, winShift 

  prevWinState    = winState[winId]

  if winId == "w1": dx = winShift
  else:             dx = -1 * winShift

  if prevWinState == 1: winState[winId] = 0
  else:                 winState[winId] = 1; dx *= -1

  x, y             = winCoords[winId]
  newCoord         = (x+dx, y)
  winCoords[winId] = newCoord
  a                = winActors[winId]

  animate(a, pos=newCoord, tween='accel_decel', duration=.7)

####### pygame zero update loop ####### 

def update(): 
  root.update() #keeps TkInter alive

#root.mainloop()

####### main ####### 

w1b = tk.Button(root, text="w1 shift", command=partial(winShift, "w1"))
w2b = tk.Button(root, text="w2 shift", command=partial(winShift, "w2"))

b1 = tk.Button(root, text='quit', command=quitCb)
b1.pack()

constructWindowAnimators()

w1Geom = genWinGeom("w1")
w2Geom = genWinGeom("w2")

w1 = tk.Toplevel(); w1.geometry(w1Geom)
w2 = tk.Toplevel(); w2.geometry(w2Geom)


### end ###
