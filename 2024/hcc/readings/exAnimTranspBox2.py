# Enodia animated transparent box
# By Brygg Ullmer, Clemson University
# Begun 2024-09-06

#Several key pygame alpha-drawing aspects draw from Asad Ali Yawar response in:
#https://stackoverflow.com/questions/18701453/how-to-draw-a-transparent-line-in-pygame

from enoAnimTranspBox import *

WIDTH, HEIGHT = 800, 800

print("main")
TL1 = (400, 400); BR1 = (780, 780)
TL2 = ( 10,  10); BR2 = (20, 20)

TL3 = (  5,   5); BR3 = (300, 300)
TL4 = (500, 500); BR4 = (600, 600)

TL5 = (  5, 700); BR5 = ( 55, 750)
TL6 = (750, 700); BR6 = (800, 750)

aSrc1, aDest1 = (TL1, BR1), (TL2, BR2)
aSrc2, aDest2 = (TL3, BR3), (TL4, BR4)
aSrc3, aDest3 = (TL5, BR5), (TL6, BR6)

etsc = enoTranspSurfaceCache()

#eatb1 = enoAnimTranspBox(topLeft=TL1, bottomRight=BR1)
eatb1 = enoAnimTranspBox(animSrc=aSrc1, animDest=aDest1, animBounce=True, eTranspSurfaceCache=etsc, animDuration=4)
eatb2 = enoAnimTranspBox(animSrc=aSrc2, animDest=aDest2, animBounce=True, eTranspSurfaceCache=etsc, animDuration=4)

cursorColor = (200, 0, 0, 75)
cursor = enoAnimTranspBox(animSrc=aSrc3, animDest=aDest3, animBounce=True, animDuration=5, lineColor=cursorColor)

def draw(): screen.clear(); eatb1.draw(screen); eatb2.draw(screen); cursor.draw(screen)

### end ###
