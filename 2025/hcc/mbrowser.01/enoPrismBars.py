# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import math
import pygame
import pygame.gfxdraw

from ataBase     import *
from enoPrismBar import *

class EnoPrismBars(AtaBase):
  basePos   = (50, 0)
  cumPos    = None
  pathWidth = 500
  pathMaxDx = 800
  pathMaxDy = 950

  barList     = None
  flowLeft    = True
  textOffset2 = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# addBar #############

  def addBar(self, barText, barColor, barWidth): 
    if self.barList is None: 
      self.barList = []
      self.cumPos  = self.basePos

    fl     = self.flowLeft
    to2    = self.textOffset2
    epb    = EnoPrismBar(textStrs=barText, barColor=barColor, barWidth=barWidth, 
                         basePos=cumPos, flowLeft=fl, textOffset2=to2)
    cx, cy = cumPos
    cx    += barWidth
    cumPos = (cx, cy)

  ############# draw #############

  def draw(self, screen):
    if self.barList is None:
      if self.verbose: self.msg("draw called with empty barlist"); return

    for b in self.barList: b.draw()

### end ###
