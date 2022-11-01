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

figurePosition=(100, 550)

a1 = Actor("midjourney/homelessness-wall-01b")
a2 = Actor("midjourney/midjourney-figure-01b", pos=figurePosition)
a3 = Actor("as_unit/as_unit_01d",              pos=(400,450))

actors = [a1, a3, a2]

def draw():
  for actor in actors: 
    actor.draw()

def on_mouse_down(pos):
  global figurePosition, a2

  if a2.collidepoint(pos): 
    print("figure touched")
    x, y = figurePosition
    figurePosition = (x+300, y)
    animate(a2, pos=figurePosition)

### end ###
