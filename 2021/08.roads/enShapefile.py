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


  method __init__(self):





sf = shapefile.Reader("shape/tl_2020_us_primaryroads.shp")

 #llmm = [-122.406817, -71.024618, 29.39391499999999, 47.71432] #lat long min max
latMin = llmm[0];  latMax  = llmm[1]; latRange  = abs(latMax - latMin)
longMin = llmm[2]; longMax = llmm[3]; longRange = abs(longMax - longMin)

print([latRange, longRange]); sys.exit()
WIDTH = 3; HEIGHT=2

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

#for name in targetRoadStrs:
#  print('='*10, name, '='*10)
#  print(vertices[name]) 

fig, ax = plt.subplots(figsize = (20,20))

ExistingRoutesMap.plot(ax=ax,color = 'green', label = 'bus routes')

plt.show()

#shape = shapes[3].points[7]
#['%.3f' % coord for coord in shape]
#['-122.471', '37.787']

### end ###
