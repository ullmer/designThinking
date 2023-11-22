# Convert YAML listing to Prolog
# Brygg Ullmer, Clemson University
# Begun 2023-11-21

# Example YAML text-file representation content:
# - {biaCode: 604, epaId: 100000091, states: [AZ, CA, NV], name: "Fort Mojave Indian Tribe of Arizona, California & Nevada"}
# - {biaCode: 803, epaId: 100000092, states: [AZ, NM, OK], name: "Fort Sill Apache Tribe of Oklahoma"}
# - {biaCode: 780, epaId: 100000171, states: [AZ, NM, UT], name: "Navajo Nation, Arizona, New Mexico, & Utah"}
# - {biaCode: 304, epaId: 100000311, states: [MT, ND, SD], name: "Turtle Mountain Band of Chippewa Indians of North Dakota"}
# - {biaCode: 603, epaId: 100000051, states: [AZ, CA], name: "Colorado River Indian Tribes of the Colorado River Indian Reservation, Arizona and California"}

import yaml, sys, traceback

###################### yaml to prolog ######################

class yaml2pl:
  yamlFn = None
  yamlD  = None
  ourPl  = None
  basePredicate = None

  ################### constructor ###################

  def __init__(self, **kwargs): 
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.loadYaml()
    self.genPl()

  ################### load YAML ###################

  def loadYaml(self):
    if self.yamlFn is None: print("yaml2pl loadYaml error: yaml filename unspecified"); sys.exit(-1)
    yamlF = open(self.yamlFn, 'rt')
    self.yamlD = yaml.safe_load(yamlF)
  
  ################### generate prolog ###################

  def genPl(self): 
    if self.basePredicate is None: print("yaml2pl genPl requires basePredicate to be specified"); sys.exit(-1)

    for row in self.yamlD:
      try:
        plstr = self.basePredicate + "("
        keys = []
        for key in row: keys.append(str(row[key]))
        plstr += ", ".join(keys)
        plstr += ");"
        print(plstr)
      except:
        print("<<ignoring ", row); print(traceback.print_exc())

###################### main ######################

ourYamlFn = 'tribe_entity_mapping_2021-03-04.yaml'
ourPlFn   = 'tribe_entity_mapping_2021-03-04.pl'
ourBasePredicate = 'tribe'

y2p = yaml2pl(yamlFn=ourYamlFn, plFn=ourPlFn, basePredicate=ourBasePredicate)

### end ###
