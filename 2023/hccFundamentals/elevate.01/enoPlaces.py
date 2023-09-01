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

  workspace     = None
  placeTypeList = None

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml(yamlFn)

  ############# loadYaml #############

  def loadYaml(self, yamlFn):
    self.yamlFn     = yamlFn
    yf              = open(yamlFn, 'rt')
    y = self.yamlD  = yaml.safe_load(yf)

    #base: 
    #  workspace: {x: -34.9, y: 18641.4, width: 120000, height: 120000}

    if 'base' in y:
      base = y['base']
      if 'workspace' in base:
        self.workspace = base['workspace']

    #placeTypes:
    #  #list: [ic, eo, rec, rh, es]
    #  typeList: [all]

    if 'placeTypes' in y:
      pt = self.placeTypes = y['placeTypes']
      if 'typeList' in pt:
         ptl = self.placeTypeList = pt['typeList']

    #if  in self.yamlD:
    #  self.bgFn    = self.yamlD[self.bgFnTag]
    #  self.bgActor = Actor(self.bgFn)



#  all:
#    name:  All
#    glyph: circle
#    colorDefault: gray
#    loci:
#     - [ 16881,  45712]
#     - [ 99478,  29738]
#     - [ 51102,  40869]


  ############# pgzero draw #############

  def draw(self):
    if self.bgActor is not None: self.bgActor.draw()

### end ###





