#Example of enoMidiController functionality for Novation Launchpad
#Brygg Ullmer, Clemson University
#Begun 2023-09-06

import sys, os
from pygame import time
from enoMidiController import *
from functools   import partial

#### callback function ####

def simpleCB(emc, control, arg):
  x, y = emc.addr2coord(control)
  emc.setLaunchpadXYColor(x, y, 0, 0, 63)

emc = enoMidiController('launchpad')
ecb = partial(simpleCB, emc)        #avoids use of globals
emc.registerControls(ecb)

while True:
  emc.pollMidi()
  time.wait(100)

### end ###
