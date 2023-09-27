# Enodia Interaction Panel Description
# Brygg Ullmer, Clemson University
# Begun 2023-09-26

#cuColleges01.yaml

import yaml

############################################################################## 
#################### Enodia Interaction Panel Description ####################

class enoIPanelDescr:
  yamlFn = None #yaml filename
  yamlD  = None #yaml data structure (imported)

  matrixIdxCount  = None
  matrixExpansion = None

  ############# constructor #############

  def __init__(self, yamlFn, **kwargs):
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.loadYaml(yamlFn)

  ################ Enodia Interaction Panel Description ####################

  def getField(self, fieldName):
     if self.yamlD == None:          return None
     if fieldName not in self.yamlD: return None
     result = self.yamlD[fieldName]
     return result

  ################ loadYaml ####################

  def loadYaml(self, yamlFn):
    self.yamlFn = yamlFn
    yamlF       = open(yamlFn, 'rt')
    self.yamlD  = yaml.safe_load(yamlF)
    self.parseMatrix()

  ################ parse matrix ####################

  def parseMatrix(self):
   is self.yamlD is None: return None

   m  = self.getField('matrix')  
   mm = self.getField('matrixMap')  
   if m is None or mm is None: return None #warning messages should come

   # matrixMap:
   #   A: [CAAC,     Art, CDP, Arch, LA, HP, RUD, SoA]
   #   a: [CAH,      E, H, L, PA, PR]

   # matrix: |-
   #   FFFFeeee 
   #   FFF aaaaa

   self.matrixIdxCount  = {}
   self.matrixExpansion = {} #2D dictionary
   matrixLines = matrix.split("\n")

   row = 0 

   for mline in matrixLines:
     mlLen = len(mline)
     self.matrixExpansion[row] = {}
     for col in range(mlLen):
       mlChar = mline[col]
       if mlChar not in self.matrixIdxCount:
         self.matrixIdxCount[mlChar] = 0

       if mlChar not in self.matrixMap: mlCharExpansion = None
       else:
         miCount = self.matrixIdxCount[mlChar]
         mlCharExpansion = self.matrixMap[mlChar][miCount]

       self.matrixExpansion[row][col] = mlCharExpansion 
       self.matrixIdxCount[mlChar] += 1

####################################
############### main ###############

def main():
  eipd = enoIPanelDescr("cuColleges01.yaml")

if __name__ == "__main__":
   main()

### end ###
