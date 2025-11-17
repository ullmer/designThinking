# Enodia prisms manuscripts browser
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os, sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0' #place window at 0,0 
sys.path.insert(0, #access module in parent directory (for test stubs)
  os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pgzrun, yaml
from pgzero.builtins import Actor, animate, keyboard, keys

WIDTH, HEIGHT=1800,1080

from enoPrisms        import *
from enoRefractBar    import *
from enoFrameBox      import *
from enoEntityListing import *

##### main ##### 

ep = EnoPrisms()
ep.summonPrism('teiLandscape', 0)
ep.summonPrism('teiYearsQ4',   1)

yf  = open('yaml/sampleEntries.yaml', 'rt')
yd  = yaml.safe_load(yf); yf.close()
winDim = (WIDTH, HEIGHT)
eel = EnoEntityListing(entries=yd, fieldsToPostfix=[0],
                       entryFontSize=25, winDim=winDim)

rb  = EnoRefractBar((WIDTH, 80), (0, 750))
efb = EnoFrameBox()

def update(): ep.update()

firstDraw = True

################ draw ################
def draw(): 
  global firstDraw
  screen.clear()
  if firstDraw: firstDraw=False; ep.intersectPrismBarPair(0, 1, 0, 0)
  eel.draw(screen)
  ep.draw(screen)
  rb.draw(screen)
  rcol = rb.fillColor
  screen.draw.text("TEI", midleft=(305,70), alpha=.2, 
    color=rcol, fontname="barlow_black", fontsize=250)
  efb.draw(screen)

################ on_mouse/key_down ################

def on_mouse_down(pos):
  ep.parseLocus(pos)

def on_key_down(key, mod): 
  efb.on_key_down(key, mod)

pgzrun.go()

### end ###
