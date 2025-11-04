# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import pygame
import ataBase

class EnoPrismBars(AtaBase):
  pathWidth = 100
  pathMaxDx = 300
  pathMaxDy = 700

  colorDict  = None
  colorList  = None
  colorKeys  = None
  maxW, maxH = None, None

  surfaceList = None
  screen    = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

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
    pygame.draw.polygon(surf, color, points]
    self.surfaceList.append(surf)

  ############# draw #############

  def draw():
    screen.blit(poly1, (0, 0))
    screen.blit(poly2, (0, 0))

### end ###
