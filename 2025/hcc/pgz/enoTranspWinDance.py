# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import pygame
from pygame._sdl2 import Window, Renderer
from enoWinMgr    import *

WIDTH, HEIGHT = 300, 300

##################### transparency 08 example #####################

class enoTranspWinDance:

  a1Fn          = "animist01a_100"
  subwinProxyFn = "one_red_pix"

  a1              = None
  winCoordProxies = None
  numSubwins      = 3

  pRenderers      = None
  pWindows        = None

  dur1, dur2      = 1.5, 4. #durations
  fuchsia         = (255, 0, 128)  # Transparency key color

  justBeginning   = True
  animPhase1      = True
  pos1, pos2      = (0, 0), (500, 500)

  winDimension    = (250, 250)
  winCoords       = [(0, 0), (0, 300), (0, 600)]
  ewm             = None #enoWinMgr
  tween           = 'accel_decel'

  runDefaultGlyphAnimations = True
  runDefaultWinAnimations   = True

  ############# constructor #############

  def __init__(self, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.a1 = Actor(self.a1Fn)
    self.winCoordProxies = {}
    self.pRenderers      = {}
    self.pWindows        = {}

    for i in range(self.numSubwins): self.winCoordProxies[i] = Actor(self.subwinProxyFn)

  ##################### get window coordinate (actor) proxies #####################
 
  def getWinCoordProxies(self, whichWinId):
    if self.winCoordProxies is None or whichWinId not in self.winCoordProxies:
      print("enoTranspWinDance getWinCoordProxies: issues noted, ignoring"); return

    result = self.winCoordProxies[whichWinId]
    return result

  ##################### first frame invocations #####################
  
  def firstFrame(self):

    if self.ewm is None: print("exTransp08 firstFrame: ewm is not initialized!"); return

    wh, ww = self.winDimension
    
    self.pWindows[0] = self.ewm.getWindow()
    n                = self.numSubwins - 1

    for i in [1, n]: 
      # dictionaries work for storing window handle, but lists do not, because of pygame_sdl2's "deep copy" limitations
      self.pWindows[i]   = self.ewm.newWindow("win" + str(i), ww, wh) 

      self.pRenderers[i] = Renderer(self.pWindows[i])
  
    #pWindows = [window1] #this "deepcopy" is sufficient to cause a segfault; long, long sigh
  
    for i in range(self.numSubwins):
      x, y                        = self.winCoords[i]
      self.winCoordProxies[i].pos = self.winCoords[i]
      self.ewm.moveWindow(self.pWindows[i], x, y)
  
    self.ewm.transpWinSetup(screen, self.fuchsia, WIDTH, HEIGHT)        #set up transparent window ~chromakey
    #transpWinSetup(pRenderers[1], fuchsia, WIDTH, HEIGHT, pWindows[1]) #set up transparent window ~chromakey
  
    if self.runDefaultGlyphAnimations:
      animate(self.a1, pos=self.pos2, tween=self.tween, duration=self.dur1, on_finished=self.animTransition1)

    if self.runDefaultWinAnimations:
      w1 = self.winCoordProxies[0]
      animate(w1, pos=(800,800), tween=self.tween, duration=self.dur2)
  
  ##################### animation transition #####################
  
  def animTransition1(self):
    if self.animPhase1:
      self.animPhase1 = False; animate(self.a1, pos=self.pos1, tween=self.tween, duration=self.dur1, on_finished=self.animTransition1)
    else:
      self.animPhase1 = True;  animate(self.a1, pos=self.pos2, tween=self.tween, duration=self.dur1, on_finished=self.animTransition1)
  
  ##################### draw #####################
  
  def draw(self):
    if self.justBeginning: self.firstFrame(); self.justBeginning=False
  
    for i in range(self.numSubwins):
      wp = self.winCoordProxies[i]
      x, y = wp.pos
      self.ewm.moveWindowById(i, x, y, self.pWindows)
  
    n = self.numSubwins - 1
    for i in [1,n]:
      self.pRenderers[i].clear()
      self.pRenderers[i].present()

    screen.fill(self.fuchsia)  # Transparent background ~chromakey
    self.a1.draw()
  
##################### main #####################

if __name__ == "__main__":
  
  ewm = enoWinMgr()
  et8 = exTransp08(ewm=ewm)

  def draw(): et8.draw()
  
### end ###

