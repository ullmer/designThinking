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

  barList      = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# addBar #############

  def addBar(self, barText, barColor, barWidth): 
    if self.barList is None: 
      self.barList = []
      self.cumPos  = self.basePos

    epb = EnoPrismBar(textStrs=barText

  ############# draw #############

  def draw(self, screen):
    for surf in self.surfaceList:
      screen.blit(surf, self.basePos)

    if self.drawText: self.drawTexts()

### end ###
