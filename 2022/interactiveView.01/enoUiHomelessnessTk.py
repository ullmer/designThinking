# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

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

    except: print("Problem in enoDomHomelessness:readYaml")

  ####################### get categories #######################

  def getCategories(self): return self.categories

  ####################### get description #######################

  def getDescr(self, descr):
    if descr in self.descriptions:
      return self.descriptions[descr]
    return None

####################### main #######################
if __name__ == '__main__':
  edh = enoDomHomelessness()
  print(edh.getCategories())

### end ###

