#https://github.com/GeospatialPython/pyshp
#https://www.pythoninformer.com/python-libraries/pycairo/drawing-shapes/

import shapefile

sf = shapefile.Reader("shape/tl_2020_us_primaryroads.shp")

numRecs = len(sf)

shapes  = sf.shapes()
fields  = sf.fields
records = sf.records()

targetRoads=[10,40,80,90]
targetRoadStrs = []

roadVertexSeqs = {}

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


print([latMin, latMax, longMin, longMax])

### end ###
