# Enodia Button-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# Brygg Ullmer, Clemson University
# Begun 2022-02-22

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

import yaml
from pygame import Rect
from pgzero.builtins import Actor, animate, keyboard
#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

##################### pygamezero button #####################

class enoActor:
  basePos    = (0,0)
  buttonDim  = (100, 30)
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

  toggleMode  = True
  toggleState = False

  ############# constructor #############

  def __init__(self, imgFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    #self.buttonText = buttonText
    #self.buttonRect = Rect(self.basePos, self.buttonDim)
    self.actor = Actor(imgFn)
    self.actor.pos = self.basePos

  ############# pgzero draw #############

  def getAbbrev(self):
    return self.abbrev

  ############# pgzero draw #############

  #def draw(self, screen):
  def draw(self):
    return self.actor.draw()

    if self.toggleMode and self.toggleState: bgcolor = self.bgcolor2
    else:                                    bgcolor = self.bgcolor1

    screen.draw.filled_rect(self.buttonRect, bgcolor)
    #screen.draw.text(self.buttonText, self.basePos, align="center",
    x0, y0 = self.basePos; dx, dy = self.buttonDim; cx=x0+dx/2; cy = y0+dy/2
    screen.draw.text(self.buttonText, centerx=cx, centery=cy, align="center",
                     fontsize=self.fontSize, 
                     color=self.fgcolor, alpha=self.alpha)

  ############# nudge #############

  def nudgeY(self, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.buttonDim)

  def nudgeXY(self, dx, dy): 
    bpx, bpy = self.basePos
    self.basePos = (bpx+dx, bpy+dy)
    self.buttonRect = Rect(self.basePos, self.buttonDim)

  ######################### on_mouse_down #########################

  def toggle(self):
    if self.toggleState: self.toggleState = False
    else:                self.toggleState = True

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    if self.actor.collidepoint(pos): 
      if self.abbrev is not None: print(self.abbrev, "pressed1")
      else:                       print(self.buttonText, "pressed2")
      self.toggle()
      return True

    return False

##################### pygamezero button #####################

class enoActorArray:
  basePos    = (0,0) #30, 327
  buttonDim  = (100, 30)
  #dx, dy     = 190, 0
  dx, dy     = 55, 0

  textArray    = None
  buttonArray  = []
  lastSelected = None

  yamlFn, yamlF, yamlD = [None] * 3

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.yamlFn = yamlFn
    self.yamlF  = open(yamlFn, 'r+t')
    self.yamlD  = yaml.safe_load(self.yamlF)

    self.textArray  = buttonTextList
    self.buttonArray = []

    idx = 0

    bpx, bpy = self.basePos
    for text in self.textArray:
      but = enoActor(text, basePos = (bpx+idx*self.dx, bpy+idx*self.dy),
                      buttonDim = self.buttonDim)
      self.buttonArray.append(but); idx += 1

  ############# pgzero draw #############

  def draw(self, screen): 
    for but in self.buttonArray: but.draw(screen)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for but in self.buttonArray:
      if but.on_mouse_down(pos):
        if self.lastSelected is not None: self.lastSelected.toggle()
        self.lastSelected = but


### end ###
