# Enodia Interaction Panel Description
# Brygg Ullmer, Clemson University
# Begun 2023-09-26

#cuColleges01.yaml

import yaml, traceback

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

  ############# report error #############

  def reportError(self, functionName, issue):
    try: 
      errorMsg = "enoIPanelDescr %s error: %s" % (functionName, issue)
      print(errorMsg)
    except: print("enoIPanelDescr reportError error:"); traceback.print_exc(); return None

  ################ Enodia Interaction Panel Description ####################

  def getField(self, fieldName):
     if self.yamlD == None:          
       self.reportError("getField", "yamlD is None"); return None

     if 'imageMatrix' not in self.yamlD:
       self.reportError("getField", "imageMatrix not in yamlD"); return None

     im = self.yamlD['imageMatrix']

     if fieldName not in im:
       self.reportError("getField", "fieldName not in yamlD"); return None

     result = im[fieldName]
     return result

  ################ get matrix expansion ####################

  def getMatrixExpansion(self):
     return self.matrixExpansion

  ################ loadYaml ####################

  def loadYaml(self, yamlFn):
    self.yamlFn = yamlFn
    yamlF       = open(yamlFn, 'rt')
    self.yamlD  = yaml.safe_load(yamlF)
    self.parseMatrix()

  ################ parse matrix ####################

  def parseMatrix(self):
   if self.yamlD is None: 
     self.reportError("parseMatrix", "yamlD is None"); return None

   m  = self.getField('matrix')  
   mm = self.getField('matrixMap')  
   if m is None: 
     self.reportError("parseMatrix", "matrix is None"); return None

   if mm is None: 
     self.reportError("parseMatrix", "matrixMap is None"); return None

   # matrixMap:
   #   A: [CAAC,     Art, CDP, Arch, LA, HP, RUD, SoA]
   #   a: [CAH,      E, H, L, PA, PR]

   # matrix: |-
   #   FFFFeeee 
   #   FFF aaaaa

   self.matrixIdxCount  = {}
   self.matrixExpansion = [] #2D dictionary
   matrixLines = m.split("\n")

   for mline in matrixLines:
     mlLen = len(mline)
     row = []
     for i in range(mlLen):
       mlChar = mline[i]
       if mlChar not in self.matrixIdxCount:
         self.matrixIdxCount[mlChar] = 0

       if mlChar not in mm:
         if mlChar != ' ': self.reportError("parseMatrix", "mlChar not in matrixMap")
         mlCharExpansion = None
       else:
         miCount = self.matrixIdxCount[mlChar]
         mlCharExpansion = mm[mlChar][miCount]

       row.append(mlCharExpansion)
       self.matrixIdxCount[mlChar] += 1
     self.matrixExpansion.append(row)

####################################
############### main ###############

def main():
  eipd = enoIPanelDescr("cuColleges01.yaml")
  print(eipd.getMatrixExpansion())

if __name__ == "__main__":
   main()

### end ###
