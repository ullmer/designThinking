# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import traceback
import spectra
import pygame
from pgzero.builtins import Actor, animate, keyboard, keys

from hccReadingsYaml import *
from hccReadingsSuppl import *

################### readingsPg ################### 

class ReadingsPgHighlighted(hccReadingsPgSuppl):

  colorScaleColors = ['yellow', 'gold', 'white', 'cyan', 'chartreuse', 'violet']
  colorScale = None

  drawExtraAnnotatives  = True

  ################## constructor, error ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()

    try:    self.colorScale = spectra.scale(self.colorScaleColors)    //A
    except: print("problems with color scale; spectra probably not installed"); pass #if spectra installed, do the right thing

    self.buildUI()

  def err(self, msg): print("hccReadingsPgHighlighted error:", msg); traceback.print_exc()

  ################## get reading group color ##################

  def getReadingGroupColor(self, readingGroupId, colorType): 
    if self.numReadingGroups is None: #unassigned; error, sigh
      self.err("getGroupColor: numReadingGroups unassigned!"); return '#aaa'; #gray

    if self.colorScale is None: return '#c99' #spectra not installed, return red

    ratio = float(readingGroupId) / float(self.numReadingGroups)

    if colorType == 'hex': result = self.colorScale(ratio).hexcode
    else:                  r,g,b = self.colorScale(ratio).rgb; result = (r*255, g*255, b*255)
    return result

  ################## on_mouse_down ##################

  def on_mouse_down(self, pos): 
    for i in range(self.numRd):
      actor = self.actors[i]
      if actor.collidepoint(pos): 
        self.actorSelectedId = i
        return

      if self.drawExtraAnnotatives: 
        actor = self.timeDotActors[i]
        if actor.collidepoint(pos): 
          self.actorSelectedId = i
          self.dotSelected     = True
          return

  ################## on_mouse_move ##################

  def on_mouse_move(self, rel, buttons): 
    if self.actorSelectedId is not None:
      id     = self.actorSelectedId

      if not(self.dotSelected): actor  = self.actors[id]                           //A
      else:                     actor  = self.timeDotActors[id]

      x1, y1 = actor.pos
      dx, dy = rel
      x2, y2 = x1+dx, y1+dy

      if id in self.readingTextDrawOffset and not(self.dotSelected): 
        x3, y3 = self.readingTextDrawOffset[id]
        x4, y4 = x3+dx, y3+dy
        self.readingTextDrawOffset[id] = (x4, y4)

      actor.pos = (x2, y2)

  def on_mouse_up(self): 
     self.actorSelectedId = None
     self.dotSelected     = False

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
  
    screen.draw.text(au2,   topleft  = (x0+  3, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.2) //B
    screen.draw.text(yr2,   topright = (x0+285, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.2)
    screen.draw.text(abTi,  topleft  = (x0+  3, y0+41), fontsize=fs, fontname=f1, color=c1, alpha=0.5)
    screen.draw.text(mo,    topright = (x0+332, y0- 7), fontsize=fs, fontname=f1, color=c1, alpha=0.4)
    screen.draw.text(da,    topright = (x0+332, y0+41), fontsize=fs, fontname=f1, color=c1, alpha=0.3)

    rGn = reading.readingGroupNum
    if rGn is not None:
      gnt = self.getReadingGroupLetter(rGn)
      c2 = self.getReadingGroupColor(rGn, 'hex') 
      if self.drawExtraAnnotatives: 
        screen.draw.text(gnt, topright = (x0+285, y0+41), fontsize=fs, fontname=f1, color=c2, alpha=.7)

    if self.drawExtraAnnotatives: 
      rrect  = pygame.Rect(x0, y0, self.rrectX, self.rrectY)
      rcolor = self.getReadingGroupColor(rGn, 'rgb')

      if self.olderPgz: screen.draw.rect(rrect, rcolor)
      else:             screen.draw.rect(rrect, rcolor, width=2)

  ################## draw time dot text ################## 

  def drawTimeDotText(self, screen, readingId):
    reading = self.getReading(readingId)
    rGn     = reading.readingGroupNum
    f1, fs  = self.font1, self.fontSize

    if rGn is not None:
      timeDotActor = self.timeDotActors[readingId]
      gnt  = self.getReadingGroupLetter(rGn)
      c2   = self.getReadingGroupColor(rGn, 'hex') 
      x, y = timeDotActor.pos
      x   -= 1 #nudge by one pixel; a detail, but shows
      screen.draw.text(gnt, center=(x,y), fontsize=fs, fontname=f1, color=c2, alpha=.7)

### end ###
