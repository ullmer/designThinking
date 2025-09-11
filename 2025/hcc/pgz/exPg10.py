# Example ~visualizing class readings
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsPg import *

WIDTH, HEIGHT = 1920, 1080

rpg = ReadingsPg()
#rpg = ReadingsPg(font1='party')
bg  = Actor('bg01e')

def draw(): screen.clear(); bg.draw(); rpg.draw(screen); 
def on_mouse_down(pos):                rpg.on_mouse_down(pos)
def on_mouse_move(rel, buttons):       rpg.on_mouse_move(rel, buttons)
def on_mouse_up():                     rpg.on_mouse_up()

### end ###
