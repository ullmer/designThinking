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
  
  def mapColId(self)
  
  targetColDictXC = { #target column dictionary, Excel column ID (alphabetic)
    for keys 
    'name':     'AE',
  targetColDictN  = {} #target column dictionary, Excel column ID (numeric)
  targetColFields = [] #keys of targetColDictXC/N
  targetColList   = [] #vals of targetColDictN
  def mapColAlpha2Num(colAlpha): #map column alphabetic ID (A..Z, AA..AZ, etc.) to numeric
  
  ################### loadCsv ###################
  
    if self.csvFn  is None: print("csv2yaml constructor requires csvFn");  sys.exit(-1)
    if self.yamlFn is None: print("csv2yaml constructor requires yamlFn"); sys.exit(-1)
  csvF  = open(csvFn, 'rt')
  csvR  = csv.reader(csvF, delimter=',', quotechar='"')
  
  maxLineNum = 10
  lineNum    = 0
  
  for row in csvR:
    print("TBD")
    lineNum += 1
    if lineNum >= maxLineNum: sys.exit(1)

################### main ###################

csvFn = 'tribe_entity_mapping_2021-03-04.csv'
yFn   = 'tribe_entity_mapping_2021-03-04.csv'

c2y = csv2yaml()
  
### end ###
