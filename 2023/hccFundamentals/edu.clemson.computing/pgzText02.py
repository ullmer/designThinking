# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButton import *

WIDTH=600
HEIGHT=600

global but1
but1 = enoButton("hello, world")
but2 = enoButton("line2"); but2.nudgeY(35)

def draw(): 
  global but1
  but1.draw(screen)
  but2.draw(screen)

### end ###
