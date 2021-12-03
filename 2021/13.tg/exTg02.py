# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-28

from solid import *        # load in SolidPython/SCAD support code

c1 = cylinder(r=1, h=.5)
outGeom = c1

c2 = translate([1.5,0,0])(c1)

numF = 5
rot  = 0; rotIncr = 30

for i in range(numF):
  c3 = rotate([rot,0,0])(c2)
  outGeom += c3; rot += rotIncr

radialSegments = 50; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exTg02.scad', file_header=hdr) # write the .scad file

### end ###

