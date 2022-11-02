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

  animationId          = 1 #1, 2, perhaps more: different patterns of animation
  animateDuration      = .5
  animateTween         = 'accel_decel'
  selectedXOffset1     = 200
  selectedXOffset2     = 200

  basePos           = (0, 0)
  basePosUnselected = (400, 400)
  basePosSelected   = (0, 0)

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

    x, y = self.basePos

    for category in categories:
      imgFn = self.edh.getImageFn(category)
      pos   = (x, y)
      a1    = Actor(imgFn, topleft=pos)

      self.actors.append(a1)
      self.actor2category[a1]       = category
      self.category2actor[category] = a1
      self.actor2homepos[category]  = pos
      y                            += self.edh.yOffset

  ####################### animate selected #######################

  def animateSelected(self, category):
    aId = self.animationId

    if aId == 1: self.animateSelectedRight1(category)
    if aId == 2: self.animateSelectedRight2(category)
  
####################### animate selected : simple right-animation #######################

  def animateSelectedRight1(self, category): # simpler animation, albeit less useful 
      d = self.animateDuration; t = self.animateTween

      if self.selectedCategory is not None:
        sc = self.selectedCategory
        a2 = self.category2actor[sc]
        x2, y2 = self.actor2homepos[sc]
        animate(a2, topleft=(x2,y2), duration=d, tween=t)
  
      a1  = self.category2actor[category]
      x,y = self.actor2homepos[category]
      x  += self.selectedXOffset1
      animate(a1, topleft=(x, y), duration=d, tween=t)
      self.selectedCategory = category

####################### animate selected : more evolved right-animation #######################

  def animateSelectedRight2(self, category): # simpler animation, albeit less useful 
      d = self.animateDuration; t = self.animateTween
      categories = self.edh.getCategories()

      sx, sy = self.basePosUnselected #sx, sy: side x, y, for unselected

      if self.selectedCategory is not None:
        for c in categories:
          if c == category: continue #bypass match for unselected sidebar
          a2     = self.category2actor[category]
          sy    += self.edh.yOffset
          animate(a2, topleft=(sx,sy), duration=d, tween=t)
  
      a1  = self.category2actor[category]
      x,y = self.basePosSelected
      animate(a1, topleft=(x, y), duration=d, tween=t)
      self.selectedCategory = category

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

####################### draw #######################
def draw():
  screen.clear()
  enoUiH.draw()

####################### on_mouse_down #######################
def on_mouse_down(pos):
  enoUiH.onMouseDown(pos)

### end ###

