# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsPg    import *
from hccReadingsYaml  import *
from enoGlyphArrayPgz import *

WIDTH, HEIGHT = 1200, 800

# relevant pgzero documentation:
#   https://pygame-zero.readthedocs.io/en/stable/builtins.html
#   https://github.com/lordmauve/pgzero/blob/master/pgzero/actor.py

################### readingsPg ################### 

class ReadingsPgAnim(ReadingsPg):

  displayActorHalo = True
  actorHaloAnimDirection = None #dict; are "halos" animating toward or away from their ~pair? 1=twd, 0=awy
  actorHaloAnimPair      = None #dict: "pair" for each actor (e.g., storage slot)
  actorHaloCoords        = None 
  glyphArrayPgz          = None

  actorDefaultSize       = (335,94)
  actorHaloPad           = 5    #pixel padding (initially, same in X and Y)


  ################## constructor, error ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    super().__init__()
    self.actorHaloAnimDirection = {}
    self.actorHaloAnimPair      = {}
    self.actorHaloCoords        = {}
    self.glyphArrayPgz          = enoGlyphArrayPgz()
    
  def err(self, msg): print("ReadingPgAnim error:", msg); traceback.print_exc()
  
################## calculate actor "halo" dimensions ################## 

  def calcActorHaloCoords(self, actor): 
    w, h = self.actorDefaultSize #brittle, but an initial expediency
    x, y = actor.pos
    pad  = self.actorHaloPad

    w2, h2 = w/2, h/2
    x1, y1 = x-w2-pad, y-h2-pad
    x2, y2 = x+w2+pad, y+h2+pad

    result = ((x1, y1), (x2, y2))
    return result

################## calculate "halo" dimensions for all actors, and cache ################## 

  def calcActorsHaloCoords(self): 
    if self.actors is None: self.err("calcActorsHaloCoords: no actors found"); return

    numActors = len(self.actors)

    for i in range(numActors):
      actor      = self.actors[i]
      haloCoords = self.calcActorHaloCoords(actor)
      self.actorHaloCoords[i] = halocoords
    
################## draw ################## 

  def draw(self, screen): 
    super().draw(screen)

################## main ################## 

#if __name__ == "__main__":

rpga = ReadingsPgAnim()

def draw(): screen.clear(); rpga.draw(screen)
def on_mouse_down(pos):     rpga.on_mouse_down(pos)

### end ###
