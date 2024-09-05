# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

WIDTH, HEIGHT = 800, 800

a1 = Actor('readings_box_1c', pos=(400,400))
a2 = Actor('readings_box_1c', pos=(400,500))
actors = [a1, a2]

def draw(): 
  screen.clear()
  for actor in actors: actor.draw()

def on_mouse_down(pos): 
  if a1.collidepoint(pos): print("Actor 1 was pressed")
  if a2.collidepoint(pos): print("Actor 2 was pressed")

### end ###
