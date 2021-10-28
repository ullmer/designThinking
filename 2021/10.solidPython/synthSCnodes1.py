# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code

scPopCoordFn = 'sc-pop-coord.csv'; scPCF = open(scPopCoordFn, "r")
scpcReader   = csv.reader(scPCF, delimiter=",")

outGeom = None
y1 = cylinder(r=.3, h=.6)

for row in scpcReader:
  city, pop, lat, long = row
  y2 = translate([lat, long, 0])(y1)

  if outGeom == None: outGeom = y2
  else:               outGeom += y2

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'scNodes1.scad', file_header=hdr) # write the .scad file

### end ###

