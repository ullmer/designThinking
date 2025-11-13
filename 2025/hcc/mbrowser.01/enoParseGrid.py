# Segment spatial input from regular arrays (initially, touch on grids)
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

from ataBase   import *
from functools import partial

class EnoParseGrid(AtaBase):

  rows, cols   = None, None
  x0, y0       = None, None
  pixDim       = None
  gridBindings = None

  callbacks       = None
  callbacksActive = False

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# set grid binding #############

  def setGridBinding(self, row, col, binding):
    try:
      if self.gridBindings is None: self.gridBindings = {}
      self.gridBindings[(row, col)] = binding
    except: self.err("setGridBinding"); return None

  def printGridBindings(self): self.msg("printGridBindings: " + str(self.gridBindings))

  ############# set grid binding #############

  def setGridCallback(self, row, col, callback):
    try:
      if self.callbacks is None: self.callbacks = {}
      self.callbacks[(row, col)] = callback

    except: self.err("setGridCallback"); return None

  ############# get grid binding #############

  def getGridCallback(self, row, col):
    try:
      if self.callbacks is None: 
        self.msg("getGridCallback: callbacks unpopulated"); return None
      result = self.callbacks((row,col))
      return result

    except: self.err("getGridCallback"); return None

  ############# set grid bindings #############

  def setGridBindings(self, bindings):
    try:
      if self.gridBindings is None: self.gridBindings = {}
      idx = 0
      numBindings = len(bindings)

      for j in range(self.rows):
        for i in range(self.cols):
          if idx < numBindings: self.gridBindings[(i, j)] = bindings[idx]
          idx += 1
      self.msg("sgb: " + str(idx) + str(bindings))
    except: self.err("setGridBindings")

  ############# set grid callbacks #############

  def setGridCallbacks(self, callback): #map a single parameter-receiving callback via partials
    try:
      if self.callbacks is None: self.callbacks = {}
      numCallbacks = len(callbacks)

      for i in range(self.cols):
        for j in range(self.rols):
          cb = partial(callback, (i, j))
          self.callbacks[(i, j)] = cb

    except: self.err("setGridCallbacks")

  ############# keyFieldsPopulated #############

  def keyFieldUnpopulated(self):
    try:
      for el in [self.cols, self.rows, self.x0, self.y0, self.pixDim]:
        if el is None: return True
      return  False

    except: self.err("keyFieldsPopulated"); return None

  ############# collidepoint #############

  def collidepoint(self, pos): #determine whether pos collides with our known bounds
    try:
      if self.keyFieldUnpopulated(): self.msg("parseLocus: key field unpopulated!"); return None

      width, height = self.pixDim
      x,  y         = pos
      x1, y1        = self.x0 + width, self.y0 + height

      if x < self.x0 or y < self.y0 or x > x1 or y > y1:
        return False
      return True

    except: self.err("collidepoint"); return None

  ############# map tabular index to 2D position #############

  def mapIdx2Pos(self, row, col):
    try:
      if self.keyFieldUnpopulated(): 
        self.msg("mapIdx2Pos called with key fields unpopulated"); return None
      w,   h = self.pixDim
      dw, dh = w/self.cols, h/self.rows
      x,   y = x0 + col * dw, y0 + row * dh
      return (x,y)

    except: self.err("mapIdx2Pos"); return None

  ############# determine grid position #############

  def determineGridPos(self, pos):
    try:
      if self.keyFieldUnpopulated(): 
        self.msg("determineGridPos called with key fields unpopulated"); return None

      x,         y = pos
      w,         h = self.pixDim
      relX,   relY = x - self.x0, y - self.y0
      normX, normY = relX / w, relY / h
      fx,       fy = normX * self.cols, normY * self.rows
      gx,       gy = int(fx), int(fy) 

      if self.verbose: pass
        #self.msg("determineGridPos: relXY: " + str([relX, relY]))
        #self.msg("determineGridPos: fXY: " + str([fx, fy]))
        #self.msg("determineGridPos: gXY: " + str([gx, gy]))

      return((gx, gy))

    except: self.err("determineGridPos"); return None

  ############# determine grid binding #############

  def determineGridBinding(self, pos):
    try:
      gridPos = self.determineGridPos(pos)
      if gridPos is None: 
        self.msg("determineGridBinding observes problem response from determineGridPos"); return None

      if gridPos in self.gridBindings: return gridBindings[gridPos]
      self.msg("determineGridBindings receives unbound coordinate"); return None

    except: self.err("determineGridBindings"); return None

  ############# parseLocus #############

  def parseLocus(self, pos):
    try:
      intersectingPos = self.collidepoint(pos)
      if intersectingPos is None:  self.msg("parseLocus detects collidepoint issue"); return None
      if intersectingPos is False: return False

      gridPos = self.determineGridPos(pos)
      if self.callbacksActive:
        if gridPos in self.callbacks: 
          try:    self.callbacks[gridPos]()
          except: self.err("parseLocus error on autocallback")

      result = [gridPos]
      if self.verbose: self.msg(gridPos)

      if self.gridBindings is not None and gridPos in self.gridBindings: 
        gb = self.gridBindings[gridPos]
        result.append(gb)
        if self.verbose: self.msg(gb)

      if self.callbacksActive:
        try:
          row, col = gridPos
          cb = self.getGridCallback(row, col)
          cb(gridPos)
        except: self.err("parseLocus error on calling cb with " + str(gridPos))

      return result

    except: self.err("parseLocus"); return None

### end ###
