# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import pygame
import pygame.gfxdraw
from ataBase import *

class EnoPrismBars(AtaBase):
  basePos   = (50, 0)
  pathWidth = 500
  pathMaxDx = 800
  pathMaxDy = 950

  colorDict  = None
  colorList  = None
  colorKeys  = None
  maxW, maxH = None, None

  surfaceList  = None
  screen       = None
  flowLeft     = False # directionality of prismatic angle; better name TBD
  drawOutline     = True
  drawAntialiased = True
  outlineColor = (255, 255, 255, 135)
  outlineWidth = 1

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.createColors()
    self.createSurface()

  ############# create colors #############
    
  def createColors(self):
    self.colorDict = {}

    if self.colorList is None: 
      self.msg("createColors: colorList unassigned"); return

    if self.colorKeys is None: 
      self.msg("createColors: colorKeys unassigned"); return

    for colorSpec, colorName in zip(self.colorList, self.colorKeys):
      self.colorDict[colorName] = colorSpec

    ## Define a color with alpha (RGBA)
    #colRed = (255, 0, 0, 128)  # Semi-transparent red

  ############# create surface #############

  def createSurface(self):
    colorH = self.colorList[0]

    self.maxW = self.pathWidth + self.pathMaxDx 
    self.maxH = self.pathMaxDy 
    self.surfaceList = []

    # Create a transparent surface
    surf = pygame.Surface((self.maxW, self.maxH), pygame.SRCALPHA)

    # Define polygon points
    if not self.flowLeft:
      points = [(0, 0), (self.pathWidth, 0), 
                (self.pathMaxDx + self.pathWidth, self.maxH),
                (self.pathMaxDx,                  self.maxH)]
    else:
      points = [(self.pathMaxDx + self.pathWidth, 0), (self.pathMaxDx, 0), 
                (0,              self.maxH),
                (self.pathWidth, self.maxH)]

    # Draw the polygon on the transparent surface
    pygame.draw.polygon(surf, colorH, points)

    if self.drawOutline:
      if self.drawAntialiased:
        lenPoints = len(points)
        for i in range(lenPoints):
          start, end = points[i], points[(i+1) % lenPoints]
          x1, y1 = start; x2, y2 = end; x1 += 1; x2 -= 1
          pygame.gfxdraw.line(surf, x1, y1, x2, y2, self.outlineColor)

      else: pygame.draw.polygon(surf, self.outlineColor, points, width=self.outlineWidth)

    self.surfaceList.append(surf)

  ############# draw #############

  def draw(self, screen):
    for surf in self.surfaceList:
      screen.blit(surf, self.basePos)

### end ###
