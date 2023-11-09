# Example code relating to interactive storyboarding
# By Brygg Ullmer, Clemson University
# Begun 2023-11-08

import sys, pygame

WIDTH=1024

a1 = Actor('red-hl-1in-200dpi')
a2 = Actor('red-hl-1in-200dpi',  pos=(180, 180))
s1 = Actor('unsdg2',             pos=(550, 100))
s2 = Actor('unsdg4',             pos=(550, 100))
b1 = Actor('person-add-iconic1', pos=( 80, 500))

successiveScreens = [s1, s2]

moveableActors = [a1, a2] #chara #could be reversed
stableActors   = [s1, b1]     #achara

actorNames           = {a1: "John", a2: "Jane", s1: "screen", b1: "addUser"}
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
  newActor = Actor('red-hl-1in-200dpi',  pos=(200, 200))
  moveableActors.append(newActor)
  actorNames[newActor] = 'new actor'

###################### on mouse down/press ######################

def on_mouse_down(pos):
  global selectedActor, selectedActorName, selectedActorOrigPos, stableActors
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
        selectedActor           = actor
        selectedActorName       = name
        selectedActorOrigPos    = selectedActor.pos

  print("=" * 25)

###################### on mouse move ######################

def on_mouse_move(pos):
  print(".", end=''); sys.stdout.flush() # print "." as update, with no newline -- and update
  
  if selectedActor != None: #make sure *something* is selected
    originalMousePos  = actorOriginalPos[selectedActor]

    x0, y0 = selectedActorOrigPos
    x1, y1 = originalMousePos
    x2, y2 = pos
    dx, dy = x2-x1, y2-y1
    x3, y3 = x0 + dx, y0 + dy
    selectedActor.pos = (x3, y3)

    #print("on_mouse_mov:", selectedActorName, originalMousePos, pos, dx, dy)

###################### on mouse up ######################

def on_mouse_up():
  global selectedActor, selectedActorName, selectedActorOrigPos
  selectedActor = selectedActorName = selectedActorOrigPos = None

###################### on key down ######################

numTimesSpaceHit = 0

def on_key_down(key):
  global numTimesSpaceHit

  if key == keys.SPACE:  # keys.RIGHT, keys.H, keys.C, etc.
    print("space pressed")

    #match numTimesSpaceHit:
    #  case 0:

    if numTimesSpaceHit == 0:
      animate(a1, pos=(400, 500), tween='accel_decel', duration=.75)
    else:
      animate(a2, pos=(500, 500), tween='accel_decel', duration=.75)

    numTimesSpaceHit += 1

### end ###

