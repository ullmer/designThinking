### Clemson Elevate evolving interactive instance ###
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

WIDTH, HEIGHT = 1200, 940

import yaml

yfn = 'elevateMap01.yaml'
yf  = open(yfn, 'rt')
y   = yaml.safe_load(yf)

bgFn = y['bgFn']
bg   = Actor(bgFn)

def draw(): bg.draw()

### end ###
