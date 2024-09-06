# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

import pygame  
import math

#WIDTH, HEIGHT = 500, 500

############################ enodia animated transparent box ############################

class enoAnimTranspBox:

  lineThickness = 5
  #alpha        = 128  #on 255 scale
  lineColor     = (128, 128, 128, 128) #include alpha as 4th element
  topLeft       = None #tuple
  bottomRight   = None #tuple
  boxHeight     = None
  boxWidth      = None

  animTL1, animBR1 = None, None
  animTL2, animBR2 = None, None

  animDuration = 0.5
  animActive   = 0

  verticalLinesSurface = None
  horizLinesSurface    = None

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    if topLeft is not None and bottomRight is not None: self.buildBox()

  ####################### error message (redirectable) ####################

  def err(self, msg): print("enoAnimTranspBox:", str(msg))

  ############################ set bounds ############################

  def setBounds(self, topLeft, bottomRight):
    self.topLeft     = topLeft
    self.bottomRight = bottomRight
    self.calcWidthHeight()
  
  def calcWidthHeight(self):
    if self.topLeft is None or self.bottomRight is None:
      self.err("calcWidthHeight: topLeft and/or bottomRight coordinates not set!"); return

    x1, y1 = self.topLeft
    x2, y2 = self.bottomRight

    self.boxWidth  = math.abs(x2-x1)
    self.boxHeight = math.abs(y2-y1)

  ############################ build box ############################

  def buildBox(self):

    # Create blittable surface that supports alpha values

    if self.topLeft is None or self.bottomRight is None:
      self.err("buildBox: topLeft and/or bottomRight coordinates not set!"); return

    if self.boxWidth is None or self.boxHeight is None: self.calcWidthHeight()

    w1 = self.lineThickness
    h1 = self.boxHeight

    w2 = self.boxWidth - (self.lineThickness * 2)
    h2 = self.lineThickness

    self.verticalLinesSurface = pygame.Surface((w1,h1), pygame.SRCALPHA)
    self.horizLinesSurface    = pygame.Surface((w2,h2), pygame.SRCALPHA)

    pygame.draw.rect(self.verticalLinesSurface, color, (0, 0), (w1, h1), self.lineThickness)
    pygame.draw.rect(self.horizLinesSurface,    color, (0, 0), (w2, h2), self.lineThickness)

  ############################ draw ############################

  def draw(self, screen):

  # Draw the line on the temporary surface
  #pygame.draw.line(s1, color, start_pos, end_pos, width)

  # Draw the surface on the screen
  screen.blit(s1, (0,0))
  screen.blit(s2, (0,0))

### end ###
