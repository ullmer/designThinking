# Button field array, with keystroke shortcuts, toggleable
# Brygg Ullmer, Clemson University
# Begun 2024-09-14

import tkinter as tk
import os

class enoButtonArrayTki:
  yamlFieldDescriptorsFn = 'themeFields.yaml'
  yamlFieldDescriptorsD  = None

  root         = None
  buttonState  = {}
  buttonTk     = {}
  hideTitlebar = False

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

    self.buildUI()

  ################## error ##################

  def err(self, msg): print("enoButtonArrayTki error:", msg); traceback.print_exc()

  ################# load yaml ################# 

  def loadYaml(self):
    if self.yamlFieldDescriptorsFn is None:
      self.err("loadYaml error: yamlFieldDescriptors filename not set"); return None

    if not(os.path.exists(self.yamlFieldDescriptorsFn):
      self.err("loadYaml error: yamlFieldDescriptors filename reported not existing" + \
               self.yamlFieldDescriptorsFn); return None

    try:
      f = open(self.yamlFieldDescriptorsFn)
      self.yamlFieldDescriptorsD = yaml.safe_load(f)
      f.close()
    except:
      self.err("loadYaml error on loading and parsing); return None

    return True

  #################### build user interface ####################

  def buildUI(self):
    if self.root is None:
      self.err("buildUI error: root must be assigned, but is not"); return None
  
    self.buttonState = {}
    self.buttonTk    = {}

  ############### button toggle callback ############### 
  
  def toggleCB(self, coord):
    if self.buttonState[coord]: 
      self.buttonState[coord] = False
      print("toggleCB on %s: off" % str(coord))


### end ###
