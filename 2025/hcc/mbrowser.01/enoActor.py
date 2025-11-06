# Enodia Button-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# Brygg Ullmer, Clemson University
# Begun 2022-02-22

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import yaml
import pygame
#import pgzero #scaling seems to depend on a newer version of pgzero
# than within pypi ca. 2025-11; could add dependencies here to check

from pygame import Rect
from pgzero.builtins import Actor, animate, keyboard

#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

##################### enodia actor #####################

class EnoActor:
  name       = None
  pos        = (0,0)
  actorDim   = (100, 30)
  buttonRect = None
  buttonText = "actor"
  bgcolor1   = (0, 0, 130)
  bgcolor2   = (50, 50, 250)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 36
  imgFn      = None
  actor      = None # for image/sprite
  abbrev     = None # name/identity/handle
  scale      = None       # None -> don't rescale

  origW,     origH = None, None # "original" width and height, toward scaling
  scaledW, scaledH = None, None # "scaled" width and height

  toggleMode         = True
  toggleOnFingerDown = False  #may be either redundant or contradictory wrt toggleMode
  toggleState = False
  verbose     = False

  ############# constructor #############

  def __init__(self, imgFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.actor = Actor(imgFn)
    a          = self.actor

    if 'topleft' in kwargs:     tl = kwargs['topleft'];     a.topleft     = tl
    if 'midleft' in kwargs:     ml = kwargs['midleft'];     a.midleft     = ml
    if 'pos'     in kwargs:     p  = kwargs['pos'];         a.pos         = p
    if 'center'  in kwargs:     c  = kwargs['center'];      a.center      = c
    if 'bottomleft' in kwargs:  bl = kwargs['bottomleft'];  a.bottomleft  = bl
    if 'bottomright' in kwargs: bl = kwargs['bottomright']; a.bottomright = bl

  ############# set position #############

  def setPos(self, newPos):
    self.pos       = newPos
    self.actor.pos = newPos

  ############# get abbreviation #############

  def getAbbrev(self):
    return self.abbrev

  ############# scale #############

  def scaleV(self, scaleVal):  #scale by a value
    # https://stackoverflow.com/questions/74817115/resizing-a-sprite-with-pygame-zero

    if self.actor is None: self.err("scaleV: actor is not yet assigned! ignoring"); return

    if self.origW is None or self.origH is None:
      self.origW = self.actor.width
      self.origH = self.actor.height

    try:
      self.scaledW = self.origW * scaleVal
      self.scaledH = self.origH * scaleVal
    except:
      self.err("scaleV: error in scaling with arguments", scaleVal, self.origW, self.origH); return

    #s = self.actor._surf
    #s = self.actor._surface_cache
    s = self.actor._orig_surf

    #self.actor._surf = pygame.transform.scale(s, (self.scaledW, self.scaledH))
    self.actor._orig_surf = pygame.transform.scale(s, (self.scaledW, self.scaledH))

  ############# pgzero draw #############

  def draw(self, screen):
    return self.actor.draw()

    #if self.toggleMode and self.toggleState: bgcolor = self.bgcolor2
    #else:                                    bgcolor = self.bgcolor1
    #
    #screen.draw.filled_rect(self.buttonRect, bgcolor)
    #x0, y0 = self.pos; dx, dy = self.actorDim; cx=x0+dx/2; cy = y0+dy/2
    #screen.draw.text(self.buttonText, centerx=cx, centery=cy, align="center",
    #                 fontsize=self.fontSize, 
    #                 color=self.fgcolor, alpha=self.alpha)

  ############# nudge #############

  def nudgeY(self, dy): 
    bpx, bpy = self.pos
    self.pos = (bpx, bpy+dy)
    self.buttonRect = Rect(self.pos, self.actorDim)

  def nudgeXY(self, dx, dy): 
    bpx, bpy = self.pos
    self.pos = (bpx+dx, bpy+dy)
    self.buttonRect = Rect(self.pos, self.actorDim)

  ######################### on_mouse_down #########################

  def toggle(self):
    if self.toggleState: self.toggleState = False
    else:                self.toggleState = True

  ######################### on_mouse_down #########################

  def on_finger_down(self, finger_id, x, y):
    if self.verbose: print("enoActor ofd:", x, y)
    if self.actor.collidepoint((x,y)): 
      if self.abbrev is not None and self.verbose: print(self.abbrev, "pressed1")
      elif self.verbose:                           print(self.buttonText, "pressed2")

      if self.toggleOnFingerDown: self.toggle()
      return True

    return False

############################################################### 
##################### enodia actor array #####################
## fixed, regular grid

class EnoActorArray:
  pos    = (0,0) #30, 327
  actorDim  = (100, 30)
  #dx, dy     = 190, 0
  dx, dy     = 55, 0

  textArray    = None
  actorArray   = None
  lastSelected = None

  yamlFn, yamlF, yamlD = [None] * 3

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.actorArray = []
    self.parseYaml(yamlFn)

    idx = 0

    bpx, bpy = self.pos
    for text in self.textArray:
      but = EnoActor(text, pos = (bpx+idx*self.dx, bpy+idx*self.dy),
                      actorDim = self.actorDim)
      self.actorArray.append(but); idx += 1

  ############# yaml warning #############

  def yamlWarn(self, message): 
    print("enoActor parseYaml warning: ", message)

  ############# parse yaml #############

  def parseYaml(self, yamlFn): 

    self.yamlFn = yamlFn
    self.yamlF  = open(yamlFn, 'r+t')
    yd = self.yamlD  = yaml.safe_load(self.yamlF)

    if 'panel' not in yd: self.yamlWarn("panel not present"); return
    ydp = yd['panel']

    if 'buttons' not in ydp: self.yamlWarn("panel:buttons not present"); return
    ydpb = ydp['buttons']

    self.yamlWarn(str(ydpb))

  ############# pgzero draw #############

  def draw(self, screen): 
    for actor in self.actorArray: actor.draw(screen)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for actor in self.actorArray:
      if actor.on_mouse_down(pos):
        if self.lastSelected is not None: self.lastSelected.toggle()
        self.lastSelected = actor

############################################################### 
##################### enodia actor ensemble ###################
## plurality, but not of regular structure

class EnoActorEnsemble:
  actorList     = None
  lastSelected  = None
  actorNameDict = None

  #actorAnchor   = 'topleft' #could also later be pos, center, etc.

  fingerIdActorAssocDict = None   #dictionary of associations between finger IDs and actors
  toggleOnFingerDown     = False  #may be either redundant or contradictory with toggleMode

  ############# constructor #############

  def __init__(self, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.actorList     = []
    self.actorNameDict = {}

    self.fingerIdActorAssocDict = {}

  ############# add actor #############

  def addActor(self, actorName, imgFn, **kwargs): 
    a = None 

    if 'topleft' in kwargs: tl = kwargs['topleft']; a = EnoActor(imgFn, topleft=tl)
    if 'midleft' in kwargs: ml = kwargs['midleft']; a = EnoActor(imgFn, midleft=ml)
    if 'pos'     in kwargs: p  = kwargs['pos'];     a = EnoActor(imgFn, pos=p)
    if 'center'  in kwargs: c  = kwargs['center'];  a = EnoActor(imgFn, center=c)

    if 'bottomleft' in kwargs: bl = kwargs['bottomleft']; a = enoActor(imgFn, bottomleft=bl)

    a.verbose = self.verbose

    self.actorList.append(a)
    self.actorNameDict[actorName] = a
    return a
  
  ############# get actor #############

  def getActor(self, actorName):

    if actorName not in self.actorNameDict:
      self.err("getActor: actorName" + actorName + "not known!  Ignoring"); return None

    return self.actorNameDict[actorName]

  ############# pgzero draw #############

  def draw(self, screen): 
    for actor in self.actorList: actor.draw(screen)

  ######### get list of actors with active finger ID associations ("currently touched") ######

  def getFingerIdActorList(self): return list(self.fingerIdActorAssocDict.keys())

  ######################### on_mouse_down #########################

  def on_finger_down(self, finger_id, x, y):
    if self.verbose: print("enoActorEnsemble on_finger_down")

    for actor in self.actorList:
      if actor.on_finger_down(finger_id, x, y):
        if self.lastSelected is not None and self.toggleOnFingerDown: self.lastSelected.toggle()
        self.lastSelected                      = actor
        self.fingerIdActorAssocDict[finger_id] = actor
        return actor

    return None #don't seem to be touching any actors

### end ###
