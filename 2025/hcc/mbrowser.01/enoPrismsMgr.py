# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

from enoPrismBar   import *
from enoPrismBars  import *
from enoPrismActor import *
from enoActor     import *

class enoPrismsMgr(AtaBase):

  cblu = (0,   0, 255, 80)
  cyel = (255, 255, 0, 70)
  cgre = (0,   255, 0, 70)
  cred = (255,   0, 0, 70)

  prismBarSources = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.init()

  ############# initiate #############

  def init(self):
    b1 = EnoActor("teiland04",      bottomleft=(0,  1190))
    b2 = EnoActor("teiblockconf04", bottomleft=(910,1190))
    sc = .45
    b1.scaleV(sc)
    b2.scaleV(sc)
    self.prismBarSources = [b1, b2]

initialized = False
n,w=35,400
epb1 = EnoPrismBars(flowLeft=False, textOffset2=(-18,0), fontSize=25, pathMaxDx=900)
epb1.addBar("22: Daejeon",  cyel, n)
epb1.addBar("23: Warsaw",   cblu, n)
epb1.addBar("24: Cork",     cblu, w)
epb1.addBar("25: Bordeaux", cblu, n)
epb1.addBar("26: Chicago",  cred, n)

epb1b = EnoPrismBars(flowLeft=False, pathMaxDx=140, pathMaxDy=80, baseWidth=78, basePos=(900, 850))
#epb1b = EnoPrismBars(flowLeft=False, pathMaxDx=140, pathMaxDy=75, basePos=(900, 850))
epb1b.addBar("", cyel, n)
#epb1b.addBar("", cblu, n)
#epb1b.addBar("", cblu, w)
#epb1b.addBar("", cblu, n)
#epb1b.addBar("", cred, n)

n2=88
epb2 = EnoPrismBars(flowLeft=True, textOffset2=(705, 0), fontSize=25)
epb2.addBar("creativity",    cgre, n2)
epb2.addBar("dance+theater", cgre, n2)
epb2.addBar("music+sound",   cgre, n2)
epb2.addBar("actuation",     cyel, n2)
epb2.addBar("AI",            cyel, n2)
epb2.addBar("computing hardware", cyel, n2)

epb2b = EnoPrismBars(flowLeft=True, textOffset2=(705, 0), pathMaxDy=80, pathMaxDx=0,
                     fontSize=25, basePos=(0, 850)) #, baseWidth=80)
                     #baseWidth=20, fontSize=25, basePos=(50, 850))
epb2b.addBar("", cgre, n2)


refractBar = pygame.Surface((WIDTH, 75), pygame.SRCALPHAg
gcolor = (255, 255, 255, 75)
refractBar.fill(rcolor)


def update():
  global initialized
  if not initialized: setup(); initialized=True

epb = [epb1, epb1b, epb2, epb2b]

def draw(): 
  screen.clear()
  for p in epb: p.draw(screen)
  for b in bs:  b.draw(screen)
  screen.blit(refractBar, (0, 800))

pgzrun.go()

g## end ###
