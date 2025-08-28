# Enodia Button-like elements -- sometimes backed by Pygame Zero, 
#  sometimes by physical buttons, sometimes by other variants.
# First approximation, albeit too specific to Pygame Zero
# Brygg Ullmer, Clemson University
# Begun    2022-02-22
# Revamped 2024-08

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButton import *
import traceback

##################### enodia button array #####################

class enoButtonArray:
  basePos    = (0,0)
  buttonDim  = (100, 30)
  dx, dy     = 190, 0

  labelArray      = None #originally named textArray, but decided (e.g.) ints equally interesting
  buttonArray     = None
  imageFns        = None
  lastSelected    = None
  angle           = 0
  requestAnim     = False
  motionAnimTween = None
  animDuration    = 1.
  callbackList    = None

  maxOneToggledOn    = False
  currentToggleState = None

  drawText  = True
  drawImg   = False
  drawAdapt = True   # if True, will render text and/or image only when specified
  verbose   = False

  bgcolor1  = (30, 30, 30)
  bgcolor2  = (80, 10, 10)
  fgcolor   = "#bbbbbb"
  alpha     = .8
  fontSize  = 36
  angle     = 0

  expandContractState = 1   # 1 if expanded or animating in that direction; 0 if contracted
  buttonRetractedPos  = None # buttons in contracted position, optionally (esp. if animated)
  buttonUnfurledPos   = None # buttons in unfurled position, optionally (esp. if animated)
  label2Button        = None

  ############# error message #############

  def err(self, msg): print("enoButtonArray error:" + msg)
  def msg(self, msg): print("enoButtonArray msg:  " + msg)

  ############# constructor #############

  def __init__(self, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.buttonArray  = []
    self.callbackList = []

    self.buttonRetractedPos = {}
    self.buttonUnfurledPos  = {}
    self.label2Button       = {}
    self.currentToggleState = {}

    idx = 0

    bpx, bpy  = self.basePos
    ifn       = None         #image filename
    postAnimP = None

    for label in self.labelArray:
      if self.imageFns is not None: ifn = self.imageFns[idx]

      p1 = (bpx+idx*self.dx, bpy+idx*self.dy)

      if self.requestAnim: # make distinction between (shared) base position and post-animation pos
        baseP     = (bpx, bpy)
        postAnimP = p1

        self.buttonRetractedPos[text] = baseP
        self.buttonUnfurledPos[text]  = postAnimP

      else: baseP = p1         # no distinction

      but = enoButton(buttonLabel = label, basePos = baseP, postAnimPos = postAnimP, 
                      buttonDim   = self.buttonDim,   angle = self.angle,         imageFn = ifn,
                      drawText    = self.drawText,  drawImg = self.drawImg,     drawAdapt = self.drawAdapt,
                      bgcolor1    = self.bgcolor1, bgcolor2 = self.bgcolor2,      fgcolor = self.fgcolor,
                      alpha       = self.alpha,    fontSize = self.fontSize, animDuration = self.animDuration,
                      requestAnim = self.requestAnim,                     motionAnimTween = self.motionAnimTween)

      self.label2Button[label] = but
      self.buttonArray.append(but); idx += 1

  activAnim   = None

  ############# get number of buttons #############

  def getNumButtons(self):
    if self.buttonArray is None: return 0
    return len(self.buttonArray)

  ############# get button by index #############

  def getButtonIdx(self, idx):
    nb = self.getNumButtons()
    if idx >= 0 and idx < nb: return self.buttonArray[idx]
    return None #error

  ############# tobble button by index #############

  def toggleButtonIdx(self, idx):
    if self.verbose: self.msg("toggleButtonIdx called")

    b = self.getButtonIdx(idx)
    if b is None: self.err("toggleButtonIdx fails: " + str(idx)); return
    b.toggle()

    if self.maxOneToggledOn and b.isToggledOn(): # we will clear the others, albeit hackily
      nb = self.getNumButtons()
      for i in range(nb):
        if i == idx: continue #we've already toggled that

        b = self.getButtonIdx(i)
        if b is None: self.err("toggleButtonIdx fails in clearing button idx " + str(idx)); return

        if b.isToggledOn(): b.toggle() 

  ############# addCallback #############

  def addCallback(self, callback):
    if self.callbackList is None: err("addCallback: callback list not yet created!"); return

    self.callbackList.append(callback)

  ############# clear/reset callback #############

  def clearCallbacks(self): self.callbackList = []

  ############# invokeCallbacks #############

  def invokeCallbacks(self, buttonName):
    if self.callbackList is None: err("invokeCallback: callback list not yet created!"); return

    for cb in self.callbackList: 
      try:     cb(buttonName)
      except:  self.err("invokeCallbacks: error received"); traceback.print_exc(); return None

  ############# expand/contract #############

  def expandContract(self):
    for text in self.labelArray:
      but = self.label2Button[text] 

      if self.expandContractState == 1:   # 1 if expanded or animating in that direction; 0 if contracted
        targetPos = self.buttonRetractedPos[text] 
      else:
        targetPos = self.buttonUnfurledPos[text] 

      but.animate(targetPos)

    if self.expandContractState == 1: self.expandContractState = 0
    else:                             self.expandContractState = 1

  ############# pgzero draw #############

  def draw(self, screen): 
    for but in self.buttonArray: but.draw(screen)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    for but in self.buttonArray:
      if but.on_mouse_down(pos):
        if self.lastSelected is not None: self.lastSelected.toggle()
        self.lastSelected = but
        try: self.invokeCallbacks(but.buttonLabel)
        except: self.err("on_mouse_down error:"); traceback.print_exc(); return None

### end ###
