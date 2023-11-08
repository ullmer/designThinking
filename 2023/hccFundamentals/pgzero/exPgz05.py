import sys

WIDTH=1024

a1 = Actor('red-hl-1in-200dpi')
a2 = Actor('red-hl-1in-200dpi', pos=(180, 180))
s1 = Actor('unsdg2',            pos=(550, 100))
s2 = Actor('unsdg4',            pos=(550, 100))

moveableActors = [a1, a2] #chara #could be reversed
stableActors   = [s1]     #achara

actorNames           = {a1: "John", a2: "Jane", s1: "screen"}
actorOriginalPos     = {}
selectedActor        = None
selectedActorName    = None
selectedActorOrigPos = None

def draw(): 
  screen.clear()
  for actor in stableActors:   actor.draw()
  for actor in moveableActors: actor.draw()

def on_mouse_down(pos):
  global selectedActor, selectedActorName, selectedActorOrigPos, stableActors
  for actor in (stableActors + moveableActors):
    if actor.collidepoint(pos): 
      name = actorNames[actor]
      print("\nactor selected:", name)

      if name == "screen": 
        print("update the virtual screen images")
        stableActors = [s2]
      else:
        actorOriginalPos[actor] = pos     
        selectedActor           = actor
        selectedActorName       = name
        selectedActorOrigPos    = selectedActor.pos

  print("=" * 25)

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

def on_mouse_up():
  global selectedActor, selectedActorName, selectedActorOrigPos
  selectedActor = selectedActorName = selectedActorOrigPos = None

### end ###

