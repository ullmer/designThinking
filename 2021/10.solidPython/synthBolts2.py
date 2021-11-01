# Synthesize bolts within SolidPython
# Brygg Ullmer, Clemson University
# Begun 2021-10-31

from solid import *
from mcmBolts import *
import traceback

outGeom = None

cx, cy, cz = [0,0,0] #current xyz position
xd, yd, zd = [0,0,0] #xyz diffs

mb = mcmBolts()
boltspecs = mb.getBoltspecs()

for boltspec in boltspecs:
  boltHeight = mb.getFullHeight(boltspec)
  if boltHeight != None: cz += boltHeight * 15
  if outGeom == None: outGeom =  mb.synthBolt(boltspec)
  else:               
    cx += xd; cy += yd; cz += zd
    outGeom += mb.synthBoltPos(boltspec, [cx,cy,cz])

print(scad_render(outGeom))

### end ###

