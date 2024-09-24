# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import traceback
import spectra
import pygame
from hccReadingsYaml import *

WIDTH, HEIGHT = 1200, 800

################### readingsPg ################### 

class ReadingsPg(Readings):

  rows, cols =   6,   3
  dx, dy     = 350, 100
  x0, y0     =  50,  70
  actors     = None
  actor2id   = None
  numRd      = None
  readingGroups = None

  rrectX, rrectY = 336, 92

  font1      = "oswald-medium"
  fontSize   = 40
  cwhite     = "#ffffff"
  cblack     = "#000000"
  actorBgFn  = 'readings_box_1c'

  #colorScaleColors = ['orange', 'purple']
  #colorScaleColors = ['yellow', 'white', 'cyan', 'chartreuse', 'mauve']
  colorScaleColors = ['yellow', 'gold', 'white', 'cyan', 'chartreuse', 'violet']
  colorScale = None

  actorSelectedId       = None
  readingTextDrawOffset = None

  ################## constructor, error ##################

  def __init__(self): 
    super().__init__()
    self.actors                = []
    self.actor2id              = {}
    self.readingTextDrawOffset = {}

    try:    self.colorScale = spectra.scale(self.colorScaleColors)
    except: print("problems with color scale; spectra probably not installed"); pass #if spectra installed, do the right thing

    self.numRd    = self.size()
    rxc           = self.rows * self.cols
    if self.numRd > rxc: self.numRd = rxc

    self.buildUI()

  ################## error ##################

  def err(self, msg): print("ReadingPg error:", msg); traceback.print_exc()

  ################## get reading group color ##################

  def getReadingGroupColor(self, readingGroupId, cHex=True): 
    if self.numReadingGroups is None: #unassigned; error, sigh
      self.err("getGroupColor: numReadingGroups unassigned!"); return '#aaa'; #gray

    if self.colorScale is None: return '#c99' #spectra not installed, return red

    ratio = float(readingGroupId) / float(self.numReadingGroups)
    #result = self.colorScale(ratio).rgb

    if cHex: result = self.colorScale(ratio).hexcode
    else:     r,g,b = self.colorScale(ratio).rgb; result = (r*255, g*255, b*255)
    return result

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

    if self.readingGroups is None: #construct the reading groups
      self.readingGroups = {}
      for i in range(self.numRd):
        n = self.getReading(i).readingGroupNum
        if n not in self.readingGroups: self.readingGroups[n] = []
        self.readingGroups[n].append(i)

  ################## calculate reading position by id ##################

  def calcReadingPosById(self, readingId): 
    try:
      actor  = self.actors[readingId]
      result = actor.pos
      return result
    except: self.err("calcReadingPosById on readingId " + str(readingId)); return None

  ################## draw ##################

  def draw(self, screen): 
    for actor in self.actors: actor.draw()

    row, col = 0, 0
    x, y     = self.x0, self.y0
    
    for i in range(self.numRd):
      if i in self.readingTextDrawOffset: textDrawOffsetsSaved = True
      else:                               textDrawOffsetsSaved = False

      if textDrawOffsetsSaved:
        x2, y2 = self.readingTextDrawOffset[i]
      else:
        self.readingTextDrawOffset[i] = (x, y)
        x2, y2 = x, y

      self.drawReading(screen, i, x2, y2)

      if not(textDrawOffsetsSaved): # we need to calculate them. Logic should be relocated
        y += self.dy; row += 1

        if row >= self.rows: 
          row = 0; col += 1; y = self.y0; x += self.dx

    #draw lines connecting readings within reading groups
    self.drawLinesAmongReadingsInGroups(screen)

  ################## draw lines amongs readings in groups ##################

  def drawLinesAmongReadingsInGroups(self, screen): 
    for i in range(self.numReadingGroups):
      readingIds = self.readingGroups[i]
      lri = len(readingIds)
      if lri == 1: continue #nothing to do, onwards
      rgcolor = self.getReadingGroupColor(i, False) #False indicates "we need color triple, not hex"

      if lri >= 2:
        id0, id1 = readingIds[0], readingIds[1]
        self.drawLineBetweenReadings(screen, id0, id1, rgcolor, 2)
        if lri > 2:
          for j in range(2, lri):
            id1 = readingIds[j]
            self.drawLineBetweenReadings(screen, id0, id1, rgcolor, 2)

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

      if id in self.readingTextDrawOffset: 
        x3, y3 = self.readingTextDrawOffset[id]
        x4, y4 = x3+dx, y3+dy
        self.readingTextDrawOffset[id] = (x4, y4)

      actor.pos = (x2, y2)

  def on_mouse_up(self): self.actorSelectedId = None

  ################## draw reading ################## 
  
  def drawReading(self, screen, readingId, x0, y0):
    reading = self.getReading(readingId)
    au, yr, abTi, prDa = reading.getFields(['author', 'year', 'abbrevTitle', 'presentedDate']) 
    mo, da = prDa.split('-')
  
    if type(au) is list: au2 = ', '.join(au)
    else:                au2 = str(au)
  
    yr2    = str(yr)
    f1, fs = self.font1, self.fontSize
    c1     = self.cwhite
  
    screen.draw.text(au2,   topleft  = (x0+  3, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.2)
    screen.draw.text(yr2,   topright = (x0+285, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.2)
    screen.draw.text(abTi,  topleft  = (x0+  3, y0+41), fontsize=fs, fontname=f1, color=c1, alpha=0.5)
    screen.draw.text(mo,    topright = (x0+332, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.4)
    screen.draw.text(da,    topright = (x0+332, y0+41), fontsize=fs, fontname=f1, color=c1, alpha=0.3)

    rGn = reading.readingGroupNum
    if rGn is not None:
      gnt = str(chr(ord('A') + rGn))
      c2 = self.getReadingGroupColor(rGn) 
      screen.draw.text(gnt, topright = (x0+285, y0+41), fontsize=fs, fontname=f1, color=c2, alpha=.7)

    rrect  = pygame.Rect(x0, y0, self.rrectX, self.rrectY)
    rcolor = self.getReadingGroupColor(rGn, False)
    screen.draw.rect(rrect, rcolor, width=2)

  ################## draw line between readings: bl to tl ################## 
  
  def drawLineBetweenReadings(self, screen, readingId1, readingId2, rcolor, lwidth=1):
    x1, y1 = calcReadingPosById(readingId1)
    x2, y2 = calcReadingPosById(readingId2)
    y1 += self.rrectY

    screen.draw.line((x1, y1), (x2, y2), rcolor, width=lwidth)

################## main ################## 

if __name__ == "__main__":

  rpg = ReadingsPg()

  def draw(): screen.clear(); rpg.draw(screen)
  def on_mouse_down(pos):     rpg.on_mouse_down(pos)

### end ###
