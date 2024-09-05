# Example parsing class reading li
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import yaml, traceback

################## Reading class ##################

class Reading: #not catching any errors; caveat emptor

  fields     = ['author', 'year', 'abbrevTitle', 'title', 'presenter']
  fieldsDict = None

  def setFieldsFromYaml(self, yd):
    try: 
      for field in self.fields: self.fieldsDict[field] = yd[field]
    except: self.err('setFieldsFromYaml')
    
  def err(self, msg):              print("Reading error:", msg); traceback.print_exc()
  def __init__(self):              self.fieldsDict = {}

  def setField(self, field, val):  
    try:    self.fieldsDict[field] = val
    except: self.err('setField' + field + val)

  def getField(self, field):       
    try:    return self.fieldsDict[field]
    except: self.err('getField' + field)

  def printReadingAbbrev(self):    
    try:    print(self.fieldsDict['abbrevTitle'])
    except: self.err('printReadingAbbrev')

################## Readings class ##################

class Readings: #not catching any errors; caveat emptor
  fn          = 'index.yaml'  #filename
  yd          = None          #YAML data
  yc          = None          #YAML extraction for classes
  readingList = None

  ################## constructor ##################

  def __init__(self): self.readingList = []
  def err(self, msg): print("Readings error:", msg); traceback.print_exc()

  ################## load YAML from file ##################

  def loadYaml(self): 
    try:
      f       = open(self.fn, 'rt')
      self.yd = yaml.safe_load(f)
      self.yc = self.yd['class'] 

      for classDate in self.yc:
        classPeriod = self.yc[classDate]
        for reading in classPeriod:
          r = Reading()
          r.setFieldsFromYaml(reading)
          self.readingList.append(r)
    except: self.err("loadYaml")

  ################## print reading abbreviations ##################

  def printReadingAbbrevs(self): 
    try:
      for r in self.readingList: r.printReadingAbbrev()
    except: self.err("printReadingAbbrevs")

################## main ##################

if __name__ == "__main__":
  readings = Readings()
  readings.loadYaml()
  readings.printReadingAbbrevs()

### end ###
