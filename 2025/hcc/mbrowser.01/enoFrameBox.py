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
  verbose         = False
  shiftMultiplier = 10

  borderCol = (255, 255, 255, 80)
  pos, dim  = (900, 900), (100, 100)
  lastPos, lastDim = None, None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# keyMod #############
  
  def keymod(self, keymod):
    try:
      result = []
      if keymod == 0:       return result
      if keymod & 1   > 0:  result.append("shf")
      if keymod & 256  > 0: result.append("alt")
      if keymod & 1024 > 0: result.append("sup") #"win," "cmd," "meta," ...
      return result
    except: return []

  ############# draw #############

  def nudge(self, dx, dy, mods):
    try:
      if self.verbose: 
        msgStr = "%i,%i,%s" % (x,y,str(mods))
        self.msg(msgStr)

      sm = self.shiftMultiplier

      if 'shf' in mods: dx *= sm; dy *= sm
      x, y = pos
      w, h = dim
      if 'alt' not in mods: x += dx; y += dy
      else                : w += dx; h += dy
      pos, dim = (x, y), (w, h)

    except: self.err("nudge")

  ############# draw #############

  def draw(self, screen):
    try:
      r = Rect(self.pos, self.dim)
      screen.draw.rect(r, self.borderCol)
    except: self.err("draw")

  ############# on_key_down #############

  def on_key_down(self, key, mod): 
    try:
      km = self.keymod(mod)

      if   key==keys.LEFT : self.nudge(-1, 0, km) #match/case not present on micropython, etc.
      elif key==keys.RIGHT: self.nudge( 1, 0, km)
      elif key==keys.UP:    self.nudge( 0, 1, km)
      elif key==keys.DOWN:  self.nudge( 0,-1, km)
    except: self.err("on_key_down")

### end ###
