# SolidPython example code 
# Brygg Ullmer, Clemson University
# Begun 2024-10-24
# Documented on 2024-12-04

from solid import *        # load in SolidPython/SCAD support code

cyl1a = cylinder(r=.5,  h=1.5); cyl1b = scale([1.5, 1,   1])(cyl1a) #cyl1b expresses the outer perimeter.  
cyl2a = cylinder(r=.4,  h=2);   cyl2b = scale([1.6, 1.1, 1])(cyl2a) #cyl2b is for cutting away the inside
outGeom = cyl1b - cyl2b #output as exSolid04a.png. this performs the subtraction/cut, leaving an elliptical pipe.  

cube1a = cube();  cube1b = translate([ -.5, -.5, 0 ])(cube1a); cube1c = scale([2, .2, 2])(cube1b) #for cutting the pipe in two
cyl3a  = cylinder(r=.45, h=2); cyl3b = rotate(a = [90, 0, 0])(cyl3a)
cyl3c  = translate([0, .7, .5 ])(cyl3b) #cylinder for large hole perforating the two halves of the oculus
outGeom -= cube1c #cleave the pipe into left and right halves
outGeom -= cyl3c  #output as exSolid04b.png. perforate the two halves of the oculus 

radialSegments = 90; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid04b.scad', file_header=hdr) # write the .scad file

### end ###

