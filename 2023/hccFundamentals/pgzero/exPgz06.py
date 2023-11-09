# Example code relating to interactive storyboarding
# By Brygg Ullmer, Clemson University
# Begun 2023-11-08

import sys

WIDTH=1024

knownActorFilenames = ['red-hl-1in-200dpi', 'person-iconic1']
defaultActorFn      = knownActorFilenames[1]

a1 = Actor(defaultActorFn) #previously: a1 = Actor('red-hl-1in-200dpi')
a2 = Actor(defaultActorFn,  pos=(180, 180))
s1 = Actor('unsdg2',             pos=(550, 100)) #H20
s2 = Actor('unsdg4',             pos=(550, 100)) #NaCl
b1 = Actor('person-add-iconic1', pos=( 80, 500))
m1 = Actor('campus-map8',        pos=(348, 202))

successiveScreens = [s1, s2]
lastSelectedActor = a1

moveableActors = [m1, a1, a2, b1] # chalraha
stableActors   = [s1] #achalraha / rukha

actorNames           = {a1: "John", a2: "Jane", s1: "screen", 
                        b1: "addUser", m1: "map"}
actorOriginalPos     = {}
selectedActor        = None
selectedActorName    = None
selectedActorOrigPos = None
defaultEllipseColor    = (0, 200, 200)
defaultEllipseLocation = Rect((800, 600), (850, 650))

###################### draw ######################

def draw(): 
  screen.clear()
  for actor in stableActors:   actor.draw()
  for actor in moveableActors: actor.draw()

  #placeholder per idea from Yang
  #pygame.draw.ellipse(screen.surface, defaultEllipseColor, defaultEllipseLocation)
  screen.draw.circle((800, 500), 50, defaultEllipseColor)

###################### on mouse down/press ######################

def addUser():
  print("map position:", m1.pos)
  newActor = Actor('red-hl-1in-200dpi',  pos=(200, 200))
  moveableActors.append(newActor)
  actorNames[newActor] = 'new actor'

###################### on mouse down/press ######################

def on_mouse_down(pos): # on_press_down
  global selectedActor, selectedActorName, selectedActorOrigPos
  global stableActors, lastSelectedActor

  for actor in (stableActors + moveableActors):
    if actor.collidepoint(pos): 
      name = actorNames[actor]
      print("\nactor selected:", name)

      if name == "screen": 
        print("update the virtual screen images")
        stableActors = [s2, b1]

      elif name == "addUser":
        addUser()

      else:
        actorOriginalPos[actor] = pos     
        lastSelectedActor = selectedActor = actor
        selectedActorName       = name
        selectedActorOrigPos    = selectedActor.pos

  print("=" * 25)

###################### on mouse move ######################

def on_mouse_move(rel):
  print(".", end=''); sys.stdout.flush() # print "." as update, with no newline -- and update
  
  if selectedActor != None: #make sure *something* is selected
    origX, origY = selectedActor.pos
    dx,       dy = rel #relative position; thanks to pg0 magic, we cannot rename that
    newX,   newY = origX+dx, origY+dy
    selectedActor.pos = (newX, newY)

    #print("on_mouse_mov:", selectedActorName, originalMousePos, pos, dx, dy)

###################### on mouse up ######################

def on_mouse_up(): #on_press_up
  global selectedActor, selectedActorName, selectedActorOrigPos
  lastSelectedActor = selectedActor 
  selectedActor     = selectedActorName = selectedActorOrigPos = None

###################### on key down ######################

numTimesSpaceHit = 0

def on_key_down(key):
  global numTimesSpaceHit, lastSelectedActor

  if key == keys.SPACE:  # keys.RIGHT, keys.H, keys.C, etc.
    print("space pressed")

    #match numTimesSpaceHit:
    #  case 0:

    if numTimesSpaceHit == 0:
      animate(a1, pos=(400, 500), tween='accel_decel', duration=.75)
    else:
      animate(a2, pos=(500, 500), tween='accel_decel', duration=.75)

    numTimesSpaceHit += 1

  if key == keys.RIGHT: lastSelectedActor.angle += 45
  if key == keys.LEFT:  lastSelectedActor.angle -= 45

### end ###

