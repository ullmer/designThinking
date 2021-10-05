# Enodia Shapefile abstractions
# Brygg Ullmer, Clemson University
# Begun 10/02/2021

#https://www.visualcapitalist.com/wp-content/uploads/2017/10/interstate-highways-map.html

from enShapefile import *

import csv, traceback
capitolsFn = 'state-capitols.csv'
capitolsF  = open(capitolsFn, 'r+t')
dataReader = csv.reader(capitolsF, delimiter=',');

es       = enShapefile()
es.minDiff = 10.
es.targetRoads = []

for i in range(10, 91, 10): es.targetRoads.append(i)
#for i in range( 5, 96, 10): es.targetRoads.append(i)
#for i in range(195, 895, 100): es.targetRoads.append(i)

#manualList = [82,84,86,94, 17,29,24,43,77,79,81,87, 26, 44, 255, 270, 64]
#manualList = [82,84,86,94, 17,29,24,43,77,79,81,87,89,93, 26, 255, 270, 64, 57]
#manualList += [64,264,294,24,57, 505, 205, 880, 580, 475, 280, 69,96,496]
#manualList += [270, 71,69,74,72,335,470,44,69,269]
manualList = []

def roadBus(roadNum, postfixes=['W', 'E', ' W', ' E']): #business roads
  result = []
  for postfix in postfixes: result.append(str(roadNum) + postfix)
  return result

postfixedRoads = [35, 20]
#for postfixedRoad in postfixedRoads: manualList += roadBus(postfixedRoad)
#manualList += roadBus(5, [' Expy', ' Scn'])

for road in manualList: es.targetRoads.append(road)

print('targetRoads:', es.targetRoads)
es.extractInterstateVerts()
es.calcLatLongMinMaxRange()

rvs      = es.roadVertexSeqs
rvsNames = rvs.keys()

#es.cairoCreatePngSurface()
es.cairoCreatePdfSurface("usMap14.pdf")

for rvsName in rvsNames:      #primary road names
  for rvSeq in rvs[rvsName]: #list of constituitive vertex sequences
    es.plotCaiVertSeq(rvSeq)

#es.drawCircle([-81, 34], .02) #, Columbia, SC

firstline = True; lineNum = 0

#es.plotLatLong()

for capitolDS in dataReader: #state capitol data structure
  if firstline: firstline = False; continue
  city, state, long, lat = capitolDS; lineNum += 1
  #try:    es.drawCircle([float(lat), float(long)], .02) 
  #try:    es.drawCircle([float(lat), float(long)], .03) 
  #try:    es.drawCircle([float(lat), float(long)], .025) 
  #except: print(traceback.print_exc())

es.ctx.stroke()

#es.cairoWritePng("usMap12.png")
es.cairoWritePdf()
    
### end ###
