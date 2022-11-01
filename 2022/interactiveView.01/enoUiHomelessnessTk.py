# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

import tkinter
import enoDomHomelessness

class enoUiHomelessnessTk:

  edh      = None  #enoDomHomelessness
  tkParent = None  #tk parent

  yamlD        = None
  imagePath    = None
  yOffset      = None #placeholder assignments until read in or assigned
  xOffset      = None
  categories   = None
  descriptions = None

  ####################### constructor #######################

  def __init__(self, tkParent):
    self.edh = enoDomHomelessness()
    self.buildUI(tkParent)

  ####################### build UI #######################

  def buildUI(self, tkParent):
    self.tkParent = tkParent 
    categories = self.edh.getCategories()
    for category in categories:

####################### main #######################
if __name__ == '__main__':
  enoUiH = enoUiHomelessness()

### end ###

