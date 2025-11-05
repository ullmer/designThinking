# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pgzrun
WIDTH, HEIGHT=1900,1000

from enoPrismBar import *

##### main ##### 

color1  = (0, 0, 255, 80)
color1N = 'blu1'

color2  = (255, 255, 0, 60)
color2N = 'yel1'

epb1 = EnoPrismBar(colorList=[color1], colorKeys=[color1N], textStrs="foo", flowLeft=False, textOffset2=(-20,-30))
epb2 = EnoPrismBar(colorList=[color2], colorKeys=[color2N], textStrs="bar", flowLeft=True)
epb = [epb1, epb2]

def draw(): 
  screen.clear()
  for p in epb: p.draw(screen)

pgzrun.go()

### end ###
