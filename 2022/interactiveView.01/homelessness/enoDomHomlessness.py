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

  ####################### read YAML #######################

    
categories: [health, food, housing, employment, transit, goods]

descriptions:
  health:     {icon: dkdc_health1,     visuals: []}
  food:       {icon: dkdc_food1,       visuals: []}
  housing:    {icon: dkdc_housing1,    visuals: []}
  employment: {icon: dkdc_employment1, visuals: []}
  transit:    {icon: dkdc_transit1,    visuals: []}
  goods:      {icon: dkdc_goods1,      visuals: []}

### end ###

