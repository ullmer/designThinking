a1 = Actor('red-hl-1in-200dpi')
a2 = Actor('red-hl-1in-200dpi', pos=(180, 180))

actors         = [a1, a2]
actorNames     = {a1: "John", a2: "Jane"}
actorLastPos   = {}
selectedObjectHandle = None
selectedObjectName   = None

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()

def on_mouse_down(pos):
  for actor in actors: 
    if actor.collidepoint(pos): 
      name = actorNames[actor]
      print("actor selected:", name)
      actorLastPos[actor] = pos     

      selectedObjectHandle = actor
      selectedObjectName   = name

  print("=" * 25)

def on_mouse_move(pos):
  objectName = selectedObjectName
  lastPos    = actorLastPos[selectObj]

  print("on_mouse_mov:", objectName, lastPos, pos)

### end ###
