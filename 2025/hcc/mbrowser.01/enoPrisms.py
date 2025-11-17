# Enodia "prism"
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *
from enoPrismIntersects import *

class EnoPrisms(AtaBase):
  prisms       = None
  domainPrisms = None

  currentPrismIntersectBars     = None
  currentPrismIntersectVertices = None

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
        if p is not None: 
          self.prisms.append(p)
          return p
        else: self.msg("summonPrism requested but not found: " + 
                        str(prismName) + " " + str(prismLoc))

    except: self.err("summonPrism")

  ############# add prism #############

  def addPrism(self, prism):
    self.prisms.append(prism)

  ############# update #############
  
  def update(self): 
    try:    
      for dp in self.domainPrisms: dp.update()
    except: self.err("self.ept.update")

  ############# draw #############

  def draw(self, screen):
    try: 
      for  p in self.prisms: p.draw(screen)
      for dp in self.domainPrisms: dp.draw(screen)

    except: self.err("draw")

  ############# parse locus #############

  def parseLocus(self, pos):
    try: 
      for  p in self.prisms: p.parseLocus(pos)
    except: self.err("parseLocus")

### end ###
