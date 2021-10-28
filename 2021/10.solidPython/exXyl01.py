# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-28

from   solid import *        # load in SolidPython/SCAD support code
import yaml

################ convert fractional ################

def convertFractional(fractional):
  if isinstance(fractional, int):   return fractional
  if isinstance(fractional, float): return fractional
  if fractional.find('/') < 0:      return int(fractional)

  whole, fraction = fractional.split(' ')
  num, denom      = fraction.split('/')
  result = float(whole) + float(num)/float(denom)
  return result

################ convert fractional list ################

def convertFractionalList(fractionalList):
  result = []
  for fractional in fractionalList:
    result.append(convertFractional(fractional))
  return result

################ main ################

yfn = 'xylophone.yaml'
yf  = open(yfn, 'r')
yd  = yaml.safe_load(yf)

barWidth   = yd['allBars']['wide']
barThick   = yd['allBars']['thick']
barLengths = convertFractionalList(yd['lengths'])

print(barWidth, barThick, barLengths)

c1 = cube()
c2 = translate([1.5, 0, 0])(c1)
outGeom = c1 + c2

y1 = cylinder(r=.3, h=.6)
y2 = translate([.5, .5, .5])(y1)
outGeom += y2

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exXyl01.scad', file_header=hdr) # write the .scad file

### end ###

