# Make partial extraction of CSV-save of tribe_entity_mapping sheet from this source:
#  https://www.epa.gov/sites/production/files/2021-03/tribe_entity_mapping_2021-03-04.xlsx
#  into YAML.
# (Exploratory version to facilitate related conversations.)
# Brygg Ullmer, Clemson University
# Begun 2023-11-21

import csv, sys, traceback

################### csv2yaml support class ###################

class csv2yaml:

  csvFn  = None
  yamlFn = None

  targetColDictXC = { #target column dictionary, Excel column ID (alphabetic)
    'name':     'AE',
    'biaCode':  'AF',
    'epaId':    'AG',
    'states':   'AH'}

  targetColDictN  = {} #target column dictionary, Excel column ID (numeric)
  targetColFields = [] #keys of targetColDictXC/N
  targetColList   = [] #vals of targetColDictN

  maxLineNum = 10
  lineNum    = 0

  ################### constructor ###################

  def __init__(self, **kwargs): 

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.mapColId()
    self.loadCsv() #internally checks for csvFn to be populated
    self.genYaml() #internally checks for yamlFn to be populated 
  
  ################### map alphabetic to numeric ###################
  
  def mapAlpha2Num(self, alpha):
    try:
      lowAlpha = alpha.tolower()
      return ord(alpha) - ord('a') #A/a -> 0 .. Z/z-> 25
    except: 
      print('mapAlpha2Num issue:'); print(traceback.print_exc()); sys.exit(-1)
  
  ################### map alphabetic to numeric ###################
  
  def mapColAlpha2Num(self, colAlpha): #map column alphabetic ID (A..Z, AA..AZ, etc.) to numeric
                                 #initially, hardcode to 1 or 2 alphabetic codes 
    numCA  = len(colAlpha)
    if numCA == 1: return mapAlpha2Num(alpha)
    if numCA > 2:  print('mapColAlpha2Num requires generalization; sorry!'); sys.exit(-1)
    if numCA == 0: print('mapColAlpha2Num requires 1 or 2 alphabetic characters; sorry!'); sys.exit(-1)
  
    result = 26 * mapAlpha2Num(colAlpha[0]) + mapAlpha2Num(colAlpha[1]) # hardwired to two 
    return result
  
  ################### map column IDs ###################
  
  def mapColId(self):

   for key in self.targetColDictXC:
     alphaVal = self.targetColDictXC[key]
     numVal   = self.mapColAlpha2Num(alphaVal)
     self.targetColDictN[key] = numVal
     self.targetColFields.append(key) 
     self.targetColVals.append(val) 
  
  ################### loadCsv ###################
  
  def loadCsv(self): 
    if self.csvFn  is None: print("csv2yaml: loadCsv requires csvFn");  sys.exit(-1)

    csvF  = open(csvFn, 'rt')
    csvR  = csv.reader(csvF, delimter=',', quotechar='"')
    for row in csvR:
      if self.lineNum >= self.maxLineNum: sys.exit(1)

      extractDict = {}
      for key in self.targetColDictN:
        colVal  = self.targetColDictN[key]
        dataVal = row[colVal]
        extractDict[key] = dataVal

      print("%i: %s" % (self.lineNum, str(extractDict)))
      self.lineNum += 1
    
  ################### loadCsv ###################
  
  def genYaml(self): #internally checks for yamlFn to be populated 
    if self.yamlFn is None: print("csv2yaml: genYaml requires yamlFn"); sys.exit(-1)

################### main ###################

ourCsvFn   = 'tribe_entity_mapping_2021-03-04.csv'
ourYamlFn  = 'tribe_entity_mapping_2021-03-04.yaml'

c2y = csv2yaml(csvFn=ourCsvFn, yamlFn=ourYamlFn)
  
### end ###
