# Enodia prisms manuscripts browser
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os,sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pgzrun
from pgzero.builtins import Actor, animate, keyboard, keys

WIDTH, HEIGHT=1600,1080

from enoPrisms   import *
from enoFrameBox import *

##### main ##### 

ep = EnoPrisms()
ep.summonPrism('teiLandscape', 0)
ep.summonPrism('teiYearsQ4',   1)

rb  = RefractBar((WIDTH, 80), (0, 750))
efb = EnoFrameBox()

def update(): ep.update()

def draw(): 
  screen.clear()
  ep.draw(screen)
  rb.draw(screen)
  rcol = rb.fillColor
  screen.draw.text("TEI", midleft=(305,70), alpha=.2, color=rcol, fontname="barlow_black", fontsize=250)
  efb.draw(screen)

#def on_mouse_down(pos):
#  parsePress(pos)

pgzrun.go()

### end ###
