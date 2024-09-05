# Example parsing class reading li
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import yaml

################## Reading class ##################

class Reading: #not catching any errors; caveat emptor

  fields     = ['author', 'year', 'abbrevTitle', 'title', 'presenter']
  fieldsDict = None

  def setFieldsFromYaml(self, yd):
    for field in self.fields: self.fieldsDict[field] = yd[field]

  def __init__(self):              self.fieldsDict = {}
  def setField(self, field, val):  self.fieldsDict[field] = val
  def getField(self, field):       return self.fieldsDict[field]
  def printReadingAbbrev(self):    print(self.fieldsDict['abbrevTitle'])

################## Readings class ##################

class Readings: #not catching any errors; caveat emptor
  fn          = 'index.yaml'  #filename
  yd          = None          #YAML data
  yc          = None          #YAML extraction for classes
  readingList = None

  ################## constructor ##################

  def __init__(self): self.readingList = []

  ################## load YAML from file ##################

  def loadYaml(self): 
    f       = open(self.fn, 'rt')
    self.yd = yaml.safe_load(f)
    self.yc = self.yd['class'] 

    for classDate in self.yc:
      classPeriod = self.yc[classDate]
      for reading in classPeriod:
        r = Reading()
        r.setFieldsFromYaml(reading)
        self.readingList.append(r)

  ################## print reading abbreviations ##################

  def printReadingAbbrevs(self): 
    for r in self.readingList: r.printReadingAbbrev()

################## main ##################

if __name__ == "__main__":
  readings = Readings()
  readings.loadYaml()
  readings.printReadingAbbrevs()

### end ###
