# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

from PIL import Image, ImagePgz
from enoDomHomelessness import *

class enoUiHomelessnessPgz:

  edh    = None  #enoDomHomelessness
  actors = None 
  actor2category = None 

  ####################### constructor #######################

  def __init__(self, tkParent):
    self.edh = enoDomHomelessness()
    self.buildUI()

  ####################### build UI #######################

  def buildUI(self, tkParent):
    self.actors = {}; self.actor2category = {}
    
    categories = self.edh.getCategories()
    for category in categories:
      imgFn1 = self.edh.getImageFn(category)
      a1   = Actor(imgFn1, pos=)
      self.actors[category]   = a1
      self.actor2category[a1] = category

    self.tkFrame.pack()

  ####################### draw #######################

  def draw(self):
    for actor in self.actors: actor.draw()

  ####################### draw #######################

  def onMouseDown(self, pos):
    for actor in self.actors: 
      if actor.collidepoint(pos): 
        category = self.actor2category[actor]

####################### main #######################
if __name__ == '__main__':
  top = tk.Pgz()
  enoUiH = enoUiHomelessnessPgz(top)
  top.mainloop()

### end ###
