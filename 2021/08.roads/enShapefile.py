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
  sf       = None            #shapefile

  #llmm = [-122.406817, -71.024618, 29.39391499999999, 47.71432] 
  latMin    = None #maximum and minimum latitude and longitude
  latMax    = None
  longMin   = None
  longMax   = None
  latRange  = None
  longRange = None

  longTick = [-70,-80,-90,-100,-110,-120]
  latTick  = [30,40,50]

  shapes  = None
  fields  = None
  records = None
  numRecs = None
  
  normWidth  = 4
  normHeight = 2
  pixelScale = 300
  minDiff    = .04 # if new coord is less than this thresh offset, then ignore

  targetRoads    = [10,40,80,90] #Interstates
  targetRoadStrs = None
  roadVertexSeqs = None
    
  caiSurface = None #Cairo surface
  ctx        = None
  lineColor  = [0, .1, .4]

  ################ constructor ################ 

  def __init__(self):
   self.sf = shapefile.Reader(self.shapeFn)

   self.numRecs = len(self.sf)
   self.shapes  = self.sf.shapes()
   self.fields  = self.sf.fields
   self.records = self.sf.records()

   self.targetRoadStrs = []
   self.roadVertexSeqs = {}

   #self.extractInterstateVerts()
   #self.calcLatLongMinMaxRange()

  ################ calculate normalized lat and long ################ 

  def calcNormLatLong(self, lat, long):
    if self.latMin == None: self.calcLatLongMinMaxRange() #calculate bounds if not already done

    if lat < self.latMin or lat > self.latMax:
      print("enShapefile:calcNormLatLong: lat arg outside range"); return None

    if long < self.longMin or long > self.longMax:
      print("enShapefile:calcNormLatLong: long arg outside range"); return None

    latNorm  = abs(lat  - self.latMin)  / self.latRange
    longNorm = abs(long - self.longMin) / self.longRange
    result = [latNorm * self.normWidth, (1.-longNorm) * self.normHeight]
    #print('cnLL:', result)
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

  def plotCaiWritePng(self, pngFn=None): #use Cairo to create surface for plotting
    if pngFn==None: pngFn= self.outPngFn
    self.caiSurface.write_to_png(pngFn)
  
  ################ vertDist ################ 

  def vertDist(self, vert1, vert2): 
    result = math.dist(vert1, vert2)
    return result 
  
  ################ drawCircle ################ 
  # https://zetcode.com/gfx/pycairo/basicdrawing/

  def drawCircle(self, vert, diam): 
    print("drawCircle:", vert)
    vert = self.calcNormLatLong(vert[0], vert[1])
    cr   = self.ctx

    cr.set_source_rgb(1,0,0)
    cr.set_line_width(0.02)

    cr.save()
    cr.translate(vert[0], vert[1])
    cr.set_source_rgb(0.7, .2, .2)
    cr.arc(0, 0, diam, 0, 2*math.pi)
    cr.stroke_preserve()
        
    #cr.fill()
    cr.restore()
    cr.stroke()

  ################ plotLatLong ################ 

  def plotLatLong(self): 
    #latTick  = [30,40,50]
    print("plotLatLong")

    minLat = 30; maxLat = 48
    for long in self.longTick:
      print("long:", long)
      #self.ctx.save()

      v1 = self.calcNormLatLong(long, minLat)
      v2 = self.calcNormLatLong(long, maxLat)
      self.ctx.move_to(v1[0], v1[1])
      self.ctx.line_to(v2[0], v2[1])
   
      self.ctx.set_source_rgb(1,0,0)
      self.ctx.set_line_width(0.002)
      #self.ctx.stroke_preserve()
      #self.ctx.restore()
      self.ctx.stroke()

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

    lis = normVerts[-1] #last in sequence
    if lastX != lis[0] or lastY != lis[1]: # in case last close, avoiding gaps
        self.ctx.line_to(lis[0], lis[1])

    self.ctx.line_to(vert[0], vert[1])
   
    c = self.lineColor
    self.ctx.set_source_rgb(c[0], c[1], c[2])
    #self.ctx.set_line_width(0.06)
    self.ctx.set_line_width(0.01)
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
    
    print([self.latMin, self.latMax, self.longMin, self.longMax])
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
