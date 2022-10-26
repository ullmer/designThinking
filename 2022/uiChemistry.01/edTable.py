# Brygg Ullmer and Miriam Konkel
# Support class for engaging periodic table of the elements
# Clemson University
# Begun 2022-10-26

import yaml
from PIL import Image

#ed prefix = Enodia Data 
  
######################################################################### 
#################### Enodia Data : Periodic Table #################### 

class edPerTable:
  yamlFn        = 'pubchemNcbiNlmNihElements.yaml'
  yamlD, yamlD2 = None, None
  yamlHash      = None
  yamlKeys      = None
  yamlKeyfield  = 'periodicTable'
  coord2element = None
  element2coord = None
  tableName2Img = None

  dimensions, spdFPadding, tlBrPadding = [None]*3

  verbose = False

  #################### constructor ####################

  def getKeys(self): return self.yamlKeys

  def getVal(self, key):
    if key in self.yamlHash: return self.yamlHash[key]
    print("edPerTable getVal error: key %s not defined!" % key); return None

  def getTableNames(self): 
    tables = self.getVal('tables')
    tlist = list(tables.keys())
    return tlist

  def getTableImage(self, tableName): 
    if tableName in self.tableName2Img:
      return self.tableName2Img[tableName] 

    tables = self.getVal('tables')
    table = tables[tableName]
    imgFn = table[1]
    imgFnPath = self.getVal('imgPath')
    fn = '%s/%s' % (imgFnPath, imgFn)

    img = Image.open(fn)
    self.tableName2Img[tableName] = img
    return img

  def getTableImgSize(self, tableName): 
    img = self.getTableImage(tableName)
    return img.size

  #################### load data ####################

  def loadData(self):
    yamlF         = open(self.yamlFn, 'rt')
    self.yamlD    = yaml.safe_load(yamlF)
    self.yamlKeys = []; self.yamlHash = {}
    self.tableName2Img = {}

    #print(self.yamlD)

    if self.yamlKeyfield not in self.yamlD: #partly to ascertain whether this is likely appropriate data
      print('edPerTable error: yaml keyfield not present in', self.yamlFn); return
 
    self.yamlD2 = self.yamlD[self.yamlKeyfield] #simplify future references
    
    for key in self.yamlD2:
      value = self.yamlD2[key]
      self.yamlHash[key] = value
      self.yamlKeys.append(key)

    self.dimensions  = self.getVal('dimensions')
    self.spdFPadding = self.getVal('spdFPadding')
    self.tlBrPadding = self.getVal('tlBrPadding')

    self.coord2element = {} #because sparse, will handle as hash instead of list or matrix
    self.element2coord = {}
 
    rows = self.getVal('rows')
    #print("rows:", rows)

    for row in rows:
      self.digestRowProperties(row)
  
  #################### digest row properties ####################

  def digestRowProperties(self, row):
    #print("procRow:", row)
    startRow, startColumn, elements = row
    x = startRow; y = startColumn

    for element in elements:
      if x not in self.coord2element: self.coord2element[x] = {}
      self.coord2element[x][y] = element
      self.element2coord[element] = (x,y)
      x += 1

#dimensions rows spdFPadding tlBrPadding imgPath tables
  
  #################### constructor ####################

  def __init__(self):
    self.loadData()

############################################## 
#################### main #################### 

def main():
  ed = edPerTable()
  #print("keys:", ed.getKeys())
  #print("hash:", ed.yamlHash)
  tableNames = ed.getTableNames()

  for tn in tableNames:
    size = ed.getTableImgSize(tn)
    print("%s : %s" % (tn, size))

if __name__ == "__main__":
  main()

### end ###

