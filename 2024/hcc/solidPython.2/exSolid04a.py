# SolidPython example code 
# Brygg Ullmer, Clemson University
# Begun 2024-10-24

from solid import *        # load in SolidPython/SCAD support code

cyl1a = cylinder(r=.5,  h=1.5); cyl1b = scale([1.5, 1,   1])(cyl1a) #cyl1b expresses the outer perimeter.  
cyl2a = cylinder(r=.4,  h=2);   cyl2b = scale([1.6, 1.1, 1])(cyl2a) #cyl2b is for cutting away the inside

outGeom = cyl1b - cyl2b #this performs the subtraction/cut, leaving an elliptical pipe 

radialSegments = 90; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid04a.scad', file_header=hdr) # write the .scad file

### end ###

