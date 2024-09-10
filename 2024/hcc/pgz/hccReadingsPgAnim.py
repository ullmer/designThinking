# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsYaml  import *
from enoGlyphArrayPgz import *

WIDTH, HEIGHT = 1200, 800

################### readingsPg ################### 

class ReadingsPgAnim(ReadingsPg):

  displayTranspBoundingBox       = True
  transpBoundingBoxAnimDirection = None
  transpBoundingBoxAnimPair      = None

  ################## constructor, error ##################

  def __init__(self): 
    super().__init__()
    self.transpBoundingBoxAnimDirection = {}
    self.transpBoundingBoxAnimPair      = {}
    
  def err(self, msg): print("ReadingPgAnim error:", msg); traceback.print_exc()

################## draw ################## 

  def draw(self, screen): 
    super().draw(screen)


################## main ################## 

#if __name__ == "__main__":

rpga = ReadingsPgAnim()

def draw(): screen.clear(); rpga.draw(screen)
def on_mouse_down(pos):     rpga.on_mouse_down(pos)

### end ###
