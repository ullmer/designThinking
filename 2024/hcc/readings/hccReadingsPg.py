# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import traceback
from hccReadingsYaml import *

WIDTH, HEIGHT = 1200, 800

################### readingsPg ################### 

class ReadingsPg(Readings):

  rows, cols =   6,   2
  dx, dy     = 350, 100
  x0, y0     =  50,  10
  actors     = None
  actor2id   = None
  numRd      = None

  font1    = "oswald-medium"
  fontSize = 40
  cwhite   = "#ffffff"
  cblack   = "#000000"

  actorBgFn  = 'readings_box_1c'

  ################## constructor, error ##################

  def __init__(self): 
    super().__init__()
    self.actors   = []
    self.actor2id = {}

    self.numRd    = self.size()
    rxc           = self.rows * self.cols
    if self.numRd > rxc: self.numRd = rxc

    self.buildUI()

  def err(self, msg): print("ReadingPg error:", msg); traceback.print_exc()

  ################## build UI ##################

  def buildUI(self): 
    row, col = 0, 0
    x, y     = self.x0, self.y0

    for i in range(self.numRd):
      a = Actor(self.actorBgFn, topleft=(x, y))
      self.actors.append(a)
      y += self.dy; row += 1; self.actor2id[a] = i

      if row >= self.rows: 
        row = 0; col += 1; y = self.y0; x += self.dx

  ################## draw ##################

  def draw(self, screen): 
    for actor in self.actors: actor.draw()

    row, col = 0, 0
    x, y     = self.x0, self.y0

    for i in range(self.numRd):
      r = self.getReading(i)
      self.drawReading(screen, r, x, y)
      y += self.dy; row += 1

      if row >= self.rows: 
        row = 0; col += 1; y = self.y0; x += self.dx

  ################## on_mouse_down ##################

  def on_mouse_down(self, pos): 
    for i in range(self.numRd):
      actor = self.actors[i]
      if actor.collidepoint(pos): print("Actor was pressed:", i)

  ################## draw reading ################## 
  
  def drawReading(self, screen, reading, x0, y0):
    au, yr, abTi, prDa = reading.getFields(['author', 'year', 'abbrevTitle', 'presentedDate']) 
    mo, da = prDa.split('-')
  
    if type(au) is list: au2 = ', '.join(au)
    else:                au2 = str(au)
  
    yr2    = str(yr)
    f1, fs = self.font1, self.fontSize
    c1     = self.cwhite
  
    screen.draw.text(au2,  topleft  = (x0+  3, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.2)
    screen.draw.text(yr2,  topright = (x0+285, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.2)
    screen.draw.text(abTi, topleft  = (x0+  3, y0+41), fontsize=fs, fontname=f1, color=c1, alpha=0.5)
    screen.draw.text(mo,   topright = (x0+332, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.4)
    screen.draw.text(da,   topright = (x0+332, y0+41), fontsize=fs, fontname=f1, color=c1, alpha=0.3)

################## main ################## 

if __name__ == "__main__":

  rpg = ReadingsPg()

  def draw(): screen.clear(); rpg.draw(screen)
  def on_mouse_down(pos):     rpg.on_mouse_down(pos)

### end ###
