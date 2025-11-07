# Enodia "refraction" bar
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

############# refract bar #############

class EnoRefractBar(AtaBase):
  dimensions = None
  position   = None
  surf       = None
  fillColor  = (255, 255, 255, 45)

  ############# constructor #############

  def __init__(self, dim, pos, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.dimensions = dim
    self.position   = pos
    self.createSurface()

  ############# create surface #############

  def createSurface(self):
    try:
      self.surf = pygame.Surface(self.dimensions, pygame.SRCALPHA)
      self.surf.fill(self.fillColor)
    except: self.err("createSurface")

  ############# draw #############

  def draw(self, screen):
    try:
      screen.blit(self.surf, self.position)
    except: self.err("draw")


### end ###
