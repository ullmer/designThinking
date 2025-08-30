# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsPg  import *

#WIDTH, HEIGHT = 1200, 800
WIDTH, HEIGHT = 335, 94

hrpg = HccReadingsPg(x0=0, y0=0)

def draw(): 
  screen.clear()
  hrpg.draw(screen)
  pygame.image.save(screen.surface, "tiles/t01.png")

### end ###
