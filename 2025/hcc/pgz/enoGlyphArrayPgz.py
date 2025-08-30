# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-07

import traceback
from ataBase import *

WIDTH, HEIGHT = 1200, 800

################### enodia glyph array : pygame zero ################### 

class enoGlyphArrayPgz(AtaBase):

  textualsList = None
  actors       = None

  actor2id   = None

  font1      = "oswald-medium"
  fontSize   = 40
  cwhite     = "#ffffff"
  cblack     = "#000000"
  actorBgFn  = 'readings_box_1c'

  actorSelectedId       = None
  contentTextDrawOffset = None

  ################## constructor, error ##################

  def __init__(self): 
    super().__init__()
    self.actors                = []
    self.actor2id              = {}
    self.contentTextDrawOffset = {}

    try:    self.numRd    = self.size()
    except: self.err("__init__")

    rxc           = self.rows * self.cols
    if self.numRd > rxc: self.numRd = rxc

    self.buildUI()

  def err(self, msg): print("ContentsPgz error:", msg); traceback.print_exc()

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
      if i in self.contentTextDrawOffset: textDrawOffsetsSaved = True
      else:                               textDrawOffsetsSaved = False

      if textDrawOffsetsSaved:
        x2, y2 = self.contentTextDrawOffset[i]
      else:
        self.contentTextDrawOffset[i] = (x, y)
        x2, y2 = x, y

      self.drawContent(screen, i, x2, y2)

      if not(textDrawOffsetsSaved): # we need to calculate them. Logic should be relocated
        y += self.dy; row += 1

        if row >= self.rows: 
          row = 0; col += 1; y = self.y0; x += self.dx

  ################## on_mouse_down ##################

  def on_mouse_down(self, pos): 
    for i in range(self.numRd):
      actor = self.actors[i]
      if actor.collidepoint(pos): 
        print("Actor selected:", i)
        self.actorSelectedId = i

  ################## on_mouse_move ##################

  def on_mouse_move(self, rel, buttons): 
    if self.actorSelectedId is not None:
      id     = self.actorSelectedId
      actor  = self.actors[id]
      x1, y1 = actor.pos
      dx, dy = rel
      x2, y2 = x1+dx, y1+dy

      if id in self.contentTextDrawOffset: 
        x3, y3 = self.contentTextDrawOffset[id]
        x4, y4 = x3+dx, y3+dy
        self.contentTextDrawOffset[id] = (x4, y4)

      actor.pos = (x2, y2)

  def on_mouse_up(self): self.actorSelectedId = None

################## main ################## 

if __name__ == "__main__":

  rpg = ContentsPgz()

  def draw(): screen.clear(); rpg.draw(screen)
  def on_mouse_down(pos):     rpg.on_mouse_down(pos)

### end ###
