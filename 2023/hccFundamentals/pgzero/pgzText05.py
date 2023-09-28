# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButton import *
import yaml

WIDTH=900
HEIGHT=600

panel1Fn = 'panel1.yaml'
panel1F  = open(panel1Fn, 'r+t')
panel1Y  = yaml.safe_load(panel1F)

print(panel1Y)

global panel
panel = []

dy = 50; idx = 0

for row in panel1Y: #rows
  ba = enoButtonArray(row, buttonDim=(150, 30), dx=160, 
                           basePos=(0, dy*idx))
  panel.append(ba); idx += 1

def draw(): 
  global panel
  for ba in panel: ba.draw(screen)

def on_mouse_down(pos):
  global panel
  for ba in panel: ba.on_mouse_down(pos)

### end ###
