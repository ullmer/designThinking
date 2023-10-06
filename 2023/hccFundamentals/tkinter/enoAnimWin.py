# PyGame Zero-animated Tkinter windows
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import tkinter as tk
import pygame  as pg
import sys
from   functools       import partial
from   pgzero.builtins import Actor, animate, keyboard

#######################################################
##################### enoAnimWindow ################### 

class enoAnimWindow:

  winDim        = '400x400'
  winCoords     = None
  winActors     = None
  winState      = None
  winCoordsBase = None
  winShift      = 200
  tween         = 'accel_decel'
  duration      = 0.7

  ####### support functions ####### 

  def quitCb(self): 
    print("contemplating quitting")
    pg.quit()
    sys.exit()

  ####### generate window geometry ####### 
  
  def genWinGeom(self, winId): 

    x, y   = self.winActors[winId].pos
    result = "%s+%i+%i" % (self.winDim, x, y)

    return result

  ####### construct window animation state ####### 

  def constructWindowAnimators(self):

    self.winState      = {}
    self.winActors     = {} #using PyGame Zero Actor animation mechanism to tween-animate Tkinter windows
    self.winCoords     = {}
    self.winCoordsBase = {}

    self.winCoordsBase["w1"] = (0,   0)
    self.winCoordsBase["w2"] = (800, 0)

    for winId in ["w1", "w2"]:
      self.winState[winId]  = 1
      self.winCoord         = winCoordsBase[winId]
      self.winCoords[winId] = winCoord
      self.winActors[winId] = Actor(pos=winCoord, image="single_pix")

  ####### shift windows ####### 

  def winShift(self, winId):
    #print("shifting window", winId)

    prevWinState    = self.winState[winId]

    if winId == "w1": dx = self.winShift
    else:             dx = self.winShift * -1

    if prevWinState == 1: self.winState[winId] = 0
    else:                 self.winState[winId] = 1; dx *= -1

    x, y             = self.winCoords[winId]
    newCoord         = (x+dx, y)
    self.winCoords[winId] = newCoord
    a                = self.winActors[winId]
    #print(str((x,y)), str(newCoord))

    animate(a, pos=newCoord, tween=self.tween, duration=self.duration)

  ####### pygame zero update loop ####### 

  def update(): 
    global w1, w2
    w1Geom = genWinGeom("w1")
    w2Geom = genWinGeom("w2")
    w1.geometry(w1Geom)
    w2.geometry(w2Geom)
    root.update() #keeps TkInter alive

### end ###
