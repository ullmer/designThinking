# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pgzrun
from pgzero.builtins import Actor, animate, keyboard, keys

WIDTH, HEIGHT=1600,1080

from enoPrismBar  import *
from enoPrismBars import *
from enoActor     import *

##### main ##### 

cblu = (0,   0, 255, 75)
cyel = (255, 255, 0, 70)
cgre = (0,   255, 0, 70)
cgr2 = (0,   255, 0, 30)
cred = (255,   0, 0, 70)

n,w=35,400
epb1 = EnoPrismBars(flowLeft=False, textOffset2=(-18,0), fontSize=25, pathMaxDx=700,
                    basePos=(200,0))
epb1.addBar("22: Daejeon",  cyel, n)
epb1.addBar("23: Warsaw",   cblu, n)
epb1.addBar("24: Cork",     cblu, w)
epb1.addBar("25: Bordeaux", cblu, n)
epb1.addBar("26: Chicago",  cred, n)

epb1b = EnoPrismBars(flowLeft=False, pathMaxDx=140, pathMaxDy=80, baseWidth=79, basePos=(900, 850), refractBars=True)
epb1b.addBar("", cyel, n)
epb1b.addBar("", cblu, n)
epb1b.addBar("", cblu, w)
epb1b.addBar("", cblu, n)
epb1b.addBar("", cred, n)

n2=88
epb2 = EnoPrismBars(flowLeft=True, textOffset2=(930, 0), fontSize=40, pathMaxDx=1000)
epb2.addBar("creativity",    cgre, n2)
epb2.addBar("dance+theater", cgre, n2)
epb2.addBar("music+sound",   cgre, n2)
epb2.addBar("actuation",     cyel, n2)
epb2.addBar("artificial intelligence", cyel, n2)
epb2.addBar("computing hardware", cyel, n2)

epb2b = EnoPrismBars(flowLeft=True, textOffset2=(705, 0), pathMaxDy=80, pathMaxDx=-50,
                     fontSize=25, basePos=(50, 850), baseWidth=67, refractBars=True)

epb2b.baseWidth  =  96
#epb2b.baseShiftX = 50
epb2b.addBar("", cgr2, n2, 65)
epb2b.addBar("", cgr2, n2, 65)
epb2b.addBar("", cgr2, n2, 65)

epb2b.baseWidth  =  96
epb2b.baseShiftX = -155
epb2b.addBar("", cyel, n2)
epb2b.addBar("", cyel, n2)
epb2b.addBar("", cyel, n2)


def setup():
  global bs
  b1 = EnoActor("teiland04",      bottomleft=(0,  1190))
  b2 = EnoActor("teiblockconf04", bottomleft=(910,1190))
  sc = .45
  b1.scaleV(sc)
  b2.scaleV(sc)
  bs = [b1, b2]

initialized = False

def update():
  global initialized
  if not initialized: setup(); initialized=True

epb = [epb1, epb1b, epb2, epb2b]

refractBar = pygame.Surface((WIDTH, 80), pygame.SRCALPHA)
rcolor = (255, 255, 255, 45)
refractBar.fill(rcolor)

def draw(): 
  screen.clear()
  for b in bs:  b.draw(screen)
  for p in epb: p.draw(screen)
  screen.blit(refractBar, (0, 850))
  screen.draw.text("TEI", midleft=(300,70), alpha=.2, color=rcolor, fontname="barlow_black", fontsize=250)

pgzrun.go()

### end ###
