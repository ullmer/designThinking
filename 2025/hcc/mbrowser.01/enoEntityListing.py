# Enodia entity listing
# Brygg Ullmer, Clemson University
# Begun 2025-11-12

from ataBase       import *
from enoPrism      import *
from enoPrismsTei  import *

class EnoEntityListing(AtaBase):
  entries          = None
  entryFont        = "barlow_condensed_extralight"
  entryFontSize    = 32

  entryFieldWidths = None

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

  def draw(self, screen):
    try: 
      if not isinstance(self.entries, list):
        self.msg("draw issue: internal entries not populated with a list!")
        return False

      for  entry in self.entries: self.drawEntry(entry)
    except: self.err("draw")

### end ###
