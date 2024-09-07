# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

from enoAnimTranspBox import *

WIDTH, HEIGHT = 800, 800

aSrc1 = ((400, 400), (780, 780)); aDest1 = (( 10,  10), (20, 20))
aSrc2 = ((  5,   5), (300, 300)); aDest2 = ((500, 500), (600, 600))
TL5 = (  5, 700); BR5 = ( 55, 750); TL6 = (750, 700); BR6 = (800, 750)

aSrc1, aDest1 = (TL1, BR1), (TL2, BR2)
aSrc2, aDest2 = (TL3, BR3), (TL4, BR4)
aSrc3, aDest3 = (TL5, BR5), (TL6, BR6)

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

#eatb1 = enoAnimTranspBox(topLeft=TL1, bottomRight=BR1)
eatb1 = enoAnimTranspBox(animSrc=aSrc1, animDest=aDest1, animBounce=True, eTranspSurfaceCache=etsc1, animDuration=4)
eatb2 = enoAnimTranspBox(animSrc=aSrc2, animDest=aDest2, animBounce=True, eTranspSurfaceCache=etsc1, animDuration=4)

cursorColor = (200, 0, 0, 75)
cursor = enoAnimTranspBox(animSrc=aSrc3, animDest=aDest3, animBounce=True, animDuration=5, 
                          eTranspSurfaceCache = etsc2, lineColor=cursorColor)

boxes = [eatb1, eatb2, cursor]

def draw():           
  screen.clear(); 
  for box in boxes: box.draw(screen)

def on_key_down(key): launchRect()

### end ###
