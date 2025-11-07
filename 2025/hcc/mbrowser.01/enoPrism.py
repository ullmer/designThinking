# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import math
import pygame
import pygame.gfxdraw

from ataBase      import *
from enoPrismBar  import *
from enoPrismBars import *
from enoParseGrid import *

class EnoPrism(AtaBase):
  prismName  = None
  prismBars  = None
  parseTouch = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    if self.prismBars is None: self.prismBars = []

  ############# add prism bar #############

  def addPrismBar(self, prismBar):
    try:    self.prismBars.append(prismBar)
    except: self.err("addPrismBar")

  ############# add prism bar #############

  def addPrismBars(self, prismBars):
    try:    
      for pb in prismBars: self.prismBars.append(pb)
    except: self.err("addPrismBars")

  ############# create draw #############

  def draw(self, screen):
    try:
      for pb in self.prismBars: pb.draw(screen)
    except: self.err("draw")

### end ###
