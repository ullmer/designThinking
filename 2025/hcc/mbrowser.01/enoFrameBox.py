# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import pygame
import pygame.gfxdraw

from ataBase      import *
from enoPrismBar  import *
from enoPrismBars import *
from enoParseGrid import *

class EnoFrameBox(AtaBase):
  borderCol = (255, 255, 255, 80)
  pos, dim  = (900, 900), (100, 100)

  lastPos, lastDim = None, None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# draw #############

  def draw(self, screen):
    try:
      for pb in self.prismBars: pb.draw(screen)
    except: self.err("draw")

  r = Rect((900, 900), (300, 100))
  screen.draw.rect(r, borderCol)

### end ###
