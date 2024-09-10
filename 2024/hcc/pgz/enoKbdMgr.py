# Enodia keyboard manager 
# Brygg Ullmer, Clemson University
# Begun 2024-09-10

import traceback

############### enodia keyboard manager ############### 

class enoKbdMgr:
  keyCallbacksDict = None

  kbShortcuts = {1: 'ta49012', 2: 'arl', 3: 's123456789', 4: 'shj}

  ############### constructor ############### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
  
    self.keyCallbacksDict = {} #dictionary

  def err(self, msg): print("Reading error:", msg); traceback.print_exc()

  ############### register key callback ############### 

  def registerKeyCallback(self, whichKey, callback): #maintain in a list, as multiple callbacks may be present
    if self.keyCallbacksDict is None: self.err("registerKeyCallback: keyCallbacksDict is unset, should not happen;" return None
    if whichKey in self.keyCallbacksDict: self.keyCallbacksDict[whichKey].append(callback)
    else:                               self.keyCallbacksDict[whichKey] = [callback]

  ############### register key callback ############### 

  def registerKeyCallbacks(self, whichKey, callbackList): 
    if self.keyCallbacksDict is None: self.err("registerKeyCallbacks: keyCallbacksDict is unset, should not happen;" return None

    if isinstance(callbackList, list):
      for callback in callbackList: self.registerKeyCallback(whichKey, callback) # a bit inefficient, but possible later benefits
    else: 
      self.err("registerKeyCallbacks: expecting a callback List, but not present"); return

  ############### trigger key callback ############### 
 
  def triggerKeyCallbacks(self, whichKey): 
    if self.keyCallbacksDict is None: self.err("triggerKeyCallback: keyCallbacksDict is unset, should not happen;" return None

    if whichKey not in self.keyCallbacksDict: self.err("triggerKeyCallbacks: unregistered key invoked:" + whichKey); returna

    for callback in self.keyCallbacksDict:
      if isinstance(callback, string): 
        msgStr = "triggerKeyCallbacks: key: %s, val: %s" % (whichKey, callback)
        self.msg(msgStr); 
      else:
        try:    callback()
        except: self.err("triggerKeyCallbacks: attempted callback, error received"); traceback.print_exc() 

  ############### get bound keys ############### 

  def getBoundKeys(self): 
    if self.keyCallbacksDict is None: return None
    result = list(self.keyCallbacksDict.keys())
    return result

  ############### on key down ############### 

  def on_key_down(self, key): 
    if key in self.keyCallbacksDict:
    if key == keys.S:   eba2.toggleButtonIdx(1); print('store mode')
    if key == keys.L:   eba2.toggleButtonIdx(2); print('load  mode')

    if key.name.startswith('K_') and key.name[2].isdigit():
      digit = ord(key.name[2]) - ord('0')
      eba3.toggleButtonIdx(digit)

  ############### on key up ############### 

  def on_key_up(self, key): pass

### end ###
