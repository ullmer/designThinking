### Clemson Elevate evolving interactive instance ###
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

WIDTH, HEIGHT = 1200, 940

from enoLaunch import *
from enoPlaces import *

el = enoLaunch('elevateMap01.yaml')
ep = enoPlaces('elevatePlaces01.yaml')

def draw(): el.draw(); ep.draw()

### end ###
