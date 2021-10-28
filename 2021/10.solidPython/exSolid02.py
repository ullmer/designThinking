# SolidPython example code 
# Brygg Ullmer, Clemson University

from solid import *        # load in SolidPython/SCAD support code

c1 = cube()
c2 = translate([1.5, 0, 0])(c1)
outGeom = c1 + c2

y1 = cylinder(r=.3, h=.6)
y2 = translate([.5, .5, .5])(y1)
outGeom += y2

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid02.scad', file_header=hdr) # write the .scad file

### end ###

