# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun

WIDTH, HEIGHT=1900,1000

import pygame
from ataBase import *

class EnoPrismBars(AtaBase):
  basePos   = (50, 0)
  pathWidth = 300
  pathMaxDx = 800
  pathMaxDy = 950

  colorDict  = None
  colorList  = None
  colorKeys  = None
  maxW, maxH = None, None

  surfaceList = None
  screen      = None

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
    points = [(0, 0), (self.pathWidth, 0), 
              (self.pathMaxDx + self.pathWidth, self.maxH),
              (self.pathMaxDx,                  self.maxH)]

    # Draw the polygon on the transparent surface
    pygame.draw.polygon(surf, colorH, points)
    self.surfaceList.append(surf)

  ############# draw #############

  def draw(self, screen):
    for surf in self.surfaceList:
      screen.blit(surf, self.basePos)

##### main ##### 

color1  = (0, 0, 255, 128)
color1N = 'blu1'

epb = EnoPrismBars(colorList=[color1], colorKeys=[color1N])
def draw(): 
  screen.clear(); epb.draw(screen)

pgzrun.go()
### end ###
