# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

from enoAnimTranspBox import *

WIDTH, HEIGHT = 800, 800

#################### launch rectangle ####################

def launchRect():
  TL1, BR1 = cursor.topLeft, cursor.bottomRight
  TL2, BR2 = cursor.add(TL1, (0, -700)), cursor.add(BR1, (0, -700))
  
  launched = enoAnimTranspBox(animSrc=(TL1,BR1), animDest=(TL2,BR2), animDuration=3,
                            eTranspSurfaceCache=etsc2, lineColor=cursorColor)
  boxes.append(launched)

#################### main ####################

etsc1 = enoTranspSurfaceCache()
etsc2 = enoTranspSurfaceCache()

anSrc = ((  5, 700), ( 55, 750)); anDest = ((750, 700), (800, 750))
cursorColor = (200, 0, 0, 75)
cursor = enoAnimTranspBox(animSrc=anSrc, animDest=anDest, animBounce=True, animDuration=5, 
                          eTranspSurfaceCache = etsc2, lineColor=cursorColor)

boxes = [cursor]

def draw():           
  screen.clear(); 
  for box in boxes: box.draw(screen)

def on_key_down(key): launchRect()

### end ###
