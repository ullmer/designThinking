# Simple example of bouncing ring
# Brygg Ullmer, Clemson University
# Begun 2023-09-20

import sys
import os
import pgzrun

WIDTH =600
HEIGHT=800

def draw(): 
  screen.clear()
  ring.draw()

endpoints       = [(50, 50), (600, 600)]
currentEndpoint = 1

animateTween = 'accel_decel'
ring         = Actor("ring01")
ring.pos     = endpoints[0]

################### reverse animation ################### 

def reverseAnimation():
  global endpoints, currentEndpoint, ring

  if currentEndpoint == 1:
    animate(ring, pos=endpoints[0], duration=1., tween=animateTween); currentEndpoint = 0
  else:
    animate(ring, pos=endpoints[1], duration=1., tween=animateTween); currentEndpoint = 1 

################### main ################### 

animate(ring, pos=endpoints[1], duration=1., tween=animateTween)
clock.schedule_interval(reverseAnimation, 1.)

x = 0
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x},{y}'
pgzrun.go()

### end ###
