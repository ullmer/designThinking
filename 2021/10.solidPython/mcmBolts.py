# Synthesize bolts within SolidPython
# Brygg Ullmer, Clemson University
# Begun 2021-10-31

from solid import *
from solid.utils import *
import yaml, traceback

#############################################
############### mcmaster bolt ###############

class mcmBolts: 
  yfn = 'bolts.yaml'
  yd  = None
  fullheightHash = None 
  boltnames      = None 

  ############### load YAML ###############
  
  def loadYaml(self):
    yf = open(self.yfn, 'r+t')
    self.yd = yaml.safe_load(yf)
    yf.close()

    self.fullheightHash = {}
    self.boltnames      = []

    try:    self.boltnames = self.yd['boltnames']
    except: print("mcmBolts::loadYaml"); traceback.print_exc()

    try:
      for boltname in self.boltnames:
        stemHeight = self.yd[boltname]['stemHeight']
        headHeight = self.yd[boltname]['headHeight']
        fullHeight = stemHeight + headHeight
        self.fullheightHash[boltname] = fullHeight
    except: print("mcmBolts::loadYaml"); traceback.print_exc()
  
  ############### constructor ###############
  
  def __init__(self):
    self.loadYaml()
  
  ############### getFullHeight ###############
  
  def getFullHeight(self, boltname):
    fullHeight = None
    try:    fullHeight = self.fullheightHash[boltname]
    except: print("mcmBolts::getFullHeight"); traceback.print_exc()
    return fullHeight

  ############### getHeadWidth ###############
  
  def getHeadWidth(self, boltname):
    try:    headWidth = self.yd[boltname]['headWidth']
    except: print("mcmBolts::getHeadWidth"); traceback.print_exc()
    return  headWidth

  ############### getHeadHeight ###############
  
  def getHeadWidth(self, boltname):
    try:    headHeight = self.yd[boltname]['headHeight']
    except: print("mcmBolts::getHeadHeight"); traceback.print_exc()
    return  headHeight

  ############### mcmBolt ###############
  
  def getBoltspecs(self):
    bolts = None
    try:    bolts = self.yd['boltnames']
    except: print("mcmBolt:getBoltspecs"); traceback.print_exc()
    return bolts
  
  ############### mcmBolt ###############
  
  def synthBolt(self, boltspec):
    stlFn = None
    try:    
      bolt  = self.yd[boltspec]
      stlFn = bolt['stl']
    except: print("mcmBolt:", boltspec); traceback.print_exc()
  
    result = import_stl(stlFn)
    return result 
  
  ############### mcmBolt ###############
  
  def synthBoltPos(self, boltspec, pos):
    boltGeom = self.synthBolt(boltspec)
    result   = translate(pos)(boltGeom)
    return result

### end ###

