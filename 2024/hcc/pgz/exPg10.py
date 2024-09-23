# Example ~visualizing class readings
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsPg import *

WIDTH, HEIGHT = 1200, 800

rpg = ReadingsPg()
bg  = Actor(bg01a)

def draw(): screen.clear();      rpg.draw(screen); bg.draw()
def on_mouse_down(pos):          rpg.on_mouse_down(pos)
def on_mouse_move(rel, buttons): rpg.on_mouse_move(rel, buttons)
def on_mouse_up():               rpg.on_mouse_up()

### end ###
