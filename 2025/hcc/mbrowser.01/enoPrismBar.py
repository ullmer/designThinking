# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import math
import pygame
import pygame.gfxdraw

from ataBase import *

class EnoPrismBar(AtaBase):
  basePos    = (0, 0)
  baseShiftX = None
  barWidth   = 500
  baseWidth  = None # if None, same as barWidth
  pathMaxDx  = 800
  pathMaxDy  = 950

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

  ############# find tuple list minimum x#############

  def findTupleListMinX(self, targList):
    minEl = None
    try:
      for el in targList:
        x, y = el
        if minEl is None: minEl = x
        elif  x  < minEl: minEl = x
      return minEl
    except: self.err("findTupleListMinX")

  ############# normalize points/vertices #############

  def normPoints(self, vertices, minX):
    try:
      if minX >= 0: return vertices
      result  = []
      absMinX = abs(minX)

      for el in vertices:
        x, y = el
        x   += absMinX
        result.append((x,y))
      return result
    except: self.err("normPoints")

  ############# create surface #############

  def createSurface(self):

    bottomWidth = self.barWidth
    if self.baseWidth is not None: bottomWidth = self.baseWidth

    self.maxH = self.pathMaxDy 
    self.maxW = self.pathMaxDx
    bwp = bottomWidth + self.pathMaxDx
    if self.barWidth > self.maxW: self.maxW = self.barWidth
    if bwp > self.maxW:           self.maxW = bwp
    if self.baseShiftX > 0:       self.maxW += self.baseShiftX

    self.surfaceList = []

    # Create a transparent surface
    #surf = pygame.Surface((self.maxW, self.maxH), pygame.SRCALPHA)
    surf = pygame.Surface((self.maxW, self.maxH), pygame.SRCALPHA)

    #bpxs                  = self.botPosXStart 
    #if bpxs is None: bpxs = self.pathMaxDx
    bpxs = self.pathMaxDx

    bsx = 0 # baseShift X
    if self.baseShiftX is not None: bsx += self.baseShiftX
    
    # Define polygon points
    if not self.flowLeft:
      points = [(0, 0), (self.barWidth, 0), 
                (bsx + bpxs + bottomWidth, self.maxH),
                (bsx + bpxs,               self.maxH)]

    else: 
      points = [(self.pathMaxDx + self.barWidth, 0), (self.pathMaxDx, 0), 
                (bsx,               self.maxH),
                (bsx + bottomWidth, self.maxH)]

    print("foo", str(points))
    minX = self.findTupleListMinX(points)
    if minX < 0: 
      points = self.normPoints(points, minX)
      self.baseShiftX = minX
    print("bar", str(points))

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
      pos = self.basePos
      if self.baseShiftX is not None:
        x, y = pos
        x   += self.baseShiftX
        pos  = (x, y)

      screen.blit(surf, self.basePos)

    if self.drawText: self.drawTexts(screen)

### end ###
