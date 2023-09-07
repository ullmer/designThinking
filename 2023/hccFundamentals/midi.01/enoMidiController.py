### Enodia MIDI controller wrapper class ###
# Brygg Ullmer, Clemson University
# Begun 2023-09-06

import os, os.path, sys
import traceback, yaml
import pygame, pygame.midi
from   pygame import time

from functools   import partial
#cb = partial(self.bodyCb, "rank") # example of callback construction

##########################################################
################# Enodia MIDI Controller #################

class enoMidiController:

  yamlDir = 'yaml' #yaml directory
  yamlFn  = None   #yaml filename
  yamlD   = None   #yaml data
  controllerName    = None
  controlsList      = None

  midiCtrlInputId     = 1
  midiCtrlOutputId    = 3
  numMidiReadsPerPoll = 50

  activateInput     = False
  activateOutput    = False
  activateLaunchpad = True # integrates input and output

  midiIn    = None
  midiOut   = None
  lp        = None #launchpad handle

  controllerNameDict = {'launchpad': 'novation-launchpad-mk2c-midi',
                        'dj2go2':    'numark-dj2go2b-midi'}

  controllerStatusNumDict  = None
  controllerNumDict        = None
  controlCbDict            = None # control callback dictionary

  rainbow8 = [[63, 0, 0], [63, 21, 0], [63, 63, 0], [0, 63, 0], [0, 0, 63], [30, 0, 50], [50, 0, 30], [63, 63, 63]]
  colorDivisors = [63, 40, 30, 20, 8, 5, 2, 1]
  activeColor = [63, 63, 63]

  topMarginColors   = None
  rightMarginColors = None

  ############# constructor #############

  def __init__(self, controllerName, **kwargs):

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.controllerName = controllerName
    yamlFn = self.controller2yamlFn(controllerName)
    self.loadYaml(yamlFn)
    self.startMidi()

  ############# set/get active color #############

  def setActiveColor(self, color):
    self.activeColor = color
  
  def getActiveColor(self):
    return self.activeColor 

  ############# margin functions #############

  def isRightMargin(self, key):
    lkey = str(key).lower()
    if lkey >= 'a' and lkey <= 'h': return True
    return False

  def isTopMargin(self, key):
    try:
      idx = int(key) 
      if idx >= 0 and idx < 8: return True
    except: pass
    return False

  def getRightMarginColor(self, key):
    lkey = str(key).lower()
    idx  = ord(lkey) - ord('a')
    if idx < len(self.rightMarginColors): return self.rightMarginColors[idx]
 
  def getTopMarginColor(self, key):
    idx = int(key)-1
    if idx < len(self.topMarginColors): 
      color = self.topMarginColors[idx]
      return color
 
  ############# start midi #############

  def startMidi(self):
    pygame.midi.init()
 
    inId, outId = self.midiCtrlInputId, self.midiCtrlOutputId

    #if self.activateLaunchpad: self.initLaunchpad()

    if self.activateInput:     self.midiIn  = pygame.midi.Input(inId)
    if self.activateOutput:    self.midiOut = pygame.midi.Input(outId)
    if self.activateLaunchpad: self.initLaunchpad()

  ############# map controller to yaml filename #############

  def controller2yamlFn(self, controllerName):

    if controllerName not in self.controllerNameDict:
      print("enoMidiController controller2yamlFn: controllerName %s " + \
            "not in known list!" % controllerName)
      return None

    fn1 = self.controllerNameDict[controllerName]
    fn2 = "%s/%s.yaml" % (self.yamlDir, fn1)

    if os.path.exists(fn2): return fn2
    else: 
      print("enoMidiController controller2yamlFn: filename %s does not exist!" % fn2)
      return None

  ############# load yaml #############

  def loadYaml(self, yamlFn):
    if os.path.exists(yamlFn) is False: 
      print("enoMidiController loadYaml: filename %s does not exist!" % yamlFn)
      return None

    f = open(yamlFn, 'rt')
    self.yamlD = yaml.safe_load(f)
    f.close()

    try:
      self.controlsList = self.yamlD['mmpController']['controller']['controls']['control']
    except:
      print("enoMidiController loadYaml controlList parsing error")
      traceback.print_exc(); return None

    print("enoMidiController loadYaml: controlsList length:", len(self.controlsList))
    #self.registerControls(self.simpleLightCallback)

    #print("enoMidiController loadYaml: controlCbDict", self.controlCbDict)
    #print("enoMidiController loadYaml: controllerStatusNumDict", self.controllerStatusNumDict)

  ############# midi status num key generator #############

  def midiStatusNumKey(self, midiStatus, midiNum):
    try:    result = "%i_%i" % (midiStatus, midiNum)
    except: result = "%s_%s" % (str(midiStatus), str(midiNum))
    return  result

  ############# register callback #############

  def registerCallback(self, controlName, callback):
    if self.controlCbDict == None: self.controlCbDict = {}

    # https://www.geeksforgeeks.org/partial-functions-python/
    cb = partial(callback, controlName) 
    self.controlCbDict[controlName] = cb

  ############# debug callback #############

  def debugCallback(self, control, arg):
    print("enoMidiController debugCallback: ", str(control), str(arg))

  ############# debug callback #############

  def addr2coord(self, addr):
    x = int(addr[1])-1
    y = int(ord(addr[0])-ord('a'))+1
    return [x, y]

  ############# debug callback #############

  def simpleLightCallback(self, control, arg):
    x, y = self.addr2coord(control)
    self.setLaunchpadXYColor(x, y, 0, 0, 63)

  ############# invoke callback #############

  def invokeCallback(self, controlName, controlVal):
    if self.controlCbDict == None: return None

    try:
      callback = self.controlCbDict[controlName]
      result = callback(controlVal) 
      return result
    except:
      print("enoMidiController invokeCallback exception:")
      traceback.print_exc(); return None

  ############# register controls #############

  def registerControls(self, callbackFunc):
    controlsList = self.controlsList
    if controlsList == None: 
      print("enoMidiController registerControls: controlsList is empty"); return None

    if self.controllerStatusNumDict == None: self.controllerStatusNumDict = {}
    if self.controllerNumDict       == None: self.controllerNumDict       = {}

    try:
      for c in controlsList:
        ctrlName, midiStatus, midiNum = c['key'], c['status'], c['midino']
        midiStatNumKey = self.midiStatusNumKey(midiStatus, midiNum)
        self.controllerStatusNumDict[midiStatNumKey] = ctrlName
        self.controllerNumDict[midiNum]              = ctrlName
        #self.registerCallback(ctrlName, self.debugCallback)
        self.registerCallback(ctrlName, callbackFunc)
    except:
      print("enoMidiController registerControls exception:")
      traceback.print_exc(); return None

  ############# initLaunchpad #############

  def initLaunchpad(self):
    try:
      import launchpad_py as launchpad
    except ImportError:
      try:
        import launchpad
      except ImportError:
        sys.exit("ERROR: loading launchpad.py failed")

    self.lp = launchpad.Launchpad()

    # try the first Mk2
    if self.lp.Check( 0, "mk2" ):
      self.lp = launchpad.LaunchpadMk2()

      if self.lp.Open( 0, "mk2" ): print( " - Launchpad Mk2: OK" )
      else:                        print( " - Launchpad Mk2: ERROR"); return
    else: print( " - No Launchpad Mk2 available" ); return

    # Clear the buffer because the Launchpad remembers everything
    self.lp.ButtonFlush()

  ############# clearlights #############

  def clearLights(self):
    if self.lp == None: 
      print("enoMidiController clearLights error: launchpad LED controller not initiated!")
      return None

    self.lp.LedAllOn( 0 )

  ############# set launchpad xy color #############

  def setLaunchpadXYColor(self, x, y, r, g, b):
    if self.lp == None: 
      print("enoMidiController setLaunchpadXYColor error: launchpad LED controller not initiated!")
      return None
    self.lp.LedCtrlXY(x, y, r, g, b)

  ############# right margin rainbow #############

  def rightMarginRainbow(self):
    x = 8; self.rightMarginColors = []
    for y in range(1,9):
      r, g, b = color = self.rainbow8[y-1]
      self.setLaunchpadXYColor(x, y, r, g, b)
      self.rightMarginColors.append(color)

  ############# top margin faded color #############

  def topMarginFadedColor(self, fullColor):
    y = 0; self.topMarginColors = []
    for x in range(8):
      divisor = float(self.colorDivisors[x])
      r1, g1, b1 = fullColor
      r2, g2, b2 = int(r1/divisor), int(g1/divisor), int(b1/divisor)
      self.setLaunchpadXYColor(x, y, r2, g2, b2)
      self.topMarginColors.append([r2, g2, b2])

  ############# process midi update #############

  def processMidiUpdate(self, midiStatus, midiNum, val):
    #print("pmu", midiStatus, midiNum, val)
    msn = self.midiStatusNumKey(midiStatus, midiNum)

    if self.controllerStatusNumDict == None: 
      print("enoMidiController: processMidiUpdate called, but no registered data")
      return None

    if msn in self.controllerStatusNumDict:
      control = self.controllerStatusNumDict[msn]
      self.invokeCallback(control, val)

  ############# process midi update #############

  def processMidiUpdate(self, midiNum, val):
    if self.controllerNumDict == None: 
      print("enoMidiController: processMidiUpdate called, but no registered data")
      return None

    if midiNum in self.controllerNumDict:
      control = self.controllerNumDict[midiNum]
      self.invokeCallback(control, val)

  ############# pollMidi #############

  def pollMidi(self):
    if self.lp is not None:
      bstate = self.lp.ButtonStateRaw()
      if bstate != []:
        midiNum, val1 = bstate
        self.processMidiUpdate(midiNum, val1)

    elif self.midiIn is not None:
      events = self.midiIn.read(self.numMidiReadsPerPoll)
      for el in events: 
        #print(".", end=""); sys.stdout.flush()
        payload, timestamp = el
        midiStatus, midiNum, val1, val2 = payload
        self.processMidiUpdate(midiStatus, midiNum, val1)
  
### end ###
