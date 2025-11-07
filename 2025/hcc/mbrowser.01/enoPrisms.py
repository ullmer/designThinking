# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

class EnoPrisms(AtaBase):
  prisms = None
  domainPrisms = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prisms       = []
    self.domainPrisms = []

    ept = EnoPrismsTei() #clearly needs further abstraction; a bridge 
    self.domainPrisms.append(ept)

  ############# summon prism #############

  def summonPrism(self, prismName, prismLoc):
    try:
      for dp in self.domainPrisms:
        p = dp.summonPrism(prismName, prismLoc)
        if p is not None: return p

    except: self.err("summonPrism")

  ############# add prism #############

  def addPrism(self, prism):
    self.prisms.append(prism)

  ############# draw #############
  
  def update(self): 
    try:    self.ept.update()
    except: self.err("self.ept.update")

  def draw(self, screen):
    try: 
      for p in self.prisms: p.draw(screen)
    except: self.err("draw")

### end ###
