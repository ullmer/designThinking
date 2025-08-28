#!/usr/bin/env python

import sys, os
from pygame import time
from enoMidiController import *

#emc = enoMidiController('nu_mt3')
emc = enoMidiController('nu_dj2go2')

mc = emc.getYaml('mmpController')
controller  = mc['controller']
interactors = controller['interactors']
#print("interactors:",    interactors)

aliased     = interactors['aliased']
aliases     = interactors['aliases']
numAliases = len(aliases)
print("numAliases:", numAliases)

#### support function ####

interactorsList    = []
interactorsListIdx = -1
#interactorsListIdx = 50
lastController     = None
previouslyObserved = {}

def nextBinding():
  global emc, interactorsList, interactorsListIdx
  interactorsListIdx += 1
  interactor          = interactorsList[interactorsListIdx]
  print(interactor + ': ', end='')
  sys.stdout.flush()

#### callback function ####

def midiLabelCB(emc, control, arg):
  global lastController, previouslyObserved

  if control != lastController and control not in previouslyObserved:
    lastController = control; previouslyObserved[control] = True
    #print(control, arg)
    print(control + ", ")
    nextBinding()

#### main ####

emc.registerExternalCB(midiLabelCB)

for interactorType in aliased:
  interactors = aliased[interactorType]
  for interactor in interactors:
    interactorsList.append(interactor)

nextBinding()

while True:
  emc.pollMidi()
  time.wait(100)

### end ###
