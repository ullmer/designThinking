// Generated by SolidPython 1.1.3 on 2024-10-24 15:45:58
$fn = 25;


difference() {
	scale(v = [1.5000000000, 1, 1]) {
		cylinder(h = 0.5000000000, r = 0.5000000000);
	}
	scale(v = [1.5000000000, 1, 1]) {
		cylinder(h = 0.6000000000, r = 0.4000000000);
	}
	scale(v = [2, 0.2000000000, 2]) {
		translate(v = [-0.5000000000, -0.5000000000, 0]) {
			cube();
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code

#c1 = cylinder(r=.3, h=.6)
cy1  = cylinder(r=.5, h=.5)
cy1b = scale([1.5, 1, 1])(cy1)

cy2  = cylinder(r=.4, h=.6)
cy2b = scale([1.5, 1, 1])(cy2)

cu1  = cube()
cu1a = translate([-.5, -.5, 0])(cu1)
cu1b = scale([2, .2, 2])(cu1a)

outGeom = cy1b - cy2b - cu1b

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exSolid03a.scad', file_header=hdr) # write the .scad file

### end ###

 
 
************************************************/
