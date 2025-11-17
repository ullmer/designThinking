# Enodia entity listing
# Brygg Ullmer, Clemson University
# Begun 2025-11-12

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

class EnoEntityListing(AtaBase):
  entries        = None
  entryFontName  = "barlow_condensed_extralight"
  entryFontSize  = 32
  entryFontAlpha = .8
  entryFontColor = (250, 250, 250, 150)
  entryFontAngle = 0

  winDim = None
  rowDim = None
  defaultRowHeight = 30
  defaultRowShift  = (0, -12)

  drawRowBands        = True
  rowBandsAlternating = True

  rowBand1 = (40, 40, 40, 80)
  rowBand2 = (20, 20, 20, 60)
  rowBandLastColor = None

  fieldsToPostfix = None
  postfix         = ':'

  entryFieldWidths      = None
  offsetsBetweenEntries = None
  defaultFieldWidths    = 100
  basePos               = (20, 200)

  #defaultOffsetBetweenEntries = (0, 35)
  defaultOffsetBetweenEntries = 35 #if not tuple, consider as dy

  ############# constructor #############

  def __init__(self, **kwargs):
    try:
      self.__dict__.update(kwargs) #allow class fields to be passed in constructor
      if self.entries is None: self.entries = []
 
      if self.rowDim is None and self.winDim is not None:
        w, h = self.winDim
        self.rowDim = (w, self.defaultRowHeight)

    except: self.err("constructor")

  ############# add entry #############

  def addEntry(self, entry): 
    if not isinstance(self.entries, list):
      self.msg("addEntry issue: internal entries not populated with a list!")
      return False

    try:    self.entries.append(entry)
    except: self.err("addEntry")

  ############# draw #############

  def drawEntry(self, screen, entry, pos):
    try:
      # if not already a list, make it one
      if not isinstance(entry, list): entry = [str(entry)]

      numFields = len(entry)
      if self.entryFieldWidths is None: self.entryFieldWidths = []
      lefw = len(self.entryFieldWidths)

      if numFields > lefw:
        numFieldWidthsToAdd = numFields - lefw
        dfw = self.defaultFieldWidths
        for i in range(numFieldWidthsToAdd): 
          self.entryFieldWidths.append(dfw)

      x,  y   = pos; idx = 0
      an      = self.entryFontAngle 
      fn, fs  = self.entryFontName,  self.entryFontSize
      a,  c   = self.entryFontAlpha, self.entryFontColor
      ftp, pf = self.fieldsToPostfix, self.postfix

      if self.drawRowBands:
        rbcol = self.rowBand1
        if self.rowDim is None: self.msg("drawEntry trying to draw row bands, but row dimensions unknown"); return 

        if (self.rowBandLastColor is None or self.rowBandLastColor == 1): self.rowBandLastColor = 0
        else:                                      rbcol = self.rowBand2; self.rowBandLastColor = 1

        dx, dy = self.defaultRowShift  
        rpos = (x+dx, y+dy)

        r = Rect(rpos, self.rowDim)
        screen.draw.filled_rect(r, rbcol)

      for field in entry: 
        w = self.entryFieldWidths[idx]

        #self.msg("drawEntry: " + str([field,x,y,a,c,fn,fs,an]))
        strf = str(field)
        if ftp is not None and idx in ftp: strf += pf #add postfix

        screen.draw.text(strf, midleft=(x,y), \
          alpha=a, color=c, fontname=fn, fontsize=fs, angle=an)

        x += w; idx += 1
    except: self.err("drawEntry")

  ############# draw #############

  def draw(self, screen):
    try: 
      #if self.verbose: self.msg("draw begun")
      if not isinstance(self.entries, list):
        self.msg("draw issue: internal entries not populated with a list!")
        return False

      x,   y = self.basePos

      numEntries = len(self.entries)
      if not isinstance(self.offsetsBetweenEntries, list):
        self.offsetsBetweenEntries = []

      lobe = len(self.offsetsBetweenEntries)
      if lobe < numEntries:
        numToAdd = numEntries - lobe
        dobe     = self.defaultOffsetBetweenEntries
        for i in range(numToAdd): self.offsetsBetweenEntries.append(dobe)

      idx = 0
      for  entry in self.entries: 
        self.drawEntry(screen, entry, (x, y))

        obe = self.offsetsBetweenEntries[idx]
        if isinstance(obe, tuple): dx, dy = obe; x += dx
        else:                      dy     = obe
        y   += dy
        idx += 1
        #self.msg("draw: " + str([idx,x,y]))

      #self.msg("draw ends, idx: " + str(idx))

    except: self.err("draw")

### end ###
