# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import tkinter as tk
import pygame  as pg
import sys
from   functools       import partial
from   pgzero.builtins import Actor, animate, keyboard

WIDTH  = 100
HEIGHT = 100

winDim        = '400x400'
#winController = '300x50-0-0'

root = tk.Tk()
root.title('example controller')
#root.geometry(winController)

####### support functions ####### 

def quitCb(): 
  print("contemplating quitting")
  pg.quit()
  sys.exit()

####### generate window geometry ####### 

def genWinGeom(winId): 
  global winDim, winCoords

  x, y   = winCoords[winId]
  result = "%s+%i+%i" % (winDim, x, y)

  return result

####### construct window animation state ####### 

def constructWindowAnimators():
  global winState, winActors, winCoords, winCoordsBase, winShift 

  winState     = {}
  winActors    = {} #using PyGame Zero Actor animation mechanism to tween-animate Tkinter windows
  winCoords    = {}
  winCoordsBase = {}

  winCoordsBase["w1"] = (0,   0)
  winCoordsBase["w2"] = (800, 0)
  winShift           = 200

  for winId in ["w1", "w2"]:
    winState[winId]  = 1
    winCoord         = winCoordsBase[winId]
    winCoords[winId] = winCoord
    winActors[winId] = Actor(pos=winCoord, image="single_pix")

####### shift windows ####### 

def winShift(winId):
  global winState, winActors, winCoords, winCoordsBase, winShift 
  print("shifting window", winId)

  prevWinState    = winState[winId]

  if winId == "w1": dx = winShift
  else:             dx = -1 * winShift

  if prevWinState == 1: winState[winId] = 0
  else:                 winState[winId] = 1; dx *= -1

  x, y             = winCoords[winId]
  newCoord         = (x+dx, y)
  winCoords[winId] = newCoord
  a                = winActors[winId]

  animate(a, pos=newCoord, tween='accel_decel', duration=0.7)

####### pygame zero update loop ####### 

def draw():   root.update() #keeps TkInter alive
def update(): root.update() #keeps TkInter alive

#root.mainloop()

####### main ####### 

w1b = tk.Button(root, text="w1 shift", command=partial(winShift, "w1"))
w2b = tk.Button(root, text="w2 shift", command=partial(winShift, "w2"))

b1 = tk.Button(root, text='quit', command=quitCb)

for widget in [w1b, w2b, b1]:
  widget.pack(side='left')

constructWindowAnimators()

w1Geom = genWinGeom("w1")
w2Geom = genWinGeom("w2")

w1 = tk.Toplevel(); w1.geometry(w1Geom)
w2 = tk.Toplevel(); w2.geometry(w2Geom)

### end ###
