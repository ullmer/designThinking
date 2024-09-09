# Warming up on specific enoButtonArray variants
# Brygg Ullmer, Clemson University
# Begun 2024-09-09

WIDTH, HEIGHT = 800, 800

from enoButtonArray import *

bd        = (70, 40)  #button dimension
bdx       = 75        #x offset between buttons
bp1       = (50, 25)  #button array 1 base position
bp2       = (50, 700) #button array 3 base position
bp3       = (50, 750) #button array 2 base position

bd1Labels = ['time', 1800, 1900, 1910, 1940, 1980, 1990, 2000, 2010, 2010]
bd2Labels = ['action', 'store', 'load']
bd3Labels = ['slot'] + list(range(1,10))

eba1 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd1Labels, basePos=bp1)
eba2 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd2Labels, basePos=bp2)
eba3 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd3Labels, basePos=bp3)

headerColor = (50, 50, 50)
for ba in [eba1, eba2, eba3]: ba.getButtonIdx(0).bgcolor1 = headerColor

drawables  = [eba1, eba2, eba3]

def draw(): 
  screen.clear(); 
  for drawable in drawables:  drawable.draw(screen)

def on_mouse_down(pos):          
  for touchable in drawables: touchable.on_mouse_down(pos)

### end ###
