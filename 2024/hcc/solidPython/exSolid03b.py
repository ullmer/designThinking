# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code

cyl1  = cylinder(r=.5,  h=1)
cyl2  = cylinder(r=.4,  h=1.5)
cyl3  = cylinder(r=.45, h=2)

cyl1b = scale([1.5, 1, 1])(    cyl1)
cyl2b = scale([1.5, 1, 1])(    cyl2)
cyl3a = rotate(a = [90, 0, 0])(cyl3)
cyl3b = translate([0, 0.7, .5])(  cyl3a)

cub1  = cube()
cub1a = translate([-.5, -.5, 0])(cub1)
cub1b = scale([2, .2, 2])(cub1a)

outGeom = cyl1b - cyl2b - cub1b + cyl3b

radialSegments = 90; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid03b.scad', file_header=hdr) # write the .scad file

### end ###

