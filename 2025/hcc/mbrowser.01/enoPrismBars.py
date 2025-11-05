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

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# addBar #############

  def addBar(self, barText, barColor, barWidth): 
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
    epb    = EnoPrismBar(textStrs=barText,     barColor=barColor, barWidth=barWidth, 
                         basePos =self.cumPosTop, flowLeft=fl,    textOffset2=to2, 
                         pathMaxDx=self.pathMaxDx, pathMaxDy=self.pathMaxDy, fontSize=fs,
                         baseWidth=self.baseWidth, baseShiftX=self.baseShiftX)

    cx1             += barWidth
    self.baseShiftX += (bottomWidth-barWidth)
    self.cumPosTop   = (cx1, cy1)
    
    self.barList.append(epb)

  ############# draw #############

  def draw(self, screen):
    if self.barList is None:
      if self.verbose: self.msg("draw called with empty barlist"); return

    for b in self.barList: b.draw(screen)

### end ###

