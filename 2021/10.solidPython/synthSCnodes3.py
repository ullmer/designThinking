# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code
import csv

scPopCoordFn = 'sc-pop-coord.csv'; scPCF = open(scPopCoordFn, "r")
scpcReader   = csv.reader(scPCF, delimiter=",")

def mapPop2Rad(popStr):
  try:     pop = int(popStr)
  except:  return 0

  popThresh = [5000, 25000, 50000, 100000, 250000, 500000]
  result = 1
  for testPop in popThresh:
    if pop > testPop: result += 1
    else:             return result
  return result 

outGeom = None
y1 = cylinder(r=.02, h=.1)

for row in scpcReader:
  city, popStr, lat, long = row
  y2 = translate([float(lat), float(long), 0])(y1)
  cylRad = mapPop2Rad(popStr)
  print(city, cylRad)

  if outGeom == None: outGeom = y2
  else:               outGeom += y2

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'scNodes1.scad', file_header=hdr) # write the .scad file

### end ###

