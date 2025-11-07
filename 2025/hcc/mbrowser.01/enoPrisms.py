# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

class EnoPrisms(AtaBase):
  prisms = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prisms = []

  ############# add prism #############

  def addPrism(self, prism):
    self.prisms.append(prism)

  ############# draw #############

  def draw(self, screen):
    try: 
      for p in self.prisms: p.draw(screen)
    except: self.err("draw")

### end ###
