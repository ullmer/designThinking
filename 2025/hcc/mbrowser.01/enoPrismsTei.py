# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

from enoActor     import *
from enoPrism     import *
from enoPrismBar  import *
from enoPrismBars import *
from enoParseGrid import *

class EnoPrismsTei(AtaBase):

  #pathMaxDy = 850
  pathMaxDy = 750
  barYShift = pathMaxDy + 340
  cblu = (0,   0, 255, 75); cyel = (255, 255, 0, 70); cgre = (0,   255, 0, 70)
  cgr2 = (0,   255, 0, 20); cred = (255,   0, 0, 70)
  bars = None

  initialized       = None
  #activePrisms      = None
  bars              = None
  parseTouchByPrism = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.activePrisms      = []
    self.bars              = []
    self.parseTouchByPrism = {}
    self.initialized       = False

  ################### get prism ###################

  def summonPrism(self, whichPrism, whichSlot):
    try:
      if whichPrism == "teiLandscape" and whichSlot == 0: 
        p = self.summonPrismTeiLandscapeL(); self.activePrisms.append(p); return p

      if whichPrism == "teiYearsQ4"   and whichSlot == 1: 
        p = self.summonPrismTeiYearsQ4();    self.activePrisms.append(p); return p

      return None
    except: self.err("summonPrism")

  ################### get prism tei landscape left  ###################

  def summonPrismTeiLandscapeL(self):
    try:
      n,w,pmdy=35,400, self.pathMaxDy
      cyel, cblu, cred = self.cyel, self.cblu, self.cred
      epb1a = EnoPrismBars(flowLeft=False, textOffset2=(-18,0), fontSize=25, pathMaxDy=pmdy, pathMaxDx=700, basePos=(200,0))
      epb1b = EnoPrismBars(flowLeft=False, pathMaxDx=140, pathMaxDy=80, baseWidth=79, basePos=(900, pmdy), refractBars=True)

      bindings1 = [["22: Daejeon",  cyel, n], ["23: Warsaw",  cblu, n], ["24: Cork", cblu, w],
                   ["25: Bordeaux", cblu, n], ["26: Chicago", cred, n]]

      for b in bindings1: epb1a.addBarL(b)
      for b in bindings1: epb1b.addBarL2(b)
      pb = [epb1a, epb1b]

      epg = EnoParseGrid(rows=2, cols=4, x0=-10, y0=831, pixDim=(413, 116))
      cats1='tools,actuation,AI,computing hardware,art,creativity,dance&theater,music&sound'
      cats2=cats1.split(',')
      epg.setGridBindings(cats2)
      #epg.printGridBindings()

      ep = EnoPrism(prismBars = pb, prismName = "teiLandscape", parseGrid=epg)

      return ep

    except: self.err("summonPrismTeiLandscapeL")

  ################### get prism tei years q4 ###################

  def summonPrismTeiYearsQ4(self):
    try:
      n2,pmdy=88, self.pathMaxDy
      cgre, cyel, cgr2 = self.cgre, self.cyel, self.cgr2
      epb2a = EnoPrismBars(flowLeft=True, textOffset2=(930, 0), fontSize=40, pathMaxDy=pmdy, pathMaxDx=1000)
      epb2b = EnoPrismBars(flowLeft=True, textOffset2=(705, 0), pathMaxDy=80, pathMaxDx=-100,
                           fontSize=25, basePos=(100, pmdy), baseWidth=105, refractBars=True)

      bindings2a = [["creativity", cgre, n2], ["dance+theater",          cgre, n2], ["music+sound",        cgre, n2],
                    ["actuation",  cyel, n2], ["artificial intelligence", cyel, n2], ["computing hardware", cyel, n2]]

      for b in bindings2a: epb2a.addBarL(b)

      bindings2b = [["creativity", cgr2, n2], ["dance+theater",          cgr2, n2], ["music+sound",        cgr2, n2],
                    ["actuation",  cyel, n2], ["artificial intelligence", cyel, n2], ["computing hardware", cyel, n2]]

      for b in bindings2b[0:3]: epb2b.addBarL3(b,65)
      epb2b.baseWidth  =  97
      epb2b.baseShiftX = -260
      for b in bindings2b[3:]: epb2b.addBarL2(b)
      pb = [epb2a, epb2b]
      epg = EnoParseGrid(cols=5, rows=1, x0=1040, y0=831, pixDim=(398, 116))
      epg.setGridBindings(["tei22", "tei23", "tei24", "tei25", "tei26"])

      ep  = EnoPrism(prismBars = pb, prismName = "teiYearsQ4", parseGrid=epg)

      return ep

    except: self.err("summonPrismTeiYearsQ4")

  ################### initiate ###################

  def setup(self):
    try:
      bys = self.barYShift
      b1 = EnoActor("teiland04",      bottomleft=(0,  bys), name='teiLandscape')
      b2 = EnoActor("teiblockconf04", bottomleft=(910,bys), name='teiConfsQ04')
      sc = .45
      b1.scaleV(sc); b2.scaleV(sc)
      self.bars = [b1, b2]
    except: self.err("init")

  ################### update ###################

  def update(self):
    if not self.initialized: self.setup(); self.initialized=True

  ################### draw ###################

  def draw(self, screen):
    if self.activePrisms is None: return
    try:
      for bar   in self.bars: bar.draw(screen)
      #for prism in self.activePrisms:
      #  for ppath in prism: 
      #    if ppath is not None: ppath.draw(screen)

    except: self.err("draw")

### end ###
