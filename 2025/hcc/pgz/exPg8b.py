# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import traceback
from hccReadingsYaml import *
from hccReadingsPg import   *
WIDTH, HEIGHT = 1200, 800

hrpg = HccReadingsPg()

def draw(): screen.clear(); hrpg.draw(screen)
def on_mouse_down(pos):     hrpg.on_mouse_down(pos)

### end ###
