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

#for boltspec in boltspecs[5:]:
for boltspec in boltspecs:
  boltHeight = mb.getFullHeight(boltspec)
  stemHeight = mb.getStemHeight(boltspec)
  #print(boltspec, boltHeight, cz)

  if outGeom == None: 
    outGeom =  mb.synthBoltNeutral(boltspec)
  else:               
    cx += xd; cy += yd; cz += zd
    outGeom += mb.synthBoltNPos(boltspec, [cx,cy,cz])

  cz += (boltHeight+stemHeight) * 10

print(scad_render(outGeom))

### end ###

