# Enodia Button-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# First approximation, albeit too specific to Pygame Zero
# Brygg Ullmer, Clemson University
# Begun    2022-02-22
# Revamped 2024-08

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from pygame import Rect

##################### pygamezero button #####################

class enoButton:
  basePos     = (0,0)

  postAnimPos = None
  activAnim   = None
  animDuration = 1.
  isAnimActive = False

  buttonDim  = (100, 30)
  buttonRect  = None
  buttonLabel = None
  actor       = None
  imageFn     = None #image filename, relative to PGZ's "images/" directory expectations; lower-case only
  selectImgFn = None #   selected image filename
  deactImgFn  = None #deactivated image filename
  #bgcolor1    = (0, 0, 130)
  #bgcolor2    = (50, 50, 250)
  bgcolor1    = (30, 30, 30)
  bgcolor2    = (80, 10, 10)
  fgcolor     = "#bbbbbb"
  alpha       = .8
  fontSize    = 36
  angle       = 0

  drawText    = True
  drawImg     = False
  drawAdapt   = True   # if True, will render text and/or image only when specified

  verbose     = False
  toggleMode  = True
  toggleState = False
  rectCenter  = None
  requestAnim = False
  motionAnimTween = None

  callbackList    = None

  ############# constructor #############

  def __init__(self, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.callbackList = []

    bpx,  bpy  = self.basePos
    bdx,  bdy  = self.buttonDim
    bdx2, bdy2 = bdx/2, bdy/2

    self.rectCenter = (bpx-bdx2, bpy-bdy2)
    self.buttonRect = Rect(self.rectCenter, self.buttonDim)

    if self.imageFn is not None:
      self.actor     = Actor(self.imageFn)
      self.actor.pos = self.basePos
      if self.verbose: print("button" + str(self.buttonLabel) + ": pos" + str(self.actor.pos))

    if self.requestAnim: self.launchAnim()

  ############# error message #############

  def err(self, msg): print("enoButton error:" + msg)
  def msg(self, msg): print("enoButton msg:  " + msg)

  ############# is toggled on #############

  def isToggledOn(self): 
    if self.toggleState: return True
    return False 

  ############# postAnimCb #############

  def postAnimCb(self):

    self.isAnimActive = False
    self.basePos      = self.postAnimPos

    bpx,  bpy  = self.basePos
    bdx,  bdy  = self.buttonDim
    bdx2, bdy2 = bdx/2, bdy/2

    self.rectCenter = (bpx-bdx2, bpy-bdy2)
    self.buttonRect = Rect(self.rectCenter, self.buttonDim)

  ############# clear/remove callbacks #############

  def clearCallbacks(self): self.callbackList = []

  ############# addCallback #############

  def addCallback(self, callback):
    if self.callbackList is None: 
      self.err("addCallback: callback list not yet created!"); return

    self.callbackList.append(callback)

  ############# invokeCallbacks #############

  def invokeCallbacks(self):
    if self.callbackList is None: 
      self.err("invokeCallback: callback list not yet created!"); return

    for cb in self.callbackList: 
      try:     cb()
      except:  self.err("invokeCallbacks: error received"); traceback.print_exc(); return None

  ############# launchAnim #############

  def launchAnim(self):
    if self.motionAnimTween is None: 
      self.err("launchAnim called, but motion animation tween is not selected"); return

    if self.verbose: print("launchAnim:" + str (self.postAnimPos))

    if self.actor is not None: self.animate(self.postAnimPos)

  ############# animate #############

  def animate(self, postAnimPos):
    self.isAnimActive = True
    self.activAnim   = animate(self.actor, pos=postAnimPos, duration=self.animDuration, tween=self.motionAnimTween,
                               on_finished=self.postAnimCb)
    self.postAnimPos = postAnimPos
    #self.postAnimCb()

  ############# draw #############

  def draw(self, screen):
    if self.toggleMode and self.toggleState: bgcolor = self.bgcolor2
    else:                                    bgcolor = self.bgcolor1

    if self.isAnimActive is False: 
      screen.draw.filled_rect(self.buttonRect, bgcolor)

    #x0, y0 = self.basePos; dx, dy = self.buttonDim; cx=x0+dx/2; cy = y0+dy/2
    x0, y0 = self.basePos; dx, dy = self.buttonDim; cx, cy = x0, y0

    labelText = str(self.buttonLabel)
    lbl = len(labelText)

    if (self.drawText or (self.drawAdapt and self.imageFn is None)) and lbl > 0:
      screen.draw.text(labelText, centerx=cx, centery=cy, align="center",
                       fontsize=self.fontSize, color=self.fgcolor, 
                       alpha=self.alpha, angle=self.angle)

    if (self.drawImg or self.drawAdapt) and self.imageFn is not None and len(self.imageFn)>0:
      if self.actor is not None:
        self.actor.draw()
      #else:
      #  if self.imageFn is not None and len(self.imageFn) > 0:
      #    self.actor     = Actor(self.imageFn)
      #    self.actor.pos = self.basePos
      #    self.actor.draw()

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
    if self.verbose:     self.msg("toggle called")
    if self.toggleState: self.toggleState = False
    else:                self.toggleState = True; self.invokeCallbacks()

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    if self.buttonRect.collidepoint(pos) or \
       (self.actor is not None and self.actor.collidepoint(pos)):
      print(str(self.buttonLabel), "pressed")
      self.toggle()
      return True

    return False

### end ###
