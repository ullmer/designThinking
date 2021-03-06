# Enodia Shapefile abstractions
# Brygg Ullmer, Clemson University
# Begun 10/02/2021

from enShapefile import *

es       = enShapefile()
es.targetRoads = []

for i in range(10, 91, 10): es.targetRoads.append(i)
for i in range( 5, 96, 10): es.targetRoads.append(i)
print('targetRoads:', es.targetRoads)

#es.targetRoads = [10, 20, 30, 40, 50, 60, 70, 80, 90,  5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
#es.targetRoads = [10, 90,  5, 95]

es.extractInterstateVerts()
es.calcLatLongMinMaxRange()

rvs      = es.roadVertexSeqs
rvsNames = rvs.keys()

es.plotCaiCreateSurface()

for rvsName in rvsNames:      #primary road names
  for rvSeq in rvs[rvsName]: #list of constituitive vertex sequences
    es.plotCaiVertSeq(rvSeq)

es.plotCaiWritePng()
    
### end ###
