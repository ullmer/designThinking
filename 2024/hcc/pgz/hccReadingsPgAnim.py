# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

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

  actorDefaultSize       = (335,94)
  actorhaloPad           = 5    #pixel padding (initially, same in X and Y)

  ################## constructor, error ##################

  def __init__(self): 
    super().__init__()
    self.transpBoundingBoxAnimDirection = {}
    self.transpBoundingBoxAnimPair      = {}
    
  def err(self, msg): print("ReadingPgAnim error:", msg); traceback.print_exc()
  
################## calculate actor "halo" dimensions ################## 

  def calcActorHaloDim(self, actor): 
    
    

################## draw ################## 

  def draw(self, screen): 
    super().draw(screen)


################## main ################## 

#if __name__ == "__main__":

rpga = ReadingsPgAnim()

def draw(): screen.clear(); rpga.draw(screen)
def on_mouse_down(pos):     rpga.on_mouse_down(pos)

### end ###
