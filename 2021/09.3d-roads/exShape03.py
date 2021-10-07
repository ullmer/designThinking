#https://github.com/GeospatialPython/pyshp
#http://cimms.ou.edu/~lakshman/spatialprogramming/chapter03_basicgis/ch03_basicgis.pdf

import shapefile
sf = shapefile.Reader("shape/tl_2020_us_primaryroads.shp")

numRecs = len(sf)

shapes  = sf.shapes()
fields  = sf.fields
records = sf.records()

targetRoads=[10,40,80,90]
targetRoadStrs = []

vertices = {}

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
      if name not in vertices.keys(): vertices[name] = []
      for coord in shapes[i].points:  vertices[name].append(coord)

for name in targetRoadStrs:
  print('='*10, name, '='*10)
  print(vertices[name]) 

#shape = shapes[3].points[7]
#['%.3f' % coord for coord in shape]
#['-122.471', '37.787']

### end ###
