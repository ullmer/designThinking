# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pgzrun
from pgzero.builtins import Actor, animate, keyboard, keys

WIDTH, HEIGHT=1900,1080

from enoPrismBar  import *
from enoPrismBars import *

initialized = False

##### main ##### 

cblu = (0,   0, 255, 80)
cyel = (255, 255, 0, 70)
cgre = (0,   255, 0, 70)
cred = (255,   0, 0, 70)

n,w=35,500

epb1 = EnoPrismBars(flowLeft=False, textOffset2=(-18,0), fontSize=25, pathMaxDx=900)
epb1.addBar("22: Daejeon",  cyel, n)
epb1.addBar("23: Warsaw",   cblu, n)
epb1.addBar("24: Cork",     cblu, w)
epb1.addBar("25: Bordeaux", cblu, n)
epb1.addBar("26: Chicago",  cred, n)

n2=120
epb2 = EnoPrismBars(flowLeft=True, textOffset2=(675, 0), fontSize=25)
epb2.addBar("creativity",    cgre, n2)
epb2.addBar("dance+theater", cgre, n2)
epb2.addBar("music+sound",   cgre, n2)
epb2.addBar("actuation",     cyel, n2)
epb2.addBar("AI",            cyel, n2)
epb2.addBar("computing hardware", cyel, n2)

def setup():
  global b2
  b2 = Actor("teiblockconf04", pos=(600, HEIGHT-70))

def update():
  global initialized
  if not initialized: setup(); initialized=True

epb = [epb1, epb2]

def draw(): 
  screen.clear()
  for p in epb: p.draw(screen)
  b2.draw()

pgzrun.go()

### end ###
