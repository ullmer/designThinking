#!/usr/bin/env python

import sys, os
from pygame import time
from enoMidiController import *

emc = enoMidiController('nu_mt3')

interactors = emc.get('interactors')
aliased     = interactors['aliased']


#emc.registerControls(emc.debugCallback)

eq = "=" * 10
for interactorType in aliased:
  print(eq + interactorType + eq)
  interactors = aliased[interactorType]
  for interactor in interactors:
    print(interactor)

#while True:
#  emc.pollMidi()
#  time.wait(100)

### end ###
