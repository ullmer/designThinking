# Segment spatial input from regular arrays (initially, touch on grids)
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import ataBase

class EnoParseGrid(AtaBase):

  cols, rows   = None, None
  x0, y0       = None, None
  pixDim       = None
  gridBindings = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# set grid binding #############

  def setGridBinding(self, row, col, binding):
    try:
      if self.gridBindings is None: self.gridBindings = {}
      self.gridBindings[(row, col)] = binding
    except: self.err("setGridBinding"); return None

  ############# set grid bindings #############

  def setGridBindings(self, bindings):
    try:
      if self.gridBindings is None: self.gridBindings = {}
      idx = 0
      numBindings = len(bindings)

      for i in range(self.cols):
        for j in range(self.rols):
          if idx < numBindings: self.gridBindings[(i, j)] = bindings[idx]
          idx += 1
    except: self.err("setGridBindings")

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

  ############# parseLocus #############

  def parseLocus(self, pos):
    try:
      intersectingPos = self.collidepoint(pos)
      if intersectingPos is None:  self.msg("parseLocus detects collidepoint issue"); return None
      if intersectingPos is False: return False

      gridPos = self.determineGridPos(pos)

    except: self.err("parseLocus"); return None

### end ###
