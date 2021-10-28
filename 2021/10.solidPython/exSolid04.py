# SolidPython example code 
# Brygg Ullmer, Clemson University

from solid import *        # load in SolidPython/SCAD support code

c1 = cube()
c2 = translate([1.5, 0, 0])(c1)
outGeom = c1 + c2

y1 = cylinder(r=1, h=.5)
y2 = rotate([90,0,0])(y1)
y3 = translate([1.25,.75,1.1])(y2)
outGeom += y3

radialSegments = 50; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid04.scad', file_header=hdr) # write the .scad file

### end ###

