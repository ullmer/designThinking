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
  actorDict      = None

  workspace     = None
  placeTypeList = None

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.glyphNormDict, self.glyphDimDict, self.glyphBriteDict = {}, {}, {}
    self.loadYaml(yamlFn)

  ############# report error #############

  def reportError(self, functionName, issue):
    try:
      errorMsg = "enoPlaces %s error: %s" % (functionName, issue)
      print(errorMsg)
    except: print("enoPlaces reportError error:"); traceback.print_exc(); return None

  ############# get field #############

  def getField(self, function, dictionary, key):

    if key not in dictionary:
      self.reportError(function, "getField error: key %s not in dictionary %s!" % (key, dictionary))
      return None

    result = dictionary[key]
    return result

  ############# load yaml #############

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
      y = self.yamlD  #yaml data shortcut
      if y is None:   self.reportError("processLoci", "yaml data not yet loaded"); return None

      pts   = self.getField('processLoci', y, 'placeTypes'); if pts   is None: return
      pt    = self.getField('processLoci', pts, ptypeName);  if pt    is None: return
      imgFn = self.getField('processLoci', pt,  'glyph100'); if imgFn is None: return

      self.glyphNormDict[ptypeName] = imgFn

      for locus in locii:
        screenPos = self.processLocus(ptypeName, locii)
        a = Actor(imgFn, pos = screenPos)
        self.addActor(a, ptypeName)

  ############# add actor #############

  def addActor(self, actorHandle, ptypeName):
    if self.actorDict == None: self.actorDict = {}

    if ptypeName not in self.actorDict: self.actorDict[ptypeName] = []
    self.actorDict[ptypeName].append(actorHandle) # one more argument probably important, but -- coming

  ############# pgzero draw #############

  def draw(self):
    if self.actorDict == None: self.reportError("draw", "No actors found in actorDict!"); return None
    for ptypeName in self.actorDict:
      ptActorList = self.actorDict[ptypeName]
      for a in ptActorList: a.draw()

### end ###

