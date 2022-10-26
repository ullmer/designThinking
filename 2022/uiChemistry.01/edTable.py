# Brygg Ullmer and Miriam Konkel
# Support class for engaging periodic table of the elements
# Clemson University
# Begun 2022-10-26

import yaml

#ed prefix = Enodia Data 
  
######################################################################### 
#################### Enodia Data : Periodic Table #################### 

class edPerTable:
  yamlFn        = 'pubchemNcbiNlmNihElements.yaml'
  yamlD, yamlD2 = None, None
  yamlHash      = None
  yamlKeys      = None
  yamlKeyfield  = 'periodictTable'

  dimensions, spdFPadding, tlBrPadding = [None]*3

  verbose = False

  #################### constructor ####################

  def getKeys(self): return self.yamlKeys

  def getVal(self, key):
    if key in self.yamlHash: return self.yamlHash[key]
    print("edPerTable getVal error: key %s not defined!" % key); return None

  #################### load data ####################

  def loadData(self):
    yamlF         = open(yamlFn, 'rt')
    self.yamlD    = yaml.safe_load(yamlF)
    self.yamlKeys = []; self.yamlHash = {}

    if self.yamlKeyfield not in self.yamlD: #partly to ascertain whether this is likely appropriate data
      print('edPerTable error: yaml keyfield not present in', self.yamlFn); return
 
    self.yamlD2 = self.yMLD[self.yamlKeyfield] #simplify future references
    
    for field in self.yamlD2:
      value = self.yamlD2[field]
      self.yamlHash[key] = value
      self.yamlKeys.append(key)

#dimensions rows spdFPadding tlBrPadding imgPath tables
  
  #################### constructor ####################

  def __init__(self):
    self.loadData()


############################################## 
#################### main #################### 

def main():
  ed = edPerTable()
  print("keys:", ed.getKeys())
  print("hash:", ed.yamlHash)

if __name__ == "__main__":
  main()

### end ###

