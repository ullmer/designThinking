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

  ############### err, msg ############### 

  def err(self, msg): print("enoKbdMgr error:", msg);  traceback.print_exc()
  def msg(self, msg): print("enoKbdMgr message:", msg)

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

  ############### isKeyBound ############### 

  def isKeyBound(self, whichKey): 
    if self.keyCallbacksDict is None:     return False
    if whichKey in self.keyCallbacksDict: return True
    return False

  ############### on key down ############### 

  def on_key_down(self, key): 
    if self.isKeyBound(key): self.triggerKeyCallbacks(key)

  ############### on key up ############### 

  def on_key_up(self, key): pass #not always to be ignored; more to come

### end ###
