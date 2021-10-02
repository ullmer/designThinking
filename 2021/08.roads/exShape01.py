#https://github.com/GeospatialPython/pyshp

import shapefile
sf = shapefile.Reader("shape/tl_2020_us_primaryroads.shp")

print(len(sf))
print(sf.fields)

#shapeRecs = sf.shapeRecords()
#print(dir(shapeRecs[0]))
#print(shapeRecs[0]['FULLNAME'])

shapes = sf.shapes()

for i in range(100):
  sl = len(shapes[i].points)
  print("shape %i : points %i" % (i, sl))


#shape = shapes[3].points[7]
#['%.3f' % coord for coord in shape]
#['-122.471', '37.787']

### end ###
