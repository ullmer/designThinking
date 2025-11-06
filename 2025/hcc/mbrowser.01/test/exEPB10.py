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
from prismsTei    import *

##### main ##### 

pt = PrismsTei()
p0 = pt.getPrism('teiLandscape', 0)
p1 = pt.getPrism('teiYearsQ4',   1)


def update():
  global initialized
  if not initialized: setup(); initialized=True

epb = [epb1a, epb1b, epb2a, epb2b]

refractBar = pygame.Surface((WIDTH, 80), pygame.SRCALPHA)
rcolor = (255, 255, 255, 45)
refractBar.fill(rcolor)

def draw(): 
  screen.clear()
  for b in bs:  b.draw(screen)
  for p in epb: p.draw(screen)
  screen.blit(refractBar, (0, 850))
  screen.draw.text("TEI", midleft=(300,70), alpha=.2, color=rcolor, fontname="barlow_black", fontsize=250)

#def on_mouse_down(pos):
#  parsePress(pos)

pgzrun.go()

### end ###
