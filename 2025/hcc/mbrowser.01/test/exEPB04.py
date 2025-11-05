# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pgzrun
WIDTH, HEIGHT=1900,1000

from enoPrismBar  import *
from enoPrismBars import *

##### main ##### 

cblu = (0,   0, 255, 80)
cyel = (255, 255, 0, 70)
cgre = (0,   255, 0, 70)
cred = (255,   0, 0, 70)

epb1 = EnoPrismBars(flowLeft=False, textOffset2=(-20,-30))
epb1.addBar("22: Daejeon",  cyel, 50)
epb1.addBar("23: Warsaw",   cblu, 50)
epb1.addBar("24: Cork",     cblu, 200)
epb1.addBar("25: Bordeaux", cblu, 200)
epb1.addBar("26: Chicago",  cred, 50)

epb2 = EnoPrismBars(flowLeft=True, textOffset2=(350, 0))
epb2.addBar("creativity",    cgre, 150)
epb2.addBar("dance+theater", cgre, 150)
epb2.addBar("music+sound",   cgre, 150)
epb2.addBar("actuation",     cyel, 150)
epb2.addBar("AI",            cyel, 150)
epb2.addBar("computing hardware", cyel, 150)

epb = [epb1, epb2]

def draw(): 
  screen.clear()
  for p in epb: p.draw(screen)

pgzrun.go()

### end ###
