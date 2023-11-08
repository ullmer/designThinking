a1 = Actor('red-hl-1in-200dpi')
a2 = Actor('red-hl-1in-200dpi', pos=(180, 180))

actors = [a1, a2]

def draw(): 
  for actor in actors: actor.draw()

def on_mouse_down(pos):
  for actor in actors: 
    if actor.collidepoint(pos): print("something touched")

### end ###
