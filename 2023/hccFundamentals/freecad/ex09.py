# First validation of Python port of 1995 3wish code
# Brygg Ullmer, Clemson University
# Original code begun fall 1995; here, 2023-10-20

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin
import sys, traceback

basedir = 'c:/git/tangibles/sw/3wish.02'
sys.path.append(basedir)
from w3core     import *
from enoFreecad import *

view, doc, sg, root = genViewDocSgRoot()

yamlFn = basedir + '/scene01.yaml'
efc    = enoFreecad(yamlFn, doc)

bldgCut1   = App.activeDocument().addObject("Part::Cut", "Bldg central void")
bldgCut1.Base = efc.getObj("bldg1a")
bldgCut1.Tool = efc.getObj("bldg1b")

doc.recompute()
Gui.runCommand('Std_CloseActiveWindow',0) #no idea why currently necessary; will later remove

cc = efc.getCameraConfig("pos1")
setCameraConfig(cc)

s1 = efc.getObj("screen1")
print(dir(s1))
print("FOO")
s1Node = s1.ViewObject.RootNode
s1NodeChildren = s1Node.getChildren()
s1ncLen = s1NodeChildren.getLength()
print(s1ncLen)
#n0 = s1NodeChildren.get(0)
nodeSwitch = s1NodeChildren.get(2)

outFn = basedir + "/test.iv"
writeObj(nodeSwitch, outFn)
print("saved", outFn)

#nsChildren = nodeSwitch.getChildren()
#nss1 = nsChildren.get(0)
#nct = nss1.getClassTypeId().getName()
#print(nct)
#print(dir(n0))
#print(n0.getClassTypeId().getName())

try:
  import pygame as pg
  import pygame.midi
  pygame.midi.init()
  
  ############ update midi ############
  
  def updateMidi(arg1, arg2):
    global midiIn
    e = midiIn.read(100); 
    if len(e) > 2: 
       events = e[1:]
       print(e)
       #print(len(events), events)
       #for event in e[1]: print("event:", event)
  
  global midiIn
  midiIn = pygame.midi.Input(1)
  
  e = midiIn.read(100); print(e)
  
  ts = coin.SoTimerSensor(updateMidi, 0)
  ts.schedule()
except:
  print("error with pygame/midi functionality:")
  traceback.print_exc()
  
### end ###
