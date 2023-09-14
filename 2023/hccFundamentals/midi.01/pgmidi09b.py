#Example of enoMidiController functionality for Novation Launchpad
#Brygg Ullmer, Clemson University
#Begun 2023-09-06

import sys, os
from pygame import time
from enoMidiController import *
from functools   import partial

#### callback function ####

def simpleCB(emc, control, arg):
  if control[0] == 'm': #margin button
    whichMarginKey = control[1]

    if emc.isRightMargin(whichMarginKey):
      color = emc.getRightMarginColor(whichMarginKey)
      emc.setActiveColor(color)
      emc.topMarginFadedColor(color)

    if emc.isTopMargin(whichMarginKey):
      color = emc.getTopMarginColor(whichMarginKey)
      emc.setActiveColor(color)
      
  else: 
    x, y    = emc.addr2coord(control)
    r, g, b = emc.getActiveColor()
    emc.setLaunchpadXYColor(x, y, r, g, b)

#### main ####

emc = enoMidiController('launchpad')
emc.clearLights()
emc.rightMarginRainbow()

ecb = partial(simpleCB, emc)        #avoids use of globals
emc.registerControls(ecb)

while True:
  emc.pollMidi()
  time.wait(100)

### end ###
