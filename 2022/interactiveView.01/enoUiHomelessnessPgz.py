# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

from enoDomHomelessness import *

class enoUiHomelessnessPgz:

  edh    = None  #enoDomHomelessness
  actors = None 
  actor2category = None 

  currentX = 0
  currentY = 0

  ####################### constructor #######################

  def __init__(self):
    self.edh = enoDomHomelessness()
    self.buildUI()

  ####################### build UI #######################

  def buildUI(self):
    self.actors = {}; self.actor2category = {}
    
    categories = self.edh.getCategories()
    for category in categories:
      print(category)
      imgFn1 = self.edh.getImageFn(category)
      a1   = Actor(imgFn1, pos=(self.currentX, self.currentY))
      self.actors[category]   = a1
      self.actor2category[a1] = category
      self.currentY += self.edh.yOffset

  ####################### draw #######################

  def draw(self):
    for actor in self.actors: actor.draw()

  ####################### draw #######################

  def onMouseDown(self, pos):
    for actor in self.actors: 
      if actor.collidepoint(pos): 
        category = self.actor2category[actor]

####################################################

enoUiH = enoUiHomelessnessPgz()

####################### draw #######################
def draw():
  enoUiH.draw()

####################### draw #######################
def on_mouse_down(pos):
  enoUiH.onMouseDown(pos)

### end ###

