#!/usr/bin/env python

import sys, os
from pygame import time
from enoMidiController import *

emc = enoMidiController('launchpad')
emc.registerControls(emc.simpleLightCallback)

while True:
  emc.pollMidi()
  time.wait(100)

### end ###
