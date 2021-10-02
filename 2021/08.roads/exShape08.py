# Enodia Shapefile abstractions
# Brygg Ullmer, Clemson University
# Begun 10/02/2021

import enShapefile

es       = enShapefile()
es.targetRoads = [10, 40, 80, 90,  5, 15, 35, 55, 75, 85, 95]
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
