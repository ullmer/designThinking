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
  latMin    = None #maximum and minimum latitude and longitude
  latMax    = None
  longMin   = None
  longMax   = None
  latRange  = None
  longRange = None

  shapes  = None
  fields  = None
  records = None
  numRecs = None
  
  normWidth  = 4.
  normHeight = 2.
  minDiff    = .05 # if new coord is less than this thresh offset, then ignore

  targetRoads    = [10,40,80,90] #Interstates
  targetRoadStrs = None
  roadVertexSeqs = None

  ################ constructor ################ 

  method __init__(self):
   self.sf = shapefile.Reader(self.shapeFn)

   self.numRecs = len(sf)
   self.shapes  = sf.shapes()
   self.fields  = sf.fields
   self.records = sf.records()

   self.targetRoadStrs = []
   self.roadVertexSeqs = {}

   self.extractInterstateVerts()
   self.calcLatLongMinMaxRange()

  ################ calculate normalized lat and long ################ 

  method calcNormLatLong(self, lat, long):
    if self.latMin == None: self.calcLatLongMinMaxRange() #calculate bounds if not already done

    if lat < self.latMin or lat > self.latMax:
      print("enShapefile:calcNormLatLong: lat arg outside range"); return None

    if long < self.longMin or long > self.longMax:
      print("enShapefile:calcNormLatLong: long arg outside range"); return None

    latNorm  = abs(lat  - self.latMin)  / self.latRange
    longNorm = abs(long - self.longMin) / self.longRange
    result = [latNorm, longNorm]
    return result

  ################ extract Interstate Vertices ################ 

  method extractInterstateVerts(self):
    for tr in self.targetRoads:
      trStr = "I- " + str(tr)
      self.targetRoadStrs.append(trStr)

    for i in range(self.numRecs):
      sl = len(self.shapes[i].points) #shape length (relative to points)
      name = self.records[i][1]       #road name

      if (len(name.rstrip()) > 0 and name[0]=='I' and name[1]=='-'):
        if name in self.targetRoadStrs:
          #print("shape %i : points %i : name %s" % (i, sl, name))
          numPoints = len(shapes[i].points)

          if name not in self.roadVertexSeqs.keys(): 
            self.roadVertexSeqs[name] = []

          vertSeq = [] # to support multiple independent segments of same road, as appears the case

          for coord in self.shapes[i].points: vertSeq.append(coord)
          self.roadVertexSeqs[name].append(vertSeq)
    
  ############ calculate latitude, longitude min, max, range ############

   method calcLatLongMinMaxRange(self):

    for rvs in self.roadVertexSeqs.keys():
      for vertex in roadVertexSeqs[rvs]:
        lat, long = vertex
        if latMin == None: latMin = latMax = lat; longMin = longMax = long
        else:
          if lat < latMin: latMin = lat
          if lat > latMax: latMax = lat
    
          if long < longMin: longMin = long
          if long > longMax: longMax = long
    
    self.latRange  = abs(latMax - latMin)
    self.longRange = abs(longMax - longMin)
    
### end ###
