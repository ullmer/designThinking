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
  prismName = None
  prismBars = None
  parseGrid = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    if self.prismBars is None: self.prismBars = []

  ############# number prism bars #############

  def numPrismBars(self):
    try:
      if self.prismBars is None: return 0
      return len(self.prismBars)
    except: self.err("numPrismBars")

  ############# get prism bar #############

  def getPrismBar(self, whichBar: int):
    try:
      if self.prismBars is None: return None
      return self.prismBars[whichBar]
    except: self.err("getPrismBars")

  ############# add prism bar #############

  def addPrismBar(self, prismBar):
    try:    self.prismBars.append(prismBar)
    except: self.err("addPrismBar")

  ############# add prism bar #############

  def addPrismBars(self, prismBars):
    try:    
      for pb in prismBars: self.prismBars.append(pb)
    except: self.err("addPrismBars")

  ############# draw #############

  def draw(self, screen):
    try:
      for pb in self.prismBars: pb.draw(screen)
    except: self.err("draw")

  ############# parse locus #############

  def parseLocus(self, pos):
    try:
      if self.parseGrid is None: self.msg("parseLocus: parseGrid not present"); return
      self.parseGrid.parseLocus(pos)
    except: self.err("parseLocus")

### end ###
