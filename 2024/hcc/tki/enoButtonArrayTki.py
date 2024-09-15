# Button field array, with keystroke shortcuts, toggleable
# Brygg Ullmer, Clemson University
# Begun 2024-09-14

import tkinter as tk
import os
from functools import partial
  
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
  
  buttonNames     = None
  buttonKeyDict   = None
  buttonShortDict = None
  buttonLongDict  = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.loadYaml()
    self.buildUI()

  ################## error ##################

  def err(self, msg): print("enoButtonArrayTki error:", msg); traceback.print_exc()

  ################# load yaml ################# 

  def loadYaml(self):
    if self.yamlFieldDescriptorsFn is None:
      self.err("loadYaml: yamlFieldDescriptors filename not set"); return None

    if not(os.path.exists(self.yamlFieldDescriptorsFn):
      self.err("loadYaml: yamlFieldDescriptors filename reported not existing" + \
               self.yamlFieldDescriptorsFn); return None

    try:
      f = open(self.yamlFieldDescriptorsFn)
      self.yamlFieldDescriptorsD = yaml.safe_load(f)
      f.close()

      if 'themeFields' not in self.yamlFieldsDescriptorsD:
        self.err("loadYaml: themeFields expected but not found in YAML"); return None

      self.buttonNames     = []
      self.buttonKeyDict   = {}
      self.buttonShortDict = {}
      self.buttonLongDict  = {}

      for buttonHandle in self.buttonsD: #will be assiged to dictionary key, not full entry
        bd = self.buttonsD[buttonHandle]
        bkey, bshort, blong = bd['key'], bd['short'], bd['long']

        self.buttonNames.append(buttonHandle)
        buttonKeyDict[buttonHandle]   = bkey
        buttonShortDict[buttonHandle] = bshort
        buttonLongDict[buttonHandle]  = blong

    except:
      self.err("loadYaml error on loading and parsing); return None

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
      cb   = 
      self.buttonState[buttonName] = False #not activated
      self.buttonTk[buttonName]    = Button(text=bkey, command=cb)

  ############### button toggle callback ############### 
  
  def toggleCB(self, coord):
    if self.buttonState[coord]: 
      self.buttonState[coord] = False
      print("toggleCB on %s: off" % str(coord))


### end ###
