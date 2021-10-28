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
  c1 = cube([barWidth, barThick, barLength])
  c2 = translate([offset,0,0])(c1)

  outGeom += c2; offset += between

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exXyl01.scad', file_header=hdr) # write the .scad file

### end ###

