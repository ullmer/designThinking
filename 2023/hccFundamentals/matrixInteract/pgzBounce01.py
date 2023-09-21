WIDTH=600
HEIGHT=800

def draw(): 
  screen.clear()
  ring.draw()

animateTween = 'accel_decel'
ring         = Actor("ring01")
ring.pos     = 50, 50
animate(ring, pos=(600,600), duration=3., tween=animateTween)

### end ###
