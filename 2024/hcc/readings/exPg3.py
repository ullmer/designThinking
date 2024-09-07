# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

WIDTH, HEIGHT = 800, 800

a = Actor('readings_box_1c', pos=(400,400))

def draw():             a.draw()
def on_mouse_down(pos): 
  if a.collidepoint(pos): print("Actor was pressed")

### end ###
