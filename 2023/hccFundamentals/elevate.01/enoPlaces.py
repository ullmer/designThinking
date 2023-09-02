# Enodia Launch functions
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

import yaml, traceback

from pgzero.builtins import Actor, animate, keyboard
#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

##################### pygamezero button #####################

class enoPlaces:
  fontSize   = 36
  yamlFn      = None #YAML filename; e.g., elevatePlaces01.yaml
  yamlD       = None #YAML data import
  dx, dy      = 0, 0
  screenWidth, screenHeight = 1200, 940

  glyphNormDict  = None
  glyphDimDict   = None
  glyphBriteDict = None

  workspace     = None
  placeTypeList = None

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.glyphNormDict, self.glyphDimDict, self.glyphBriteDict = {}, {}, {}
    self.loadYaml(yamlFn)

  ############# loadYaml #############

  def reportError(self, functionName, issue):
    try:
      errorMsg = "enoPlaces %s error: %s" % (functionName, issue)
      print(errorMsg)
    except: print("enoPlaces reportError error:"); traceback.print_exc(); return None

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
        self.processWorkspaceBounds()

    #placeTypes:
    #  #list: [ic, eo, rec, rh, es]
    #  typeList: [all]

    if 'placeTypes' in y:
      pts = self.placeTypes = y['placeTypes']
      if 'typeList' in pts:
        ptl = self.placeTypeList = pts['typeList']

      #  all:
      #    name:  All
      #    glyph: circle
      #    colorDefault: gray
      #    loci:
      #     - [ 16881,  45712]
      #     - [ 99478,  29738]
      #     - [ 51102,  40869]

      for ptypeName in ptl:
        ptype = pts[ptypeName]
        if 'loci' in ptype:
          loci = ptype['loci']
          self.processLoci(ptypeName, loci)

  ############# process workspace bounds #############

  def processWorkspaceBounds(self):
    #  workspace: {x: -34.9, y: 18641.4, width: 120000, height: 120000}

    w = self.workspace
    if w is None: self.reportError("processWorkspaceBounds", "self.workspace unassigned"); return None

    try:
      self.workspaceX,     self.workspaceY      = w['x'],     w['y']
      self.workspaceWidth, self.workspaceHeight = w['width'], w['height']

    except: self.reportError("processWorkspaceBounds," "xywh extraction error"); traceback.print_exc(); return None
    return True

  ############# process locus (single) #############

  def processLocus(self, ptypeName, locus):
    try:
      wx, wy, ww, wh = self.workspaceX, self.workspaceY, self.workspaceWidth, self.workspaceHeight
      sw, sh         = self.screenWidth, self.screenHeight
      x, y = locus
      sx = int((float(x) / float(ww) + wx) * sw)
      sy = int((float(y) / float(wh) + wy) * sh)
      return [sx, sy]

    except: self.reportError("processLocus", "exception caught"); traceback.print_exc(); return None

  ############# process loci (multiple) #############

  def processLoci(self, ptypeName, locii):

    try:
      y = self.yamlD  
      if y is None:             self.reportError("processLoci", "yaml data not yet loaded"); return None

      if 'placeTypes' not in y: self.reportError("processLoci", "placeTypes section not in yaml data!"); return None
      pts = y['placeTypes']

      if ptypeName not in pt:   self.reportError("processLoci", "ptypeName %s not in placeTypes" % ptypeName); return None
      pt = pts[ptypeName]
      
      if 'glyph100' not in pt:  self.reportError("processLoci", "glyph100 not in placeTypes " + ptypeName); return None

      glyphImgFn = pt['glyph100']

      self.glyphNormDict[ptypeName] = glyphImgFn

      for locus in locii:
        screenPos = self.processLocus(ptypeName, locii)
        a = Actor(glyphImgFn, pos = screenPos)
        self.addActor(a, ptypeName)

        #, pos = screenPos)

    #if  in self.yamlD:
    #  self.bgFn    = self.yamlD[self.bgFnTag]
    #  self.bgActor = Actor(self.bgFn)

  ############# pgzero draw #############

  def draw(self):
    if self.bgActor is not None: self.bgActor.draw()

### end ###

