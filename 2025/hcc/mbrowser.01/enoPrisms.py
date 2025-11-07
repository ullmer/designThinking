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
        if p is not None: 
          self.prisms.append(p)
          return p
        else: self.msg("summonPrism requested but not found: " + 
                        str(prismName) + " " + str(prismLoc))

    except: self.err("summonPrism")

  ############# add prism #############

  def addPrism(self, prism):
    self.prisms.append(prism)

  ############# draw #############
  
  def update(self): 
    try:    
      for dp in self.domainPrisms: dp.update()
    except: self.err("self.ept.update")

  def draw(self, screen):
    try: 
      for  p in self.prisms: p.draw(screen)
      for dp in self.domainPrisms: dp.draw(screen)

    except: self.err("draw")

############# refract bar #############

class RefractBar(AtaBase):
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
