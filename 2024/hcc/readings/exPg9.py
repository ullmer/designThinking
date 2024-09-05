# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsPg import *

WIDTH, HEIGHT = 1200, 800

rpg = ReadingsPg()

def draw(): screen.clear(); rpg.draw(screen)
def on_mouse_down(pos):     rpg.on_mouse_down(pos)

### end ###
