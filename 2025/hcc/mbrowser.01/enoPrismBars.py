# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import math
import pygame
import pygame.gfxdraw

from ataBase     import *
from enoPrismBar import *

class EnoPrismBars(AtaBase):
  basePos    = (0, 0)
  cumPosTop  = None
  baseShiftX = 0
  pathWidth  = 500
  baseWidth  = None
  pathMaxDx  = 800
  pathMaxDy  = 850

  fontSize    = 30
  barList     = None
  flowLeft    = True
  textOffset2 = (0,0)
  refractBars = False

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# add bar list #############

  def addBarL(self, barList):
    try:
      bl = len(barList)
      if   bl==3: bt, bc, bw      = barList; self.addBar(bt,bc,bw)
      elif bl==4: bt, bc, bw, eby = barList; self.addBar(bt,bc,bw,eby)
      else: self.msg("addBarL: non-matching parameters"); return None
    except: self.err("addBarL")

  ############# add bar list #############

  def addBarL2(self, barList):
    try:
      bl = len(barList)
      if   bl==3: bt, bc, bw      = barList; self.addBar("",bc,bw)
      elif bl==4: bt, bc, bw, eby = barList; self.addBar("",bc,bw,eby)
      else: self.msg("addBarL: non-matching parameters"); return None
    except: self.err("addBarL")

  ############# addBar #############

  def addBar(self, barText, barColor, barWidth, extendBottomY=0): 
    if self.barList is None: 
      self.barList = []
      self.cumPosTop = self.basePos
      self.cumPosBot = 0

    bottomWidth = barWidth
    if self.baseWidth is not None: bottomWidth = self.baseWidth

    fl       = self.flowLeft
    fs       = self.fontSize
    to2      = self.textOffset2
    cx1, cy1 = self.cumPosTop
    epb      = EnoPrismBar(textStrs=barText,     barColor=barColor, barWidth=barWidth, 
                         basePos =self.cumPosTop, flowLeft=fl,    textOffset2=to2, 
                         pathMaxDx=self.pathMaxDx, pathMaxDy=self.pathMaxDy+extendBottomY, fontSize=fs,
                         baseWidth=self.baseWidth, baseShiftX=self.baseShiftX, refractBar = self.refractBars)
  
    #if self.refractBars and fl: cx1 += barWidth/2
    #else:                       cx1 += barWidth

    cx1 += barWidth
    if fl: self.baseShiftX += (bottomWidth-barWidth)
    else:  self.baseShiftX += (bottomWidth-barWidth)
    self.cumPosTop   = (cx1, cy1)
    
    self.barList.append(epb)

  ############# draw #############

  def draw(self, screen):
    if self.barList is None:
      if self.verbose: self.msg("draw called with empty barlist"); return

    for b in self.barList: b.draw(screen)

### end ###

