# Enodia Shapefile abstractions
# Brygg Ullmer, Clemson University
# Begun 10/02/2021

#https://github.com/GeospatialPython/pyshp
#https://www.pythoninformer.com/python-libraries/pycairo/drawing-shapes/

import shapefile
import cairo
import sys

################ Enodia Shapefile (TIGER GIS/Maps ################ 

class enShapefile:
  shapeFn = "shape/tl_2020_us_primaryroads.shp"
  sf      = None #shapefile

  #llmm = [-122.406817, -71.024618, 29.39391499999999, 47.71432] 
  latMin  = None #maximum and minimum latitude and longitude
  latMax  = None
  longMin  = None
  longMax  = None

  shapes  = None
  fields  = None
  records = None
  numRecs = None

  targetRoads    = [10,40,80,90] #Interstates
  targetRoadStrs = []

  ################ constructor ################ 

  method __init__(self):
   self.sf = shapefile.Reader(self.shapeFn)

   self.numRecs = len(sf)
   self.shapes  = sf.shapes()
   self.fields  = sf.fields
   self.records = sf.records()

   self.extractInterstateVerts()
   self.calcLatLongMinMaxRange()





for tr in targetRoads:
  trStr = "I- " + str(tr)
  targetRoadStrs.append(trStr)





for i in range(numRecs):
  sl = len(shapes[i].points)
  name = records[i][1]
  if (len(name.rstrip()) > 0 and name[0]=='I' and name[1]=='-'):
    if name in targetRoadStrs:
      #print("shape %i : points %i : name %s" % (i, sl, name))
      numPoints = len(shapes[i].points)
      if name not in roadVertexSeqs.keys(): roadVertexSeqs[name] = []
      for coord in shapes[i].points:        roadVertexSeqs[name].append(coord)


   self.calcLatLongMinMaxRange()
### get minimum and maximum ###

latMin = latMax = longMin = longMax = None

for rvs in roadVertexSeqs.keys():
  for vertex in roadVertexSeqs[rvs]:
    lat, long = vertex
    if latMin == None: latMin = latMax = lat; longMin = longMax = long
    else:
      if lat < latMin: latMin = lat
      if lat > latMax: latMax = lat

      if long < longMin: longMin = long
      if long > longMax: longMax = long


latRange  = abs(latMax - latMin)
longRange = abs(longMax - longMin)


### end ###
