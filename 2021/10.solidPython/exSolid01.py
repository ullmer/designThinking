# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code

c1 = cube()
c2 = translate([1.5, 0, 0])(c1)
outGeom = c1 + c2

print(scad_render(outGeom))

### end ###

