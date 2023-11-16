#PyGame Zero timeline module
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

import yaml, traceback

from pgzero.builtins import Actor, animate, keyboard
#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

###############################################################
######################### pgzTimeline #########################

class pgzTimeline:

  yfn    = 'elements.yaml'
  yf     = None
  yd     = None
  actors = None
  selectedActors = []

  ######################### constructor #########################

  def __init__(self, yamlFn):
    self.yfn = yamlFn
    self.actors = {}
    self.loadYaml()

  ######################### loadYaml #########################

  def loadYaml(self):
    try:
      self.yf  = open(self.yfn, 'r')
      self.yd  = yaml.safe_load(self.yf)
    except: print(traceback.print_exc()); return None

    try:
      for key in self.yd.keys():
        imgFn       = self.yd[key]['img']
        x           = self.yd[key]['x']
        self.actors[key] = Actor(imgFn, topleft=(x, 10), opacity = .5)
    except: print(traceback.print_exc()); return None

  ######################### on_mouse_down #########################

  def on_mouse_down(self, pos):
    self.selectedActors = []

    for key in self.actors.keys():
      el = self.actors[key]
      if el.collidepoint(pos): 
        #x, y = el.center
        #animate(el, tween='accel_decel', pos=(x, y+100), duration=0.3)
        self.selectedActors.append(el)
  
 ######################### on_mouse_move #########################

  def on_mouse_move(self, pos, rel):
    if self.selectedActors is None: return
    for actor in self.selectedActors:
      x,  y  = actor.center
      dx, dy = rel
      actor.center = (x+dx, y+dy)
  
######################### on_mouse_up #########################

  def on_mouse_up(self):
    self.selectedActors = []
  
######################### draw #########################

  def draw(self):
    for key in self.actors.keys():
      self.actors[key].draw()

### end ###
