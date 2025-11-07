# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import math
import pygame
import pygame.gfxdraw

from ataBase       import *
from enoPrismBar   import *
from enoPrismBars  import *
from enoParseTouch import *

class EnoPrism(AtaBase):
  prismName  = None
  prismBars  = None
  parseTouch = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# create draw #############

  def draw(self, screen):
    try:
    except: self.err("draw")

### end ###
