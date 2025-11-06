# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enoPrismBar  import *
from enoPrismBars import *
from enoActor     import *

class PrismsTei(AtaBase):

  cblu = (0,   0, 255, 75); cyel = (255, 255, 0, 70); cgre = (0,   255, 0, 70)
  cgr2 = (0,   255, 0, 20); cred = (255,   0, 0, 70)
  bars = None

  initialized  = None
  activePrisms = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.activePrisms = []
    self.initialized  = False

  ################### get prism ###################

  def summonPrism(self, whichPrism, whichSlot):
    if whichPrism == "teiLandscape" and whichSlot == 0: 
      p = self.getPrismTeiLandscapeL(); self.activePrisms.append(p); return p

    if whichPrism == "teiYearsQ4"   and whichSlot == 1: 
      p = self.getPrismTeiYearsQ4(); self.activePrisms.append(p); return p

  ################### get prism tei landscape left  ###################

  def getPrismTeiLandscapeL(self):
    try:
      n,w=35,400
      epb1a = EnoPrismBars(flowLeft=False, textOffset2=(-18,0), fontSize=25, pathMaxDx=700, basePos=(200,0))
      epb1b = EnoPrismBars(flowLeft=False, pathMaxDx=140, pathMaxDy=80, baseWidth=79, basePos=(900, 850), refractBars=True)

      bindings1 = [["22: Daejeon",  cyel, n], ["23: Warsaw",  cblu, n], ["24: Cork", cblu, w],
                   ["25: Bordeaux", cblu, n], ["26: Chicago", cred, n]]

      for b in bindings1: epb1a.addBarL(b)
      for b in bindings1: epb1b.addBarL2(b)
      return [epb1a, epb1b]
    except: self.err("getPrismTeiLandscapeL")

  ################### get prism tei years q4 ###################

  def getPrismTeiYearsQ4(self):
    try:
      n2=88
      epb2a = EnoPrismBars(flowLeft=True, textOffset2=(930, 0), fontSize=40, pathMaxDx=1000)
      epb2b = EnoPrismBars(flowLeft=True, textOffset2=(705, 0), pathMaxDy=80, pathMaxDx=-100,
                           fontSize=25, basePos=(100, 850), baseWidth=105, refractBars=True)

      bindings2a = [["creativity", cgre, n2], ["dance+theater",          cgre, n2], ["music+sound",        cgre, n2],
                    ["actuation",  cyel, n2], ["artificial intelligence", cyel, n2], ["computing hardware", cyel, n2]]

      for b in bindings2a: epb2a.addBarL(b)

      bindings2b = [["creativity", cgr2, n2], ["dance+theater",          cgr2, n2], ["music+sound",        cgr2, n2],
                    ["actuation",  cyel, n2], ["artificial intelligence", cyel, n2], ["computing hardware", cyel, n2]]

      for b in bindings2b[0:3]: epb2b.addBarL3(b,65)
      epb2b.baseWidth  =  97
      epb2b.baseShiftX = -260
      for b in bindings2b[3:]: epb2b.addBarL2(b)
      return [epb2a, epb2b]
   except: self.err("getPrismTeiYearsQ4)

  ################### initiate ###################

  def init(self):
    try:
      b1 = EnoActor("teiland04",      bottomleft=(0,  1190), name='teiLandscape')
      b2 = EnoActor("teiblockconf04", bottomleft=(910,1190), name='teiConfsQ04')
      sc = .45
      b1.scaleV(sc); b2.scaleV(sc)
      self.bars = [b1, b2]
    except: self.err("init")

  ################### update ###################

  def update(self):
    if not self.initialized: self.setup(); self.initialized=True

  ################### draw ###################

  def draw(self):
    if self.activePrisms is None: return
    try:
      for prism in self.activePrisms:
        for ppath in prism: ppath.draw()
    except: self.err("draw")

### end ###
