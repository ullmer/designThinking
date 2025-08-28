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

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.fieldsDict = {}

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

  def printContentField(self, targetField):    
    try:    print(self.fieldsDict[targetField])
    except: self.err('printContentField')

  def print(self): print(self.fieldsDict)   

################## Contents class ##################

class ContentsYaml: #not catching any errors; caveat emptor
  fn          = 'index.yaml'  #filename
  yd          = None          #YAML data
  yc          = None          #YAML extraction for classes
  contentList = None

  ################## constructor, err ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.contentList = []
    self.loadYaml()

  def err(self, msg): print("Contents error:", msg); traceback.print_exc()

  def size(self): 
    if self.contentList is not None: return len(self.contentList)

  ################## load YAML from file ##################

  def loadYaml(self): 
    try:
      f       = open(self.fn, 'rt')
      self.yd = yaml.safe_load(f)
    except: self.err("loadYaml")

  ################## print reading abbreviations ##################

  def printContentFields(self, field): 
    try:
      for r in self.contentList: r.printContentFields(field)
    except: self.err("printContentFields")

  ################## get reading index ##################

  def getContent(self, i): 
    try:
      if i < 0 or i > len(self.contentList): self.err("getContent index out of bounds: " + i); return
      return self.contentList[i]
      
    except: self.err("getContent: " + i); return

################## main ##################

if __name__ == "__main__":
  readings = Contents()
  readings.loadYaml()
  readings.printContentAbbrevs()

### end ###
