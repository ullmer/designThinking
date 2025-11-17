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

  activateIntersects = True
  epi          = None

  drawPrismBarSelIntersection   = True

  currentPrismIntersectBars     = None
  currentPrismIntersectVertices = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.prisms       = []
    self.domainPrisms = []

    ept = EnoPrismsTei() #clearly needs further abstraction; a bridge 
    self.domainPrisms.append(ept)

    if self.activateIntersects: self.epi = EnoPrismIntersects()

  ############# summon prism #############

  def intersectPrismBarPair(self, idx1, idx2, bar1idx, bar2idx):
    try:
      if self.epi is None: self.msg("intersectPrismBarPair: epi backend not initiated")
      prism1, prism2 = self.prisms[idx1], self.prisms[idx2]
      bar1, bar2     = prism1.getPrismBar(0), prism2.getPrismBar(0)  # "upper portions"
      verts1, verts2 = bar1.barList[bar1idx].vertices, bar2.barList[bar2idx].vertices

      if verts1 is None or verts2 is None: self.msg("intersectPrismBarPair: bar vertices undefined"); return

      b1Len = len(bar1.barList)
      b2Len = len(bar2.barList)

      self.msg("ipbp: " + str(verts1) + str(verts2))

      #intersect = self.epi.intersectQuadPolysI(verts1, verts2)
      #self.msg("intersect: " + str(intersect))

      for i in range(b1Len):
        for j in range(b2Len):
          verts1, verts2 = bar1.barList[i].vertices, bar2.barList[j].vertices
          intersect = self.epi.intersectQuadPolysI(verts1, verts2)
          self.msg(str([i,j]) + str(intersect))

      intersect = self.epi.intersectQuadPolysI(verts1, verts2)
      self.msg("intersect: " + str(intersect))
    except: self.err("intersectPrismBarPair")

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
