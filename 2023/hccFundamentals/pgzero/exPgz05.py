import sys

a1 = Actor('red-hl-1in-200dpi')
a2 = Actor('red-hl-1in-200dpi', pos=(180, 180))

actors               = [a1, a2]
actorNames           = {a1: "John", a2: "Jane"}
actorOriginalPos     = {}
selectedObjectHandle = None
selectedObjectName   = None

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()

def on_mouse_down(pos):
  global selectedObjectName, selectedObjectHandle 
  for actor in actors: 
    if actor.collidepoint(pos): 
      name = actorNames[actor]
      print("actor selected:", name)
      actorOriginalPos[actor] = pos     
      selectedObjectHandle    = actor
      selectedObjectName      = name

  print("=" * 25)

def on_mouse_move(pos):
  print(".", end=''); sys.stdout.flush() # print "." as update, with no newline -- and update
  
  if selectedObjectHandle != None: #make sure *something* is selected
    originalPos  = actorOriginalPos[selectedObjectHandle]
    print("on_mouse_mov:", selectedObjectName, originalPos, pos)

### end ###
