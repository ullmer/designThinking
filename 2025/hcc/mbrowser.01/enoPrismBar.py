# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import math
import pygame
import pygame.gfxdraw

from ataBase import *

class EnoPrismBar(AtaBase):
  basePos   = (0, 0)
  barWidth  = 500
  baseWidth = None # if None, same as barWidth
  pathMaxDx = 800
  pathMaxDy = 950

  barColor   = None
  maxW, maxH = None, None

  surfaceList     = None
  screen          = None
  flowLeft        = False # directionality of prismatic angle; better name TBD
  drawOutline     = True
  drawAntialiased = True
  outlineColor    = (255, 255, 255, 135)
  outlineWidth    = 1

  drawText     = True
  textStrs     = None
  textAngle    = None
  textColor    = (255, 255, 255)
  textAlpha    = .7
  fontName     = "barlow_condensed_extralight"
  fontSize     = 32
  textOffset   = (10, 10)
  textOffset2  = (0, 0)

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.createSurface()

  ############# calcTextAngle #############

  def calcTextAngle(self): 
    if self.flowLeft:
      angle_rad = math.atan2(self.pathMaxDy,  self.pathMaxDx)
      angle_deg = math.degrees(angle_rad)
    else: 
      angle_rad = math.atan2(self.pathMaxDy, -self.pathMaxDx)
      angle_deg = math.degrees(angle_rad)+180

    self.textAngle = angle_deg

  ############# drawText #############

  def drawTexts(self, screen):
    if self.textStrs  is None: 
      if verbose: self.msg('drawText called, no text to be drawn')

    if self.textAngle is None: self.calcTextAngle()
    str1 = None
    if   isinstance(self.textStrs, str):  str1 = self.textStrs
    elif isinstance(self.textStrs, list): str1 = self.textStrs[0]
    else:                                 return

    fn, fs     = self.fontName, self.fontSize
    tox1, toy1 = self.textOffset
    tox2, toy2 = self.textOffset2

    bx, by  = self.basePos
    x, y    = bx+tox1+tox2+self.barWidth, by+toy1+toy2
    ta, tc  = self.textAlpha, self.textColor
    tan     = self.textAngle

    if self.flowLeft:
      screen.draw.text(str1, midright=(x,y), alpha=ta, color=tc, fontname=fn, fontsize=fs, angle=tan)
    else:
      screen.draw.text(str1, midleft=(x,y),  alpha=ta, color=tc, fontname=fn, fontsize=fs, angle=tan)

  ############# create surface #############

  def createSurface(self):

    self.maxW = self.barWidth + self.pathMaxDx 
    self.maxH = self.pathMaxDy 
    self.surfaceList = []

    # Create a transparent surface
    surf = pygame.Surface((self.maxW, self.maxH), pygame.SRCALPHA)

    bottomWidth = self.barWidth
    if self.baseWidth is not None: bottomWidth = self.baseWidth
    
    # Define polygon points
    if not self.flowLeft:
      points = [(0, 0), (self.barWidth, 0), 
                (self.pathMaxDx + bottomWidth, self.maxH),
                (self.pathMaxDx,                  self.maxH)]
    else:
      points = [(self.pathMaxDx + self.barWidth, 0), (self.pathMaxDx, 0), 
                (0,              self.maxH),
                (bottomWidth, self.maxH)]

    # Draw the polygon on the transparent surface
    pygame.draw.polygon(surf, self.barColor, points)

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

    if self.drawText: self.drawTexts(screen)

### end ###
