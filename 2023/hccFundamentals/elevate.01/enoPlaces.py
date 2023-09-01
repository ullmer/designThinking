# Enodia Launch functions
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

import yaml

from pgzero.builtins import Actor, animate, keyboard
#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

##################### pygamezero button #####################

class Places:
  fontSize   = 36
  yamlFn      = None #YAML filename; e.g., elevatePlaces01.yaml
  yamlD       = None #YAML data import

  bgFn        = None
  bgFnTag     = 'bgFn'
  bgActor     = None

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml(yamlFn)

  ############# loadYaml #############

  def loadYaml(self, yamlFn):
    self.yamlFn = yamlFn
    yf          = open(yamlFn, 'rt')
    self.yamlD  = yaml.safe_load(yf)

    if self.bgFnTag in self.yamlD:
      self.bgFn    = self.yamlD[self.bgFnTag]
      self.bgActor = Actor(self.bgFn)

  ############# pgzero draw #############

  def draw(self):
    if self.bgActor is not None: self.bgActor.draw()

### end ###
