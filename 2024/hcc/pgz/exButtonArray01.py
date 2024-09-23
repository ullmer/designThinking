# Warming up on specific enoButtonArray variants
# Brygg Ullmer, Clemson University
# Begun 2024-09-09

WIDTH, HEIGHT = 800, 800

from enoButtonArray import *

bd        = (75, 40) #button dimension
bdx       = 80
bd1Labels = [1800, 1900, 1910, 1940, 1980, 1990, 2000, 2010, 2010]
bp1       = (50, 25)

eba1 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd1Labels, basePos=bp1)

def draw():      screen.clear(); eba1.draw(screen)
def on_mouse_down(pos):          eba1.on_mouse_down(pos)

### end ###
