# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import yaml, traceback

################## Reading class ##################

class Reading: #not catching any errors; caveat emptor

  fields          = ['author', 'year', 'abbrevTitle', 'title', 'presenter', 'presentedDate']
  readingGroupNum = None
  fieldsDict      = None

  ################## constructor, error ##################

  def __init__(self): self.fieldsDict = {}
  def err(self, msg): print("Reading error:", msg); traceback.print_exc()

  ################## set fields from yaml ##################

  def setFieldsFromYaml(self, yd):
    try: 
      for field in self.fields: self.fieldsDict[field] = yd[field]
    except: self.err('setFieldsFromYaml')
    
  ################## set field ##################

  def setField(self, field, val):  
    try:    self.fieldsDict[field] = val
    except: self.err('setField' + field + val)

  ################## get field ##################

  def getField(self, field):       
    try:    return self.fieldsDict[field]
    except: self.err('getField' + field)

  ################## get field ##################

  def getFields(self, fields):       
    result = []

    try:    
      for field in fields: result.append(self.fieldsDict[field])
    except: self.err('getField' + field)

    return result

  ################## print ##################

  def printReadingAbbrev(self):    
    try:    print(self.fieldsDict['abbrevTitle'])
    except: self.err('printReadingAbbrev')

  def print(self): print(self.fieldsDict)   

################## Readings class ##################

class Readings: #not catching any errors; caveat emptor
  fn          = 'index.yaml'  #filename
  yd          = None          #YAML data
  yc          = None          #YAML extraction for classes
  readingList = None
  numReadingGroups = 0

  ################## constructor, err ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.readingList = []; self.loadYaml()

  def err(self, msg): print("Readings error:", msg); traceback.print_exc()

  def size(self): 
    if self.readingList is not None: return len(self.readingList)

  ################## load YAML from file ##################

  def loadYaml(self): 
    try:
      f       = open(self.fn, 'rt')
      self.yd = yaml.safe_load(f)
      self.yc = self.yd['class'] 
      idx     = 0

      for classDate in self.yc:
        classPeriod = self.yc[classDate]
        self.numReadingGroups += 1 
        for reading in classPeriod:
          reading['presentedDate'] = classDate

          r = Reading()
          r.setFieldsFromYaml(reading)
          r.readingGroupNum = idx
          self.readingList.append(r)

        idx += 1 # by class period, not reading #

    except: self.err("loadYaml")

  ################## print reading abbreviations ##################

  def printReadingAbbrevs(self): 
    try:
      for r in self.readingList: r.printReadingAbbrev()
    except: self.err("printReadingAbbrevs")

  ################## get reading index ##################

  def getReading(self, i): 
    try:
      if i < 0 or i > len(self.readingList): self.err("getReading index out of bounds: " + i); return
      return self.readingList[i]
      
    except: self.err("getReading: " + i); return

################## main ##################

if __name__ == "__main__":
  readings = Readings()
  readings.loadYaml()
  readings.printReadingAbbrevs()

### end ###
