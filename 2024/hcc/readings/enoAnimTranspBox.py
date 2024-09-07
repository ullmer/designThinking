# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

import sys
import pygame  
import traceback
from functools import partial

#WIDTH, HEIGHT = 800, 800

############################ enodia transparent surface cache ############################
### allows sharing between elements

class enoTranspSurfaceCache:

  transpRectSurfaceCache = None
  cacheCountCheck  = 0
  cacheCountFlush  = 20
  displayCacheHits = False

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.transpRectSurfaceCache = {}

  ###################### is transparent rect of specificed width & height cached ###################

  def isTRCached(self, x, y):  
    if self.displayCacheHits:
      self.cacheCountCheck += 1
      if self.cacheCountCheck % self.cacheCountFlush == 0: sys.stdout.flush()

    keyTuple = (int(x), int(y)) #... since interpolation may generate floats
    if self.transpRectSurfaceCache is not None and keyTuple in self.transpRectSurfaceCache: 
       if self.displayCacheHits: print(".", end=""); 
       return True

    if self.displayCacheHits: print("!", end="")
    return False

  ###################### is transparent rect of specificed width & height cached ###################

  def getTRCached(self, x, y):  
    keyTuple = (int(x), int(y)) #... since interpolation may generate floats

    if self.transpRectSurfaceCache is not None and keyTuple in self.transpRectSurfaceCache: 
       return self.transpRectSurfaceCache[keyTuple]

    return None

  ###################### is transparent rect of specificed width & height cached ###################

  def setTRCache(self, x, y, val):  
    keyTuple = (int(x), int(y)) #... since interpolation may generate floats

    if self.transpRectSurfaceCache is not None:
       self.transpRectSurfaceCache[keyTuple] = val

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
  animBRx, animBRy  = None, None
  animSrcDestDiffTL = None
  animSrcDestDiffBR = None

  eTranspSurfaceCache = None

  animDuration     = 2
  animTween        = 'accel_decel'
  animActive       = False
  animHandler      = None
  animProgress     = 0    #ranges from 0=animSrc to 1=full progression to animDest
  lastAnimProgress = None

  verbose      = False
  animBounce   = False # bounce between animSrc and animDest

  verticalLinesSurface = None
  horizLinesSurface    = None

  vCoord1, vCoord2 = None, None #cached coordinates for blitting operations
  hCoord1, hCoord2 = None, None
  vRect,   hRect   = None, None

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    if self.eTranspSurfaceCache is None: 
      self.eTranspSurfaceCache = enoTranspSurfaceCache()

    if None not in (self.topLeft, self.bottomRight): self.buildBox()
    if None not in (self.animSrc, self.animDest):    self.startAnim()

  ####################### error message (redirectable) ####################

  def err(self, msg): print("enoAnimTranspBox:", str(msg))

  ####################### transparent rect surface cache wrappers ####################

  def isTRCached(self, x, y):      return self.eTranspSurfaceCache.isTRCached(x, y)
  def getTRCached(self, x, y):     return self.eTranspSurfaceCache.getTRCached(x, y)
  def setTRCache(self, x, y, val): self.eTranspSurfaceCache.setTRCache(x, y, val)

  ############################ calculate 2D diff ############################
  
  def calc2dDiff(self, v1, v2):
    if self.verbose: print("calc2dDiff", v1, v2)

    x1, y1 = v1
    x2, y2 = v2
    dx, dy = x2-x1, y2-y1

    if self.verbose: print(dx, dy)
    return (dx, dy)

  ############################ start animation ############################
  
  def startAnim(self, targetInterpolationExtent=1):

    if self.verbose: print("startAnim", self.animSrc, self.animDest)

    self.animInterpolateSetup()
    self.animInterpolate()
    self.animActive = True

    tie = targetInterpolationExtent

    if self.animBounce:
      if tie==1: cb = partial(self.startAnim, 0)
      else:      cb = partial(self.startAnim, 1)

      animate(self, animProgress=tie, tween=self.animTween, duration=self.animDuration, on_finished=cb)
    else:
      animate(self, animProgress=tie, tween=self.animTween, duration=self.animDuration)

  ############################ animation interpolation setup ############################
  
  def animInterpolateSetup(self):
    try:
      animTL1, animBR1 = self.animSrc
      animTL2, animBR2 = self.animDest

      self.animSrcDestDiffTL         = self.calc2dDiff(animTL1, animTL2)
      self.animSrcDestDiffBR         = self.calc2dDiff(animBR1, animBR2)
      self.animTLx, self.animTLy     = animTL1
      self.animBRx, self.animBRy     = animBR1
      self.topLeft, self.bottomRight = animTL1, animBR1

      if self.verbose: print("animInterpolateSetup dtl dbr:", self.animSrcDestDiffTL, self.animSrcDestDiffBR)

      self.buildBox()

    except:
      self.err("animInterpolateSetup error:"); traceback.print_exc()
  
  ############################ animation interpolation ############################

  def animInterpolate(self):
    for el in [self.animSrcDestDiffTL, self.animSrcDestDiffBR]:
      if el is None: self.animInterpolateSetup() 

    try:
      x1, y1 = self.animSrcDestDiffTL
      x2, y2 = self.animTLx + x1 * self.animProgress, self.animTLy + y1 * self.animProgress
      self.topLeft = (x2, y2)

      x3, y3 = self.animSrcDestDiffBR
      x4, y4 = self.animBRx + x3 * self.animProgress, self.animBRy + y3 * self.animProgress
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

    if self.verbose: print("bb w2 h2:", w2, h2)

    c  = self.lineColor

    vWH = (w1, h1) #vertical   line width & height
    hWH = (w2, h2) #horizontal line width & height

    if self.isTRCached(w1, h1):  # especially in bounce scenario, prevent endless generation of new equiv surfaces
      self.verticalLinesSurface = self.getTRCached(w1, h1)

    else:
      self.verticalLinesSurface = pygame.Surface((w1,h1), pygame.SRCALPHA)
      self.vRect = Rect((0,0), (w1, h1))
      pygame.draw.rect(self.verticalLinesSurface, c, self.vRect, self.lineThickness)
      self.setTRCache(w1, h1, self.verticalLinesSurface)

    if self.isTRCached(w2, h2): 
      self.horizLinesSurface    = self.getTRCached(w2, h2)

    else: 
      self.horizLinesSurface    = pygame.Surface((w2,h2), pygame.SRCALPHA)
      self.hRect = Rect((0,0), (w2, h2))
      pygame.draw.rect(self.horizLinesSurface,    c, self.hRect, self.lineThickness)
      self.setTRCache(w2, h2, self.horizLinesSurface)

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

    if self.animActive and self.animProgress != self.lastAnimProgress:
      self.animInterpolate()
      self.calcWidthHeight()
      self.buildBox()

    try:
      # Draw the surface on the screen
      screen.blit(self.verticalLinesSurface, self.vCoord1)
      screen.blit(self.verticalLinesSurface, self.vCoord2) 
      screen.blit(self.horizLinesSurface,    self.hCoord1)
      screen.blit(self.horizLinesSurface,    self.hCoord2)
    except:
      self.err("draw error:"); traceback.print_exc()

### end ###
