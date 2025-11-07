# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import pygame

from pgzero.constants import * #e.g., keys

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

  ############# keyMod #############
  
  def keymod(self, keymod):
    try:
      if keymod == 0:    return None
      if keymod == 1:    return "shf"
      if keymod == 256:  return "alt"
      if keymod == 1024: return "win"
      return None
    except: return None

  ############# draw #############

  def draw(self, screen):
    try:
      r = Rect(self.pos, self.dim)
      screen.draw.rect(r, self.borderCol)
    except: self.err("draw")

  def on_key_down(self, key, mod): 
    try:
      km = self.keymod(mod)

      if   key==keys.LEFT : print("left", km)
      elif key==keys.RIGHT: print("right", km)
    except: self.err("on_key_down")

### end ###
