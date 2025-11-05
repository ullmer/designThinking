# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import math
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

  drawText     = True
  textStrs     = None
  textAngle    = None
  textColor    = (255, 255, 255)
  textAlpha    = .7
  fontName     = "barlow_condensed_extralight"
  fontSize     = 35
  textOffset   = (150, 170)

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

  ############# calcTextAngle #############

  def calcTextAngle(self): 
    if self.flowLeft:
      angle_rad = math.atan2(self.pathMaxDy, -self.pathMaxDx)
      angle_deg = math.degrees(angle_rad)+180
    else: 
      angle_rad = math.atan2(self.pathMaxDy,  self.pathMaxDx)
      angle_deg = math.degrees(angle_rad)

    self.textAngle = angle_deg

  ############# drawText #############

  def drawTexts(self): #CoPilot
    if self.textStrs  is None: 
      if verbose: self.msg('drawText called, no text to be drawn')

    if self.textAngle is None: self.calcTextAngle()
    str1 = None
    if   isinstance(self.textStrs, str):  str1 = self.textStrs
    elif isinstance(self.textStrs, list): str1 = self.textStrs[0]
    else:                                 return

    fn, fs   = self.fontName, self.fontSize
    tox, toy = self.textOffset
    bx,  by  = self.basePos
    x, y     = bx+tox+self.pathWidth, by+toy
    ta, tc   = self.textAlpha, self.textColor
    tan      = self.textAngle

    screen.draw.text(str1, (x,y), alpha=ta, color=tc, fontname=fn, fontsize=fs, angle=tan)
    self.msg("drawTexts called on " + str1 + str((x,y)))

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

    if self.drawText: self.drawTexts()

### end ###
