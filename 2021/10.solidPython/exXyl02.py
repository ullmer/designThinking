# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-28

from       solid import * # load in SolidPython/SCAD support code
from synthShapes import *
import yaml

yfn = 'xylophone.yaml'
yf  = open(yfn, 'r')
yd  = yaml.safe_load(yf)

barWidth   = convertFractional(yd['allBars']['wide'])
barThick   = convertFractional(yd['allBars']['thick'])
between    = convertFractional(yd['allBars']['between'])
barLengths = convertFractionalList(yd['lengths'])

#print(barWidth, barThick, barLengths)

outGeom = None; offset = 0
for barLength in barLengths:
  c1 = cube([barWidth, barLength, barThick])
  c2 = translate([offset,0,0])(c1)

  if outGeom == None: outGeom = c2
  else:               outGeom += c2
  offset += barWidth + between

y1 = cylinder()
y2 = scale([.5,5,20])(y1)
y3 = rotate([0,90,0])(y2)
y4 = translate([-1,.75,-.25])(y3)
y5 = color([1,0,0])(y4)
outGeom += y5

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exXyl02.scad', file_header=hdr) # write the .scad file

### end ###

