# Button field array, with keystroke shortcuts, toggleable
# Brygg Ullmer, Clemson University
# Begun 2024-09-14

import tkinter as tk

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

  #################### build user interface ####################

  def buildUI(self):
  
    self.root = tk.Tk()

    #self.root.title("Interactive grid example")
    #self.root.geometry(self.windowGeometry)

    if self.hideTitlebar: self.root.overrideredirect(1) #hide window decorations ~= titlebar
  
    self.buttonState = {}
    self.buttonTk    = {}

  ############### button toggle callback ############### 
  
  def toggleCB(self, coord):
    if self.buttonState[coord]: 
      self.buttonState[coord] = False
      print("toggleCB on %s: off" % str(coord))

  ################# load yaml ################# 

  def loadYaml(self):

### end ###
