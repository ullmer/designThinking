#https://github.com/GeospatialPython/pyshp
#http://cimms.ou.edu/~lakshman/spatialprogramming/chapter03_basicgis/ch03_basicgis.pdf

import shapefile
sf = shapefile.Reader("shape/tl_2020_us_primaryroads.shp")

numRecs = len(sf)

shapes  = sf.shapes()
fields  = sf.fields
records = sf.records()

for i in range(numRecs):
  sl = len(shapes[i].points)
  name = records[i][1]
  if (len(name.rstrip()) > 0 and name[0]=='I' and name[1]=='-'):
    print("shape %i : points %i : name %s" % (i, sl, name))


#shape = shapes[3].points[7]
#['%.3f' % coord for coord in shape]
#['-122.471', '37.787']

### end ###
