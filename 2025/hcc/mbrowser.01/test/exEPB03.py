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

color1  = (0, 0, 255, 80)
color2  = (255, 255, 0, 60)

epb1 = EnoPrismBars(flowLeft=False, textOffset2=(-20,-30))
epb1.addBar("foo1", color1, 200)
epb1.addBar("foo2", color1, 200)

epb2 = EnoPrismBars(flowLeft=True, textOffset2=(350, 0))
epb2.addBar("bar1", color2, 150)
epb2.addBar("bar2", color2, 150)
epb2.addBar("bar3", color2, 150)

epb = [epb1, epb2]

def draw(): 
  screen.clear()
  for p in epb: p.draw(screen)

pgzrun.go()

### end ###
