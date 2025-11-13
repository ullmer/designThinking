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
  entryFontAlpha = .1
  entryFontColor = (200, 200, 200, 100)
  entryFontAngle = 0

  entryFieldWidths      = None
  offsetsBetweenEntries = None
  defaultFieldWidths    = 50
  basePos               = (100, 100)

  #defaultOffsetBetweenEntries = (0, 35)
  defaultOffsetBetweenEntries = 35 #if not tuple, consider as dy

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    if self.entries is None: self.entries = []

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

      x,  y  = pos; idx = 0
      an     = self.entryFontAngle 
      fn, fs = self.entryFontName,  self.entryFontSize
      a,  c  = self.entryFontAlpha, self.entryFontColor

      for field in entry: 
        w = self.entryFieldWidths[idx]

        screen.draw.text(str(field), midleft=(x,y), \
          alpha=a, color=c, fontname=fn, fontsize=fs, angle=an)

        x += w; idx += 1
    except: self.err("drawEntry")

  ############# draw #############

  def draw(self, screen):
    try: 
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

    except: self.err("draw")

### end ###
