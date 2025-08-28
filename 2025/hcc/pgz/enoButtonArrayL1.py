# Specific variant of enodia button array; name should be evolved,
#  but needs fleshing out and companionship for sufficient clarity
# Brygg Ullmer, Clemson University
# Begun    2022-02-22
# Revamped 2024-09

# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

from enoButtonArray import *
import traceback

##################### enodia button array L1 (linear variant 1) #####################

class enoButtonArrayL1(enoButtonArray):
  buttonDim  = (75, 75)
  dx, dy     = 80, 0

  textArray       = None
  buttonArray     = None
  imageFns        = None
  lastSelected    = None
  angle           = 0
  requestAnim     = False
  motionAnimTween = None
  animDuration    = 1.
  callbackList    = None

  expandContractState = 1   # 1 if expanded or animating in that direction; 0 if contracted

  buttonRetractedPos = None # buttons in contracted position, optionally (esp. if animated)
  buttonUnfurledPos  = None # buttons in unfurled position, optionally (esp. if animated)
  text2Button        = None

  ############# error message #############

  def err(self, msg): print("enoButtonArrayL1 error:" + msg)
  def msg(self, msg): print("enoButtonArrayL1 msg:  " + msg)

  ############# constructor #############

  def __init__(self, buttonTextList, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

### end ###
