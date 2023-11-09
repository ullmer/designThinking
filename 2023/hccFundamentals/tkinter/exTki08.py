# Example code relating to interactive storyboarding
# By Brygg Ullmer, Clemson University
# Begun 2023-11-08

from tkinter import *

#WIDTH=1024

screenStates = ['unsdg2', 'unsdg4']
imgAddUser   = 'person-add-iconic1'

#actorNames           = {a1: "John", a2: "Jane", s1: "screen", b1: "addUser"}
actorOriginalPos     = {}
selectedActor        = None
selectedActorName    = None
selectedActorOrigPos = None

def helloCB():
  print("hello was pushed")

#screen.draw.circle((800, 500), 50, defaultEllipseColor)
#
####################### on mouse down/press ######################
#
#def addUser():
#  newActor = Actor('red-hl-1in-200dpi',  pos=(200, 200))
#  moveableActors.append(newActor)
#  actorNames[newActor] = 'new actor'
#
####################### on mouse down/press ######################
#
#def on_mouse_down(pos):
#  global selectedActor, selectedActorName, selectedActorOrigPos, stableActors
#  for actor in (stableActors + moveableActors):
#    if actor.collidepoint(pos): 
#      name = actorNames[actor]
#      print("\nactor selected:", name)
#
#      if name == "screen": 
#        print("update the virtual screen images")
#        stableActors = [s2, b1]
#
#      elif name == "addUser":
#        addUser()
#
#      else:
#        actorOriginalPos[actor] = pos     
#        selectedActor           = actor
#        selectedActorName       = name
#        selectedActorOrigPos    = selectedActor.pos
#
#  print("=" * 25)
#
#def on_mouse_move()
#
####################### on mouse up ######################
#
#def on_mouse_up():
#  global selectedActor, selectedActorName, selectedActorOrigPos
#  selectedActor = selectedActorName = selectedActorOrigPos = None
#
####################### on key down ######################
#
#numTimesSpaceHit = 0
#
#def on_key_down(key):
#  global numTimesSpaceHit
#
#  if key == keys.SPACE:  # keys.RIGHT, keys.H, keys.C, etc.
#    print("space pressed")
#
#    #match numTimesSpaceHit:
#    #  case 0:
#
#    if numTimesSpaceHit == 0:
#      animate(a1, pos=(400, 500), tween='accel_decel', duration=.75)
#    else:
#      animate(a2, pos=(500, 500), tween='accel_decel', duration=.75)
#
#    numTimesSpaceHit += 1
#
####################### build UI ######################
#
#buildUI(f1Screens, f2Spatial, f3Controls):
#  
#
####################### main ######################

root = Tk() # Create the root (base) window

#b    = Button(root, text="Hello, world!", command=helloCB) # Create a label with words
#b.pack()                                                   # Put the label into the window

f1Screens  = Frame(root)
f2Spatial  = Frame(root)
f3Controls = Frame(root)
#buildUI(f1Screens, f2Spatial, f3Controls)

for frame in [f1Screens, f2Spatial, f3Controls]: frame.pack(side=TOP)

root.mainloop()                                            # Start the event loop

### end ###

