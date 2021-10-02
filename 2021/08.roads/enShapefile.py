# Enodia Shapefile abstractions
# Brygg Ullmer, Clemson University
# Begun 10/02/2021

#https://www2.census.gov/geo/tiger/TIGER2020/PRIMARYROADS/tl_2020_us_primaryroads.zip
#https://github.com/GeospatialPython/pyshp
#https://www.pythoninformer.com/python-libraries/pycairo/drawing-shapes/

import shapefile
import cairo
import sys, math

################ Enodia Shapefile (TIGER GIS/Maps ################ 

class enShapefile:
  shapeFn  = "shape/tl_2020_us_primaryroads.shp"
  outPngFn = "ex08.png"
  sf       = None #shapefile

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
  
  normWidth  = 4
  normHeight = 2
  pixelScale = 200
  minDiff    = .05 # if new coord is less than this thresh offset, then ignore

  targetRoads    = [10,40,80,90] #Interstates
  targetRoadStrs = None
  roadVertexSeqs = None
    
  caiSurface = None #Cairo surface
  ctx        = None
  lineColor  = [1, .8, 0]

  ################ constructor ################ 

  def __init__(self):
   self.sf = shapefile.Reader(self.shapeFn)

   self.numRecs = len(self.sf)
   self.shapes  = self.sf.shapes()
   self.fields  = self.sf.fields
   self.records = self.sf.records()

   self.targetRoadStrs = []
   self.roadVertexSeqs = {}

   self.extractInterstateVerts()
   self.calcLatLongMinMaxRange()

  ################ calculate normalized lat and long ################ 

  def calcNormLatLong(self, lat, long):
    if self.latMin == None: self.calcLatLongMinMaxRange() #calculate bounds if not already done

    if lat < self.latMin or lat > self.latMax:
      print("enShapefile:calcNormLatLong: lat arg outside range"); return None

    if long < self.longMin or long > self.longMax:
      print("enShapefile:calcNormLatLong: long arg outside range"); return None

    latNorm  = abs(lat  - self.latMin)  / self.latRange
    longNorm = abs(long - self.longMin) / self.longRange
    result = [latNorm, longNorm]
    return result

  ################ plotCaiVertSeq ################ 

  def plotCaiCreateSurface(self): #use Cairo to create surface for plotting

    self.caiSurface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             self.normWidth * self.pixelScale,
                             self.normHeight * self.pixelScale)
    self.ctx = cairo.Context(self.caiSurface)
    self.ctx.scale(self.pixelScale, self.pixelScale)

    self.ctx.rectangle(0, 0, self.normWidth, self.normHeight)
    self.ctx.set_source_rgb(0.9, 0.9, 1)
    self.ctx.fill()

  ################ plotCaiVertSeq ################ 

  def plotCaiWritePng(self): #use Cairo to create surface for plotting
    self.caiSurface.write_to_png(self.outPngFn)
  
  ################ vertDist ################ 

  def vertDist(self, vert1, vert2): 
    result = math.dist(vert1, vert2)
    return result 
  
  ################ plotCaiVertSeq ################ 

  def plotCaiVertSeq(self, vertSeq): #use Cairo to plot vertex sequence
    #print("plotCaiVerSeq:", vertSeq)
    normVerts = []
    for vert in vertSeq:
      normVert = self.calcNormLatLong(vert[0], vert[1])
      normVerts.append(normVert)
      
    # Drawing code
    lastX, lastY = normVerts[0]
    self.ctx.move_to(lastX, lastY)

    for vert in normVerts[1:]:
      # if distance from last point sufficient, then plot; otherwise, ignore
      if self.vertDist(vert, [lastX, lastY]) > self.minDiff: 
        self.ctx.line_to(vert[0], vert[1])
        lastX, lastY = vert
   
    c = self.lineColor
    self.ctx.set_source_rgb(c[0], c[1], c[2])
    self.ctx.set_line_width(0.06)
    self.ctx.stroke()

  ################ extract Interstate Vertices ################ 

  def extractInterstateVerts(self):
    for tr in self.targetRoads:
      trStr = "I- " + str(tr)
      self.targetRoadStrs.append(trStr)

    for i in range(self.numRecs):
      sl = len(self.shapes[i].points) #shape length (relative to points)
      name = self.records[i][1]       #road name

      if (len(name.rstrip()) > 0 and name[0]=='I' and name[1]=='-'):
        if name in self.targetRoadStrs:
          #print("shape %i : points %i : name %s" % (i, sl, name))
          numPoints = len(self.shapes[i].points)

          if name not in self.roadVertexSeqs.keys(): 
            self.roadVertexSeqs[name] = []

          vertSeq = [] # to support multiple independent segments of same road, as appears the case

          for coord in self.shapes[i].points: vertSeq.append(coord)
          self.roadVertexSeqs[name].append(vertSeq)
    
  ############ calculate latitude, longitude min, max, range ############

  def calcLatLongMinMaxRange(self):

    for rvs in self.roadVertexSeqs.keys():
      for vertexSeq in self.roadVertexSeqs[rvs]:
        for vertex in vertexSeq:
          lat, long = vertex
          if self.latMin == None: 
            self.latMin  = self.latMax  = lat; 
            self.longMin = self.longMax = long; 
          else:
            if lat < self.latMin: self.latMin = lat
            if lat > self.latMax: self.latMax = lat
    
            if long < self.longMin: self.longMin = long
            if long > self.longMax: self.longMax = long
    
    self.latRange  = abs(self.latMax  - self.latMin)
    self.longRange = abs(self.longMax - self.longMin)
  
############ main ############

def main():
  es       = enShapefile()
  rvs      = es.roadVertexSeqs
  rvsNames = rvs.keys()

  es.plotCaiCreateSurface()

  for rvsName in rvsNames:      #primary road names
    for rvSeq in rvs[rvsName]: #list of constituitive vertex sequences
      es.plotCaiVertSeq(rvSeq)

  es.plotCaiWritePng()

if __name__ == "__main__": main()
    
### end ###
