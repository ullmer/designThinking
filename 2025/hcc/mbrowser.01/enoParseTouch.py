# Segment spatial input from regular arrays (initially, touch on grids)
# Brygg Ullmer, Clemson University
# Begun 2025-11-06

import ataBase

class EnoParseTouch(AtaBase):

  cols, rows = None, None
  x0, y0     = None, None
  pixDim     = None
  bindings   = None

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor

  ############# keyFieldsPopulated #############

  def keyFieldUnpopulated(self):
    try:
      for el in [self.cols, self.rows, self.x0, self.y0, self.pixDim]:
        if el is None: return True
      return  False

    except: self.err(keyFieldsPopulated); return None

  ############# parseLocus #############

  def parseLocus(self, pos):
    if self.keyFieldUnpopulated(): self.msg("parseLocus: key field unpopulated!"); return None

### end ###
