# Enodia Launch functions
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

import yaml

##################### pygamezero button #####################

class enoLaunch:
  = (0,0)
  buttonDim  = (100, 30)
  buttonRect = None
  buttonText = "actor"
  bgcolor1   = (0, 0, 130)
  bgcolor2   = (50, 50, 250)
  fgcolor    = "#bbbbbb"
  alpha      = .8
  fontSize   = 36
  imgFn      = None
  actor      = None # for image/sprite
  abbrev     = None # name/identity/handle

  toggleMode  = True
  toggleState = False

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

  ############# loadYaml #############

  def loadYaml(self, yamlFn):

  ############# pgzero draw #############

  def draw(self):
    pass #return self.actor.draw()

### end ###
