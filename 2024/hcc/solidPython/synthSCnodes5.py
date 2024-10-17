# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-27

from solid import *        # load in SolidPython/SCAD support code
import csv
from mcmBolts import *

scPopCoordFn = 'sc-pop-coord.csv'; scPCF = open(scPopCoordFn, "r")
scpcReader   = csv.reader(scPCF, delimiter=",")

hlCities = ['Clemson', 'Greenville', 'Columbia', 'Charleston', 'Hartsville', 'Travelers Rest'] #highlight cities

############### map pop 2 bolt ###############

boltPopHash  = boltPopHashY = {0: 'n2', 25000: 'n4', 100000: 'n8', 500000: 'n1_4'}

def mapPop2Bolt(popStr, boltObj, boltPopHash):
  try:     pop = int(popStr)
  except:  return 1

  popThresh = boltPopHash.keys()
  idx = 0
  for testPop in popThresh:
    if pop > testPop: idx += 1
    else:             
      key = list(popThresh)[idx]
      boltSpec = boltPopHash[key]
      #print("bs1:", boltSpec)
      return boltObj.synthBoltNeutral(boltSpec)
  try:
    key = list(popThresh)[idx]
    boltSpec = boltPopHash[key]
    #print("bs2:", boltSpec)
    return boltObj.synthBoltNeutral(boltSpec)
  except: return -1

############### main ###############

boltObj = mcmBolts()
outGeom = None

for row in scpcReader:
  city, popStr, lat, long = row
  bolt1 = mapPop2Bolt(popStr, boltObj, boltPopHash)
  if isinstance(bolt1, int): continue #ignore errors

  bolt2 = rotate([180,0,0])(bolt1)
  coord = [float(lat)*65., float(long)*65., 0]
  #print("coord:", coord, str(bolt))
  y2 = translate(coord)(bolt2)
  #print(city, y2)

  if outGeom == None:    outGeom = y2
  elif city in hlCities: outGeom += color([1,.5,0])(y2)
  else:                  outGeom += y2

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'scNodes5.scad', file_header=hdr) # write the .scad file

### end ###

