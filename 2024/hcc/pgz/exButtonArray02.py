# Warming up on specific enoButtonArray variants
# Brygg Ullmer, Clemson University
# Begun 2024-09-09

WIDTH, HEIGHT = 800, 800

from enoButtonArray import *

bd        = (65, 40) #button dimension
bdx       = 70  
bp1       = (50, 25)
bp2       = (50, 750)

bd1Labels = ['time', 1800, 1900, 1910, 1940, 1980, 1990, 2000, 2010, 2010]
bd2Labels = ['slot'] + list(range(1,10))

eba1 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd1Labels, basePos=bp1)
eba2 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd2Labels, basePos=bp2)

headerColor = (50, 50, 50)
eba1.getButtonIdx(0).bgcolor1 = headerColor
eba2.getButtonIdx(0).bgcolor1 = headerColor

drawables  = [eba1, eba2]

def draw(): 
  screen.clear(); 
  for drawable in drawables:  drawable.draw(screen)

def on_mouse_down(pos):          
  for touchable in drawables: touchable.on_mouse_down(pos)

### end ###
