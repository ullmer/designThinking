# PyGame Zero examples 
# Brygg Ullmer, Clemson University 
# Begun 2022-11-01 

#https://pygame-zero.readthedocs.io/en/stable/

WIDTH  = 1358
HEIGHT = 1024

a1 = Actor("midjourney/homelessness-wall-01b")
a2 = Actor("midjourney/midjourney-figure-01b")
a3 = Actor("as_unit/as_unit_01d")

actors = [a1, a2, a3]

def draw():
  for actor in actors: 
    actor.draw()

### end ###
