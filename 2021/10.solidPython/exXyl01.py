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

  if fractional.find(' ') < 0: fraction = fractional; whole=0
  else:                        whole, fraction = fractional.split(' ')
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

barWidth   = convertFractional(yd['allBars']['wide'])
barThick   = convertFractional(yd['allBars']['thick'])
between    = convertFractional(yd['allBars']['between'])
barLengths = convertFractionalList(yd['lengths'])

#print(barWidth, barThick, barLengths)

outGeom = None; offset = 0
for barLength in barLengths:
  c1 = cube([barWidth, barThick, barLength])
  c2 = translate([offset,0,0])(c1)

  outGeom += c2; offset += between

radialSegments = 25; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exXyl01.scad', file_header=hdr) # write the .scad file

### end ###

