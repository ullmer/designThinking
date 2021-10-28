# SolidPython example code 
# Brygg Ullmer, Clemson University

from solid import *        # load in SolidPython/SCAD support code

c1 = cube()
c2 = translate([1.5, 0, 0])(c1)
outGeom = c1 + c2

y1 = cylinder()
y2 = translate([3, 0, 0])(y1)
outGeom += y2

#print(scad_render(outGeom))
radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid02.scad', hdr)    # write the .scad file

### end ###

