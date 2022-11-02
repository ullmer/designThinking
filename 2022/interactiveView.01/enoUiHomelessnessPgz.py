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

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.edh = enoDomHomelessness()
    self.buildUI()

  ####################### build UI #######################

  def buildUI(self):
    self.actors = []; self.actor2category = {}
    
    categories = self.edh.getCategories()

    for category in categories:
      imgFn = self.edh.getImageFn(category)
      a1    = Actor(imgFn, topleft=(self.currentX, self.currentY))

      self.actors.append(a1)
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
        print("pushed:", category)

####################################################

enoUiH = enoUiHomelessnessPgz()
#enoUiH = enoUiHomelessnessPgz(currentX=200, currentY=75)

####################### draw #######################
def draw():
  enoUiH.draw()

####################### draw #######################
def on_mouse_down(pos):
  enoUiH.onMouseDown(pos)

### end ###

