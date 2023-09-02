### Clemson Elevate evolving interactive instance ###
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

WIDTH, HEIGHT = 1200, 940

from enoLaunch import *
from enoPlaces import *
import platform, pygame

#https://stackoverflow.com/questions/57674156/how-to-move-a-no-frame-pygame-windows-when-user-click-on-it/57681853#57681853

winPos = (0, 0)
if platform.system() == "Windows":
  from ctypes import windll
  hwnd = pygame.display.get_wm_info()['window']
  windll.user32.MoveWindow(hwnd, winPos[0], winPos[1], WIDTH, HEIGHT, False)

el = enoLaunch('elevateMap01.yaml')
ep = enoPlaces('elevatePlaces01.yaml')

def draw(): el.draw(); ep.draw()

### end ###
