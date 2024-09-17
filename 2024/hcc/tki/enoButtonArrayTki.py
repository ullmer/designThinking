# Button field array, with keystroke shortcuts, toggleable
# Brygg Ullmer, Clemson University
# Begun 2024-09-14

import tkinter as tk
import os
import traceback
from tkinter.font import *
from functools    import partial
  
############# Enodia Button Array: tkinter #############

class enoButtonArrayTki:
  yamlFieldDescriptorsFn = 'themeFields.yaml'
  yamlFieldDescriptorsD  = None

  root         = None
  buttonD      = None #buttons data
  buttonState  = None
  buttonTk     = None
  buttonsFrame = None
  buttonSide   = tk.LEFT
  verbose      = False
  
  buttonNames     = None
  buttonKeyDict   = None
  buttonShortDict = None
  buttonLongDict  = None

  whichButtonsToggledOn = None

  bgColor1 = '#ddd'
  bgColor2 = '#e77'

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.loadYaml()
    self.buildUI()

  ################## error ##################

  def err(self, msg): print("enoButtonArrayTki error:", msg); traceback.print_exc()
  def msg(self, msg): print("enoButtonArrayTki msg:", msg)

  ################# load yaml ################# 

  def loadYaml(self):
    if self.yamlFieldDescriptorsFn is None:
      self.err("loadYaml: yamlFieldDescriptors filename not set"); return None

    if not(os.path.exists(self.yamlFieldDescriptorsFn)): 
      self.err("loadYaml: yamlFieldDescriptors filename reported not existing" + \
               self.yamlFieldDescriptorsFn); return None

    try:
      f = open(self.yamlFieldDescriptorsFn)
      self.yamlFieldDescriptorsD = yaml.safe_load(f)
      f.close()

      if 'themeFields' not in self.yamlFieldsDescriptorsD:
        self.err("loadYaml: themeFields expected but not found in YAML"); return None

      self.buttonNames           = []
      self.buttonKeyDict         = {}
      self.buttonShortDict       = {}
      self.buttonLongDict        = {}
      self.whichButtonsToggledOn = {}

      for buttonHandle in self.buttonsD: #will be assiged to dictionary key, not full entry
        bd = self.buttonsD[buttonHandle]
        bkey, bshort, blong = bd['key'], bd['short'], bd['long']

        self.buttonNames.append(buttonHandle)
        buttonKeyDict[buttonHandle]   = bkey
        buttonShortDict[buttonHandle] = bshort
        buttonLongDict[buttonHandle]  = blong

    except:
      self.err("loadYaml error on loading and parsing"); return None

    return True

  #################### build user interface ####################

  def buildUI(self):
    if self.root is None:
      self.err("buildUI error: root must be assigned, but is not"); return None

    if self.buttonNames is None or len(buttonNames) < 1: 
      self.err("buttonUI: buttonNames not as expected"); return

    buttonsFrame = Frame(self.root)

    self.buttonState = {}
    self.buttonTk    = {}

    for buttonName in buttonNames:
      bkey = self.buttonKeyDict[buttonName]
      cb   = partial(self.toggleCb, buttonName)
      self.buttonState[buttonName] = False #not activated
      self.buttonTk[buttonName]    = Button(text=bkey, command=cb)

    buttonsFrame.bind("<KeyPress>", self.onKeyDown)

  ############### on key down ############### 
  
  def onKeyDown(self, event): self.msg("key pressed: " + str(event))

  ############### button toggle callback ############### 

  def toggleCB(self, buttonName):
    if self.buttonState[buttonName]: 
      self.buttonState[buttonName] = False
      if self.verbose: print("toggleCB on %s: off" % str(coord))

############# button highlight manager; may merit from fusion with above ############# 

class buttonHighlightMgr: 
  handle2button, handle2cb = {}, {}
  currentHandle = None
  bg1, bg2 = '#444', '#ccc' #bg1 = normal background color; bg2, highlighted

  def err(self, msg): print("buttonHighlightMgr error:", msg); traceback.print_exc()

  def registerButtonHandle(self, handleStr, button):       self.handle2button[handleStr] = button
  def registerHandleCb(self,     handleStr, cb):           self.handle2cb[handleStr]     = cb

  def registerButtonHandleCb(self, handleStr, button, cb): 
     self.registerHandleCb(handleStr, cb);  self.registerButtonHandle(handleStr, button)

  def clearButtonVisuals(self):
    for h in self.handle2button(): b = self.handle2button[h]; b.bg=self.bg1

  def highlightButtonVisual(self, h):
    b = self.handle2button[h]; b.bg=self.bg2

  def triggerButtonCb(self, h):
    cb = self.handle2cb[h]
    try:    cb()
    except: self.err("triggerButtonCb " + str(h))

  def triggerHighlightButton(self, h):   #both highlight the button, and invoke it's callback
    self.highlightButtonVisual(h)
    self.triggerButtonCb(h)

  def cycleNextButton(self):                         
     h=self.getNextHandle()
     self.clearButtonsVisuals()
     self.highlightButtonVisual(h)
     self.triggerButtonCb(h)

### end ###
