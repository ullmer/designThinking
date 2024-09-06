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
  animTLx, animTLy  = None, None
  animSrcDestDiffTL = None
  animSrcDestDiffBR = None

  animDuration = 0.5
  animTween    = 'accel_decel'
  animActive   = False
  animHandler  = None
  animProgress = 0    #ranges from 0=animSrc to 1=full progression to animDest

  transpRectSurfaceCache = None

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

    self.transpRectSurfaceCache = {}

    if self.topLeft is not None and self.bottomRight is not None: self.buildBox()
    if self.animSrc is not None and self.animDest    is not None: self.startAnim()

  ####################### error message (redirectable) ####################

  def err(self, msg): print("enoAnimTranspBox:", str(msg))

  ###################### is transparent rect of specificed width & height cached ###################

  def isTRCached(self, elWH):  
    if self.transpRectSurfaceCache is not None and elWH in self.transpRectSurfaceCache: return True
    return False

  ############################ animation interpolation setup ############################
  
  def calc2dDiff(self, v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    dx, dy = x2-x1, y2-y1
    return (dx, dy)

  ############################ start animation ############################
  
  def startAnim(self):
    self.animInterpolateSetup()
    self.animInterpolate()

  ############################ animation interpolation setup ############################
  
  def animInterpolateSetup():
    try:
      animTL1, animBR1 = self.animSrc
      animTL2, animBR2 = self.animDest

      self.animSrcDestDiffTL     = self.calc2dDiff(animTL1, animTL2)
      self.animSrcDestDiffBR     = self.calc2dDiff(animBR1, animBR2)
      self.animTLx, self.animTLy = animTL1

    except:
      self.err("animInterpolateSetup error:"); traceback.print_exc()
  
  ############################ animation interpolation ############################

  def animInterpolate():
    for el in [self.animSrcDestDiffTL, animSrcDestDiffBR]:
      if el is None: self.animInterpolateSetup() 

    try:
      x1, y1 = self.animSrcDestDiffTL
      x2, y2 = x1 + self.animTLx * self.animProgress, y1 + self.animTLy * self.animProgress
      self.topLeft = (x2, y2)

      x3, y3 = self.animSrcDestDiffBR
      x4, y4 = x3 + self.animBRx * self.animProgress, y3 + self.animBRy * self.animProgress
      self.bottomRight = (x4, y4)

      self.calcWidthHeight()
      self.buildBox()

    except:
      self.err("animInterpolate error:"); traceback.print_exc()

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

    vWH = (w1, h1) #vertical   line width & height
    hWH = (w2, h2) #horizontal line width & height

    if self.isTRCached(vWH):  # especially in bounce scenario, prevent endless generation of new equiv surfaces
      self.verticalLinesSurface = self.transpRectSurfaceCache[vWH]

    else:
      self.verticalLinesSurface = pygame.Surface((w1,h1), pygame.SRCALPHA)
      self.vRect = Rect((0,0), (w1, h1))
      pygame.draw.rect(self.verticalLinesSurface, c, self.vRect, self.lineThickness)
      self.transpRectSurfaceCache[vWH] = self.verticalLinesSurface

    if self.isTRCached(hWH): 
      self.horizLinesSurface    = self.transpRectSurfaceCache[hWH]

    else: 
      self.horizLinesSurface    = pygame.Surface((w2,h2), pygame.SRCALPHA)
      self.hRect = Rect((0,0), (w2, h2))
      pygame.draw.rect(self.horizLinesSurface,    c, self.hRect, self.lineThickness)
      self.transpRectSurfaceCache[hWH] = self.horizLinesSurface

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

eatb1 = enoAnimTranspBox(topLeft=TL1, bottomRight=BR1)
#eatb1 = enoAnimTranspBox(animSrc=aSrc, animDest=aDest, bounce=True)

### end ###
