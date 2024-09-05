# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsYaml import *

WIDTH, HEIGHT = 800, 800

numRd  = 8
dy     = 100
y = y0 = 10
actors = []

for i in range(numRd):
  a = Actor('readings_box_1c', topleft=(50,y))
  actors.append(a); y += dy

font1  = "oswald-medium"
cwhite = "#ffffff"
cblack = "#000000"

readings = Readings()
readings.loadYaml()

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()
  y = y0

  for i in range(numRd):
    r = readings.getReading(i)
    drawReading(r, 50, y)
    y += dy

def on_mouse_down(pos): 
  if a1.collidepoint(pos): print("Actor 1 was pressed")
  if a2.collidepoint(pos): print("Actor 2 was pressed")
  
def drawReading(reading, x0, y0):
  au, yr, abTi, prDa = reading.getFields(['author', 'year', 'abbrevTitle', 'presentedDate']) 
  mo, da = prDa.split('-')
  fs = 40

  au2 = ', '.join(au)
  yr2 = str(yr)

  screen.draw.text(au2,  topleft  = (x0+  3, y0- 7), fontsize=fs, fontname=font1, color=cwhite, alpha=0.2)
  screen.draw.text(yr2,  topright = (x0+285, y0- 7), fontsize=fs, fontname=font1, color=cwhite, alpha=0.2)
  screen.draw.text(abTi, topleft  = (x0+  3, y0+41), fontsize=fs, fontname=font1, color=cwhite, alpha=0.5)
  screen.draw.text(mo,   topright = (x0+332, y0- 7), fontsize=fs, fontname=font1, color=cblack, alpha=0.4)
  screen.draw.text(da,   topright = (x0+332, y0+41), fontsize=fs, fontname=font1, color=cblack, alpha=0.4)

### end ###
