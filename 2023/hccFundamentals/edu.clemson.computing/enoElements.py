#Enodia People 
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

import yaml, traceback

import pgzrun 
#from pgzhelper import *

from pgzero.builtins import Actor, animate, keyboard
#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

#############################################################
################# Enodia Element Clusters ###################

# Cluster a series of elements into subclusters, each with distinctive associated positions

class enoElClusters:
  x1,y1 = 5,    5    # spatial stage coordinates
  dx,dy = 220,  130
  xm,ym = 1300, 700
  padX  = 20
  verbose = False

  clustersName = 'Unnamed cluster'

  clusterNames = None
  elPositions  = None
  clusterEls   = None

  ######################### constructor #########################

  def __init__(self, clustersDict):
    self.clusterNames = [] #list of cluster names
    self.elPositions  = {} #hash of element positions
    self.clusterEls   = {} #hash of cluster-name to element-lists

    self.buildClusters(clustersDict)
        
  ######################### printSummary #########################

  def printSummary(self):
    hash = '#' * 10; header = hash + self.clustersName + hash
    print(header)
    for clusterName in self.clusterNames:
      els = self.clusterEls[clusterName]
      print(clusterName, ':', els)
    print(self.elPositions)

  ######################### buildClusters #########################

  def buildClusters(self, clustersDict):

    if self.verbose: print("buildClusters:", clustersDict)
    self.clusterNames = clustersDict.keys()
    x,y = self.x1, self.y1 # start at declared origin 

    for clusterName in self.clusterNames:
       els = clustersDict[clusterName]

       if self.verbose: print("clusterName:", clusterName); print("els:", els)
       self.clusterEls[clusterName] = els

       for el in els:
         pos = (x, y)
         self.elPositions[el] = pos

         if y < self.ym: y += self.dy
         else:           y  = self.y1; x += self.dx
       #except: print(traceback.print_exc()); return None

       y = self.y1
       x += self.dx + self.padX

###############################################################
######################### enoElements #########################

class enoElements:
  x1,y1 = 5,    5
  dx,dy = 220,  130
  xm,ym = 1300, 700

  actors = None
  selectedActors = []
  actorLocationHistory = None
  clustersList = None
  clusterIdx   = 0

  ######################### constructor #########################

  def __init__(self, buildList):
    self.actors = {}
    self.actorLocationHistory = {}
    self.clustersList = []

    self.buildActors(buildList)
  
######################### buildActors #########################

  def buildActors(self, buildList):
    x,y = self.x1, self.y1 # start at declared origin 

    for lastname in buildList:
      try:
        imgFn = self.genImgFn(lastname)
        self.actors[lastname] = Actor(imgFn, topleft=(x, y))
        self.actorLocationHistory[lastname] = [(x,y)]

        if y < self.ym: y += self.dy
        else:           y  = self.y1; x += self.dx
      except: print(traceback.print_exc()); return None

######################### buildActors #########################

  def animToClusters(self, eeClusters):
    targetPositions = eeClusters.elPositions
    for lastname in self.actors.keys():
      if lastname in targetPositions:
        targetPosition = targetPositions[lastname]
        actor          = self.actors[lastname]
        animate(actor, tween='accel_decel', pos=targetPosition, duration=.7)

######################### buildActors #########################

  def genImgFn(self, lastname):
    lastn1 = lastname.replace(" ", "") #e.g., "Van Scoy" -> "VanScoy"
    lastn2 = lastn1.lower()
    imgFn  = lastn2 + '.png'
    return imgFn

  ######################### animate next cluster #########################

  def addCluster(self, cluster):
     self.clustersList.append(cluster)

  ######################### animate next cluster #########################

  def animNextCluster(self):
    clLen = len(self.clustersList); self.clusterIdx += 1

    if self.clusterIdx >= clLen: self.clusterIdx = 0
    cluster = self.clustersList[self.clusterIdx]

    self.animToClusters(cluster)
  
  ######################### animate cluster N#########################

  def animClusterN(self, clusterN):
    clLen = len(self.clustersList)
    if clusterN > clLen: return None
    cluster = self.clustersList[clusterN]
    self.animToClusters(cluster)

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    self.selectedActors = []

    for key in self.actors.keys():
      el = self.actors[key]
      if el.collidepoint(pos): 
        self.selectedActors.append(el)

        #x, y = el.center
        #animate(el, tween='accel_decel', pos=(x, y+100), duration=0.3)
        #el.scale = 2
        #animate(el, tween='accel_decel', width=el.width*2, duration=.7)
  
 ######################### on_mouse_move #########################

  def on_mouse_move(self, pos, rel):
    if self.selectedActors is None: return
    for actor in self.selectedActors:
      x,  y  = actor.center
      dx, dy = rel
      actor.center = (x+dx, y+dy)
  
######################### on_mouse_up #########################

  def on_mouse_up(self): 
    try:
      for lastname in self.selectedActors: # allows varying forms of "undo."  May wish to bound #
        actor = self.actors[lastname]
        currentPos = (actor.x, actor.y)
        self.actorLocationHistory[lastname].append(currentPos)

      self.selectedActors = []
    except: print("on_mouse_up error:", traceback.print_exc())
  
######################### draw #########################

  def draw(self):
    for key in self.actors.keys():
      self.actors[key].draw()

### end ###
