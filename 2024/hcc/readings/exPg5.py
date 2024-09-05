# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsYaml import *

WIDTH, HEIGHT = 800, 800

a1 = Actor('readings_box_1c', pos=(400,400))
a2 = Actor('readings_box_1c', pos=(400,500))
actors = [a1, a2]

readings = Readings()
readings.loadYaml()
r0       = readings.getReading(0)

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()
  drawReading(r0, 400, 400)

def on_mouse_down(pos): 
  if a1.collidepoint(pos): print("Actor 1 was pressed")
  if a2.collidepoint(pos): print("Actor 2 was pressed")
  
def drawReading(reading, x0, y0):
  print("foo")

### end ###
