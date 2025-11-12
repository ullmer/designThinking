# Enodia entity listing
# Brygg Ullmer, Clemson University
# Begun 2025-11-12

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

class EnoEntityListing(AtaBase):
  entries          = None
  entryFontName    = "barlow_condensed_extralight"
  entryFontSize    = 32

  entryFieldWidths     = None
  defaultFieldWidths   = 50
  offsetBetweenEntries = (0, 35)
  basePos              = (100, 100)

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
        for i in numFieldWidthsToAdd: self.entryFieldWidths.append(dfw)

      x, y = pos; idx = 0
      for field in entry: 
        w     = self.entryFieldWidths[idx]
        f, fs = self.entryFontName, self.entryFontSize

        idx  += 1

  defaultFieldWidths = 50
  verticalOffset     = 35
  basePos            = (100, 100)

  ############# draw #############

  def draw(self, screen):
    try: 
      if not isinstance(self.entries, list):
        self.msg("draw issue: internal entries not populated with a list!")
        return False

      x,   y = self.basePos
      dx, dy = self.offsetBetweenEntries

      for  entry in self.entries: 
        self.drawEntry(entry, (x, y))
        x += dx; y += dy

    except: self.err("draw")

### end ###
