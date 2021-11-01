# Synthesize bolts within SolidPython
# Brygg Ullmer, Clemson University
# Begun 2021-10-31

from solid import *
from solid.utils import *
import yaml

#############################################
############### mcmaster bolt ###############

class mcmBolt: 
  yfn = 'bolts.yaml'
  yd  = None

############### constructor ###############

def __init__(self):
  self.loadYaml()

############### load YAML ###############

def loadYaml(self):
  yf = open(self.yfn, 'r+t')
  self.yd = yaml.safe_load(yf)
  yf.close()

############### mcmBolt ###############

def getBoltspecs(self):
  try:    keys = self.yd.keys()
  except: print("mcmBolt:getBoltspecs"); traceback.print_exc()
  return keys

############### mcmBolt ###############

def synthBolt(self, boltspec):
  try:    stlFn = self.yd[boltspec]['stl']
  except: print("mcmBolt:", boltspec); traceback.print_exc()

  result = import_stl(stlFn)
  return result 

############### mcmBolt ###############

def synthBoltPos(self, boltspec, pos):
  boltGeom = self.synthBolt(boltspec)
  result   = translate(pos)(boltGeom)
  return result

### end ###

