# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code

cyl1a = cylinder(r=.5,  h=1.5)
cyl2a = cylinder(r=.4,  h=2)
cyl3a = cylinder(r=.45, h=2)
cyl4a = cylinder(r=.5, h=2)

cyl1b = scale([1.5, 1, 1])(    cyl1a)
cyl2b = scale([1.5, 1, 1])(    cyl2a)

cyl3b = rotate(a = [90, 0, 0])(cyl3a)
cyl4b = rotate(a = [90, 0, 0])(cyl4a)

cyl3c = translate([  0,  .7, .5])(cyl3b)
cyl4c = translate([-.25, .7, .59])(cyl4b)

cube1a = cube()
cube1b = translate([-.5, -.5, 0])(cube1a)
cube1c = scale([2, .2, 2])(       cube1b)

cube2a = cube(2)
cube2b = translate([-1.4, -.8, 1])(cube2a)
cube2c = rotate(a =[0, 15, 0])(    cube2b)

cube3a = cube(1.5)
cube3b = translate([-1.65, -.8, .7])(cube3a)

#outGeom = cyl1b - cyl2b - cube1c + cyl3b + cube2c
#outGeom = cyl1b - cyl2b - cube1c - cyl3c - cube2c
#outGeom = cyl1b - cyl2b - cube1c - cyl3c - cube2c + cube3b + cyl4c
#outGeom = cyl1b - cyl2b - cube1c - cyl3c - cube2c + (cube3b - cyl4c)
outGeom = cyl1b - cyl2b - cube1c - cyl3c - cube2c - (cube3b - cyl4c)

radialSegments = 90; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid03b.scad', file_header=hdr) # write the .scad file

### end ###

