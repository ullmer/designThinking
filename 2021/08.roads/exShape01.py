#https://github.com/GeospatialPython/pyshp

import shapefile
sf = shapefile.Reader("shape/tl_2020_us_primaryroads.shp")
print(len(sf))

### end ###
