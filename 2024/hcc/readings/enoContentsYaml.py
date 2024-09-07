# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import yaml, traceback

################## Content class ##################

class ContentYaml: 

  #fields     = ['author', 'year', 'abbrevTitle', 'title', 'presenter', 'presentedDate']
  fields     = None
  fieldsDict = None

  ################## constructor, error ##################

  def __init__(self): self.fieldsDict = {}
  def err(self, msg): print("Content error:", msg); traceback.print_exc()

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

  def printContentAbbrev(self):    
    try:    print(self.fieldsDict['abbrevTitle'])
    except: self.err('printContentAbbrev')

  def print(self): print(self.fieldsDict)   

################## Contents class ##################

class ContentsYaml: #not catching any errors; caveat emptor
  fn          = 'index.yaml'  #filename
  yd          = None          #YAML data
  yc          = None          #YAML extraction for classes
  readingList = None

  ################## constructor, err ##################

  def __init__(self): self.readingList = []; self.loadYaml()

  def err(self, msg): print("Contents error:", msg); traceback.print_exc()

  def size(self): 
    if self.readingList is not None: return len(self.readingList)

  ################## load YAML from file ##################

  def loadYaml(self): 
    try:
      f       = open(self.fn, 'rt')
      self.yd = yaml.safe_load(f)
      self.yc = self.yd['class'] 

      for classDate in self.yc:
        classPeriod = self.yc[classDate]
        for reading in classPeriod:
          reading['presentedDate'] = classDate

          r = Content()
          r.setFieldsFromYaml(reading)
          self.readingList.append(r)
    except: self.err("loadYaml")

  ################## print reading abbreviations ##################

  def printContentAbbrevs(self): 
    try:
      for r in self.readingList: r.printContentAbbrev()
    except: self.err("printContentAbbrevs")

  ################## get reading index ##################

  def getContent(self, i): 
    try:
      if i < 0 or i > len(self.readingList): self.err("getContent index out of bounds: " + i); return
      return self.readingList[i]
      
    except: self.err("getContent: " + i); return

################## main ##################

if __name__ == "__main__":
  readings = Contents()
  readings.loadYaml()
  readings.printContentAbbrevs()

### end ###
