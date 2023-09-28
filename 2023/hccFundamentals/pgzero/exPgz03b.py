# PyGame Zero examples 
# Brygg Ullmer, Clemson University 
# Begun 2022-11-01 

#https://pygame-zero.readthedocs.io/en/stable/

WIDTH  = 1358
HEIGHT = 1024

#magic for placing at 0,0
import platform, pygame
if platform.system() == "Windows":
  from ctypes import windll
  hwnd = pygame.display.get_wm_info()['window']
  windll.user32.MoveWindow(hwnd, 0, 0, WIDTH, HEIGHT, False)

## Return to interesting content

a1 = Actor("midjourney/homelessness-wall-01b")
a2 = Actor("midjourney/midjourney-figure-01b", pos=(100,550))
a3 = Actor("as_unit/as_unit_01b2",              pos=(400,450))
#a3 = Actor("as_unit/as_unit_01d",              pos=(400,450))

actors = [a1, a3, a2]

#animate(a2, pos=(300,600), duration=d, tween=t)
animateTween         = 'accel_decel'
animate(a2, pos=(600,600), duration=3., tween=animateTween)


def draw():
  for actor in actors: 
    actor.draw()

def on_mouse_down(pos):
  global actors
  print("mouse pushed:", pos)
  for actor in actors:
    if actor.collidepoint(pos):
      print("actor touched:", actor)
#        category = self.actor2category[actor]
#        print("pushed:", category)
#        self.animateSelected(category)



### end ###
