# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pgzrun
WIDTH, HEIGHT=1900,1000

from enoPrismBars import *

##### main ##### 

color1  = (0, 0, 255, 128)
color1N = 'blu1'

epb = EnoPrismBars(colorList=[color1], colorKeys=[color1N])
def draw(): 
  screen.clear(); epb.draw(screen)

pgzrun.go()

### end ###
