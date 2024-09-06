# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

import traceback
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

  animSrc, animDest = None, None
  animSrcDestDist   = None
  animSrcDestVect   = None

  animDuration = 0.5
  animActive   = 0
  animHandler  = None
  animProgress = 0    #ranges from 0=animSrc to 1=full progression to animDest

  verbose      = False
  bounce       = False # bounce between animSrc and animDest

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
    if self.animSrc is not None and self.animDest    is not None: self.startAnim()

  ####################### error message (redirectable) ####################

  def err(self, msg): print("enoAnimTranspBox:", str(msg))

  ############################ animation interpolation setup ############################
  
  def animInterpolateSetup():
    try:
      x1, y1 = self.animSrc
      x2, y2 = self.animDest
      dx, dy = x2-x1, y2-y1

      self.animSrcDestDist = math.dist(self.animSrc, self.animDest)
      self.animSrcDestVect = (dx, dy)
    except:
      self.err("animInterpolateSetup error:"); traceback.print_exc()
  
  ############################ animation interpolation ############################

  def animInterpolate():
    for i in [self.animSrcDestDist, animSrcDestVect]:
      if i is None: self.animInterpolateSetup() 

    if self.animProgress 

  ############################ build box ############################

  def buildBox(self):
eatb1 = enoAnimTranspBox(animSrc=aSrc, animDest=aDest, bounce=True)


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
TL1 = (100, 100)
BR1 = (300, 300)

TL2 = (10, 10)
BR2 = (20, 20)

aSrc, aDest = (TL1, BR1), (TL2, BR2)

#eatb1 = enoAnimTranspBox(topLeft=TL, bottomRight=BR)
eatb1 = enoAnimTranspBox(animSrc=aSrc, animDest=aDest, bounce=True)

### end ###
