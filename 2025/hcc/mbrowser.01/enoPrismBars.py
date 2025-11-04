# Enodia "prism bars"
# Brygg Ullmer, Clemson University
# Begun 2025-11-03

import pygame
import ataBase

class EnoPrismBars(AtaBase):
  pathWidth = 100
  pathMaxDx = 300
  pathMaxDy = 700
  screen    = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# create colors #############
    
  def createColors(self, ):
    # Define a color with alpha (RGBA)
    colRed = (255, 0, 0, 128)  # Semi-transparent red

  ############# create surface #############

  def createSurface(self, ):

    # Create a transparent surface
    poly1 = pygame.Surface((400, 400), pygame.SRCALPHA)
    poly2 = pygame.Surface((400, 400), pygame.SRCALPHA)

    # Define polygon points
    points1 = [(100, 100), (300, 100), (350, 300), (150, 350)]
    points2 = [(200,   0), (400, 400), (  0, 400)]

# Draw the polygon on the transparent surface
pygame.draw.polygon(poly1, colRed, points1)
pygame.draw.polygon(poly2, colRed, points2)

def draw():
  screen.clear()
  screen.blit(poly1, (0, 0))
  screen.blit(poly2, (0, 0))



### end ###
