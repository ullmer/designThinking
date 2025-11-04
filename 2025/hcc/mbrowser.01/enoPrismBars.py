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

    # Create a transparent surface
    poly1 = pygame.Surface((400, 400), pygame.SRCALPHA)
    poly2 = pygame.Surface((400, 400), pygame.SRCALPHA)

    # Define polygon points
    points1 = [(100, 100), (300, 100), (350, 300), (150, 350)]
    points2 = [(200,   0), (400, 400), (  0, 400)]

    # Draw the polygon on the transparent surface
    pygame.draw.polygon(poly1, colRed, points1)
    pygame.draw.polygon(poly2, colRed, points2)

  ############# draw #############

  def draw():
    screen.blit(poly1, (0, 0))
    screen.blit(poly2, (0, 0))

### end ###
