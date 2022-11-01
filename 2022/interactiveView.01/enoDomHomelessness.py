# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

import yaml

class enoDomHomelessness:

  yamlFn = "homelessness/dkdc01.yaml"

  yamlD        = None
  imagePath    = None
  yOffset      = None #placeholder assignments until read in or assigned
  xOffset      = None
  categories   = None
  descriptions = None

  ####################### constructor #######################

  def __init__(self):
    self.readYaml()

  ####################### read YAML #######################

  def readYaml(self):
    try:
      yf              = open(self.yamlFn)  #open yamlFn filename for reading
      yd = self.yamlD = yaml.safe_load(yf) #load and parse YAML content

      self.xOffset    = yd['positions']['xOffset']
      self.yOffset    = yd['positions']['yOffset']
      self.imagePath  = yd['paths']['images']

      self.categories   = yd['categories']
      self.descriptions = yd['descriptions']

    except: print("Problem in enoDomHomelessness:readYaml")

  ####################### get categories #######################

  def getCategories(self): return self.categories

  ####################### get Image Filename #######################

  def getImageFn(self, category): 
    descr = self.getDescr(category)
    

  ####################### get description #######################

  def getDescr(self, category):
    if category in self.descriptions:
      return self.descriptions[category]
    return None

####################### main #######################
if __name__ == '__main__':
  edh = enoDomHomelessness()
  print(edh.getCategories())

### end ###

