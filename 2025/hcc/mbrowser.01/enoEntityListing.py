# Enodia entity listing
# Brygg Ullmer, Clemson University
# Begun 2025-11-12

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

class EnoEntityListing(AtaBase):
  prisms = None
  domainPrisms = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prisms       = []
    self.domainPrisms = []

    ept = EnoPrismsTei() #clearly needs further abstraction; a bridge 
    self.domainPrisms.append(ept)

  ############# draw #############

  def draw(self, screen):
    try: 
      for  p in self.prisms: p.draw(screen)
      for dp in self.domainPrisms: dp.draw(screen)

    except: self.err("draw")

### end ###
