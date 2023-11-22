# Make partial extraction of CSV-save of tribe_entity_mapping sheet from this source:
#  https://www.epa.gov/sites/production/files/2021-03/tribe_entity_mapping_2021-03-04.xlsx
#  into YAML (with some fields initially hardcoded to defaults, but coded to generalize)
# Exploratory version to facilitate related conversations.
# Brygg Ullmer, Clemson University
# Begun 2023-11-21

import csv, sys, traceback
from collections import Counter

################### csv2yaml support class ###################

class csv2yaml:

  csvFn  = None
  yamlFn = None

  targetColDictXC = { #target column dictionary, Excel column ID (alphabetic)
    'name':     'AE',
    'biaCode':  'AF',
    'epaId':    'AG',
    'states':   'AH'}

  quoteFields   = ['name']
  listifyFields = ['states']       #change these fields into lists
  listifySubstitutes = {';' : ','} #... making these character substitutions

  fieldOrder  = ['biaCode', 'epaId', 'states', 'name']

  targetColDictN     = {} #target column dictionary, Excel column ID (numeric)
  maxObservedLenDict = {}
  targetColFields    = [] #keys of targetColDictXC/N
  targetColVals      = [] #vals of targetColDictN
  rowData            = []
  ignoreRowErrors    = False
  verbose            = False

  groupByTargetListLen   = True #e.g., group by number of states
  groupByTargetListField = 'states' #e.g., group by number of states

  #maxLineNum = 10
  maxLineNum = None
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
      lowAlpha = alpha.lower()
      return ord(lowAlpha) - ord('a') #A/a -> 0 .. Z/z-> 25
    except: 
      print('mapAlpha2Num issue:'); print(traceback.print_exc()); sys.exit(-1)
  
  ################### map alphabetic to numeric ###################
  
  def mapColAlpha2Num(self, colAlpha): #map column alphabetic ID (A..Z, AA..AZ, etc.) to numeric
                                       #initially, hardcode to 1 or 2 alphabetic codes 
    numCA  = len(colAlpha)

    if numCA == 1: return self.mapAlpha2Num(alpha)
    if numCA > 2:  print('mapColAlpha2Num requires generalization; sorry!'); sys.exit(-1)
    if numCA == 0: print('mapColAlpha2Num presently requires 1 or 2 alphabetic characters; sorry!'); sys.exit(-1)
  
    result = 26 * (self.mapAlpha2Num(colAlpha[0])+1) + self.mapAlpha2Num(colAlpha[1]) # hardwired to two 
    return result
  
  ################### map column IDs ###################
  
  def mapColId(self):

   for key in self.targetColDictXC:
     alphaVal = self.targetColDictXC[key]
     numVal   = self.mapColAlpha2Num(alphaVal)
     self.targetColDictN[key] = numVal
     self.targetColFields.append(key) 
     self.targetColVals.append(numVal) 

  ################### loadCsv ###################
  
  def loadCsv(self): 
    if self.csvFn  is None: print("csv2yaml: loadCsv requires csvFn");  sys.exit(-1)

    csvF  = open(self.csvFn, 'rt')
    csvR  = csv.reader(csvF, delimiter=',', quotechar='"')
    for row in csvR:
      if self.maxLineNum is not None and self.lineNum >= self.maxLineNum: return 

      try:
        extractDict = {}
        numCols = len(row)
        for key in self.targetColDictN:
          colVal  = self.targetColDictN[key]
          if self.verbose: print(key, colVal); #print(row)

          if colVal < numCols: dataVal = row[colVal]
          else: print("loadCsv line %i issue: colVal %s not present; %s" % (self.lineNum, colVal, str(row))); continue

          extractDict[key] = dataVal

          valLen  = len(str(dataVal))
          if key not in self.maxObservedLenDict or valLen > self.maxObservedLenDict[key]: 
            self.maxObservedLenDict[key] = valLen
  
      except:
        if self.ignoreRowErrors: continue
        print("csv2yaml: loadCsv error:")
        print(traceback.print_exc()); #sys.exit(-1)

      if self.verbose: print("%i: %s" % (self.lineNum, str(extractDict)))
      self.rowData.append(extractDict)
      self.lineNum += 1

    print("loadCsv completed")

  ################### listify fields ###################
  
  def genListifyStr(self, fieldstr):
    result = "["

    for changeThis in self.listifySubstitutes:
      intoThis = self.listifySubstitutes[changeThis]
      fieldstr = fieldstr.replace(changeThis, intoThis)
  
    result += fieldstr
    result += "]"
    return result

  ################### count num char instances ###################
  #  https://realpython.com/python-counter/
  # ... but doing another way

  def countNumCharInstances(self, srcStr, targetChar):
    result = 0
    slen   = len(srcStr)

    for i in range(slen):
      if srcStr[i] == targetChar: result += 1
    return result
    
  ################### generate yaml ###################
  
  def genYaml(self): #internally checks for yamlFn to be populated 
    if self.yamlFn is None: print("csv2yaml: genYaml requires yamlFn"); sys.exit(-1)

    targetListLenDict = {}

    for rowDict in self.rowData:
      if self.verbose: print(rowDict)
      try:
        rowstr   = " - {"
        subels   = []

        for key in self.fieldOrder:
          fieldstr = key + ': '
          if   key in self.quoteFields:   fieldstr += '"%s"' % rowDict[key] #initially, ignore justification 
          elif key in self.listifyFields: fieldstr += self.genListifyStr(rowDict[key])
          else:                           fieldstr += rowDict[key]
          subels.append(fieldstr)

        if self.verbose: print(subels)

        rowstr += ', '.join(subels)
        rowstr += '}'
        if self.groupByTargetListLen is False: print(rowstr)
        else:   # group by target list length
          srcStr = rowDict[self.groupByTargetListField]
          tllen  = self.countNumCharInstances(srcStr, ';') + 1

          if tllen in targetListLenDict: targetListLenDict[tllen].append(rowstr)
          else:                          targetListLenDict[tllen] = [rowstr]

      except:
        if self.ignoreRowErrors: continue
        print("csv2yaml: genYaml error:")
        print(traceback.print_exc()); #sys.exit(-1)

      if self.groupByTargetListLen:
        targetListLengths = list(targetListLenDict.keys())
        targetListLengths.sort(reverse=True) #largest to smallest
        for listLength in targetListLengths:
          rows = targetListLenDict[listLength]
          for row in rows: print(rows)

################### main ###################

ourCsvFn   = 'tribe_entity_mapping_2021-03-04.csv'
ourYamlFn  = 'tribe_entity_mapping_2021-03-04.yaml'

c2y = csv2yaml(csvFn=ourCsvFn, yamlFn=ourYamlFn)
  
### end ###
