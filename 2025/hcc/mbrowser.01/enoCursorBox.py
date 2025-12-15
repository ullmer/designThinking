# Enodia cursor box
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import pygame

from enoFrameBox import *

class EnoCursorBox(EnoFrameBox):
  verbose         = False
  shiftMultiplier = 10

  borderCol = (255, 255, 0, 70)
  width     = 2
  pos, dim  = (2, 2), (10, 10)
  duration  = .15
  tween     = 'accel_decel'

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()

### end ###
