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

  ############### get bolt specs ###############
  
  def getBoltspecs(self):
    bolts = None
    try:    bolts = self.yd['boltnames']
    except: print("mcmBolt:getBoltspecs"); traceback.print_exc()
    return bolts
  
  ############### synth bolt ###############
  
  def synthBolt(self, boltspec):
    stlFn = None
    try:    
      bolt  = self.yd[boltspec]
      stlFn = bolt['stl']
    except: print("mcmBolt:", boltspec); traceback.print_exc()
  
    result = import_stl(stlFn)
    return result 
  
  ############### synth bolt pos ###############
  
  def synthBoltPos(self, boltspec, pos):
    boltGeom = self.synthBolt(boltspec)
    result   = translate(pos)(boltGeom)
    return result
  
  ############### synth bolt "neutral" position ###############
  
  def synthBoltNeutral(self, boltspec):
    boltHeight = float(self.getFullHeight(boltspec))
    stemHeight = float(self.yd[boltspec]['stemHeight'])
    #dz = boltHeight / 2 - stemHeight/2
    dz = -10 * boltHeight/2
    #dz = -1 * boltHeight
    boltGeom = self.synthBoltPos(boltspec, [0,0,dz])
    return boltGeom
  
  ############### synth bolt npos ###############
  
  def synthBoltNPos(self, boltspec, pos):
    boltGeom = self.synthBoltNeutral(boltspec)
    result   = translate(pos)(boltGeom)
    return result

### end ###

