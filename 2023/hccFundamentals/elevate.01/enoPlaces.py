# Enodia Launch functions
# Brygg Ullmer, Clemson University
# Begun 2023-08-30

import yaml, traceback

from pgzero.builtins import Actor, animate, keyboard
#https://stackoverflow.com/questions/55438239/name-actor-is-not-defined

##################### pygamezero button #####################

class enoPlaces:
  fontSize       = 36
  yamlFn         = None #YAML filename; e.g., elevatePlaces01.yaml
  yamlD          = None #YAML data import
  dx, dy         = 0, -315
  xscale, yscale = 1, 1.3
  screenWidth, screenHeight = 1200, 940

  glyphNormDict  = None
  glyphDimDict   = None
  glyphBriteDict = None
  bboxDimDict    = None # for bounding boxes specific to different place types, per SVG oddity
  bboxShiftDict  = None # for bounding boxes specific to different place types, per SVG oddity
  actorDict      = None

  workspace     = None
  placeTypeList = None
  verbose       = False

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.glyphNormDict, self.glyphDimDict, self.glyphBriteDict = {}, {}, {}
    self.bboxDimDict,   self.bboxShiftDict                     = {}, {}
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
      errorStr = "function %s: getField error: key %s not in dictionary %s!" % (function, key, dictionary)
      raise Exception(errorStr)

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

        if 'bboxDimension' in ptype:
          bbox = ptype['bboxDimension']
          self.bboxDimDict[ptypeName] = bbox

        if 'bboxShift' in ptype:
          bboxShift = ptype['bboxShift']
          self.bboxShiftDict[ptypeName] = bbox

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
      sw, sh, dx, dy = self.screenWidth, self.screenHeight, self.dx, self.dy
      xscale, yscale = self.xscale, self.yscale
      x, y = locus

      bbw, bbh, bbdx, bbdy = None, None, None, None

      if ptypeName in self.bboxDimDict: 
        bbw, bbh = self.bboxDimDict[ptypeName] # bounding boxes specific to specific place types

      if ptypeName in self.bboxShiftDict: 
        bbdx, bbdy = self.bboxShiftDict[ptypeName] # bounding boxes specific to specific place types
        dx, dy = bbdx, bbdy #override default

      if bbw is not None: w, h = bbw, bbh
      else:               w, h = ww,  wh

      sx = int(float(x) / float(w) * sw * xscale) + dx
      sy = int(float(y) / float(h) * sh * yscale) + dy

      if self.verbose: print("processLocus %i %i" % (sx, sy))
      return [sx, sy]

    except: self.reportError("processLocus", "exception caught"); traceback.print_exc(); return None

  ############# process loci (multiple) #############

  def processLoci(self, ptypeName, locii):

    try:
      y = self.yamlD  #yaml data shortcut
      if y is None:   self.reportError("processLoci", "yaml data not yet loaded"); return None

      try: 
        pts   = self.getField('processLoci', y, 'placeTypes')
        pt    = self.getField('processLoci', pts, ptypeName)  
        imgFn = self.getField('processLoci', pt,  'glyph100')
      except: self.reportError("processLoci", "exception caught"); traceback.print_exc(); return None

      self.glyphNormDict[ptypeName] = imgFn

      for locus in locii:
        screenPos = self.processLocus(ptypeName, locus)
        a = Actor(imgFn, pos = screenPos)
        self.addActor(a, ptypeName)

    except: self.reportError("processLoci", "exception caught"); traceback.print_exc(); return None

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

