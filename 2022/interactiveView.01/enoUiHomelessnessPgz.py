# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

from enoDomHomelessness import *

class enoUiHomelessnessPgz:

  edh    = None  #enoDomHomelessness
  actors = None 
  actor2category   = None 
  actor2homePos    = None 
  category2actor   = None
  selectedCategory = None

  animateSelectedRight = True # if true, animate selected objects to right
  animateDuration      = .5
  animateTween         = 'accel_decel'
  selectedXOffset      = 200

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
    self.actors = [];         self.actor2homepos = {}
    self.actor2category = {}; self.category2actor = {}
    
    categories = self.edh.getCategories()

    for category in categories:
      imgFn = self.edh.getImageFn(category)
      pos   = (self.currentX, self.currentY)
      a1    = Actor(imgFn, topleft=pos)

      self.actors.append(a1)
      self.actor2category[a1]       = category
      self.category2actor[category] = a1
      self.actor2homepos[category]  = pos
      self.currentY                += self.edh.yOffset

  ####################### draw #######################

  def animateSelected(self, category):
    a1      = self.category2actor[category]
    x, y    = self.actor2homepos[category]
    x += self.selectedXOffset      

    if self.animateSelectedRight:
      d = self.animateDuration; t = self.animateTween
      animate(a1, topleft=(x, y), duration=d, tween=t)

  ####################### draw #######################

  def draw(self):
    for actor in self.actors: actor.draw()

  ####################### draw #######################

  def onMouseDown(self, pos):
    for actor in self.actors: 
      if actor.collidepoint(pos): 
        category = self.actor2category[actor]
        print("pushed:", category)
        self.animateSelected(category)

####################################################

enoUiH = enoUiHomelessnessPgz()
#enoUiH = enoUiHomelessnessPgz(currentX=200, currentY=75)

####################### draw #######################
def draw():
  screen.clear()
  enoUiH.draw()

####################### draw #######################
def on_mouse_down(pos):
  enoUiH.onMouseDown(pos)

### end ###

