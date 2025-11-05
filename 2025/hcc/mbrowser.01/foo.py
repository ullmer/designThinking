# Enodia prism ensemble
# Brygg Ullmer, Clemson University
# Begun 2025-11-05

import math
import pygame
import pygame.gfxdraw

from ataBase      import *
from enoPrismBar  import *
from enoPrismBars import *

class EnoPrismEnsemble(AtaBase):
  basePos   = (0, 0)
  pathWidth = 500
  baseWidth = None
  pathMaxDx = 800
  pathMaxDy = 850

  fontSize    = 30
  barsList    = None
  flowLeft    = True
  textOffset2 = (0,0)

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# draw #############

  def draw(self, screen):
    if self.barList is None:
      if self.verbose: self.msg("draw called with empty barlist"); return

    for b in self.barList: b.draw(screen)

### end ###
