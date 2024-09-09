# Warming up on specific enoButtonArray variants
# Brygg Ullmer, Clemson University
# Begun 2024-09-09

import * from enoButtonArray

bd  = (75, 40) #button dimension
bdx = 80
bd1Text = [1800, 1900, 1910, 1940, 1980, 1990, 2000, 2010, 2010)

eba1 = enoButtonArray(buttonDim = bd, dx=bdx, textArray = bd1Text)

def draw(): screen.clear(); eba1.draw()

### end ###
