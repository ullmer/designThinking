# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

import pygame  

WIDTH, HEIGHT = 500, 500

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
  verbose      = False

  verticalLinesSurface = None
  horizLinesSurface    = None

  vCoord1, vCoord2 = None, None #cached coordinates for blitting operations
  hCoord1, hCoord2 = None, None
  vRect,   hRect   = None, None

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    if self.topLeft is not None and self.bottomRight is not None: self.buildBox()

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

    self.boxWidth  = abs(x2-x1)
    self.boxHeight = abs(y2-y1)

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

    print("bb w2 h2:", w2, h2)

    c  = self.lineColor

    self.verticalLinesSurface = pygame.Surface((w1,h1), pygame.SRCALPHA)
    self.horizLinesSurface    = pygame.Surface((w2,h2), pygame.SRCALPHA)

    self.vRect = Rect((0,0), (w1, h1))
    self.hRect = Rect((0,0), (w2, h2))

    pygame.draw.rect(self.verticalLinesSurface, c, self.vRect, self.lineThickness)
    pygame.draw.rect(self.horizLinesSurface,    c, self.hRect, self.lineThickness)

    self.updateDrawingCoords()

  ############################ updateDrawingCoords ############################

  def updateDrawingCoords(self):

    x1, y1 = self.topLeft
    x2, y2 = x1 + self.boxWidth - self.lineThickness, y1

    x3 = x1 + self.lineThickness
    y3 = y1 + self.boxHeight - self.lineThickness

    self.vCoord1 = self.topLeft
    self.vCoord2 = (x2, y2)

    self.hCoord1 = (x3, y1)
    self.hCoord2 = (x3, y3)

  ############################ draw ############################

  def draw(self, screen):

    if self.verbose:
      print("draw:")
      for c in [self.vCoord1, self.vCoord2, self.hCoord1, self.hCoord2]: print(c)

    # Draw the surface on the screen
    screen.blit(self.verticalLinesSurface, self.vCoord1)
    screen.blit(self.verticalLinesSurface, self.vCoord2) 
    screen.blit(self.horizLinesSurface,    self.hCoord1)
    screen.blit(self.horizLinesSurface,    self.hCoord2)

################## main ##################


def draw(): screen.clear(); eatb1.draw(screen)

print("main")
TL = (100, 100)
BR = (300, 300)

eatb1 = enoAnimTranspBox(topLeft=TL, bottomRight=BR)

### end ###
