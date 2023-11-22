# Make partial extraction of CSV-save of tribe_entity_mapping sheet from this source:
#  https://www.epa.gov/sites/production/files/2021-03/tribe_entity_mapping_2021-03-04.xlsx
#  into YAML.
# (Exploratory version to facilitate related conversations.)
# Brygg Ullmer, Clemson University
# Begun 2023-11-21

import csv, sys

csvFn = 'tribe_entity_mapping_2021-03-04.csv'

targetColDictXC = { #target column dictionary, Excel column ID (alphabetic)
  'name':     'AE',
  'biaCode':  'AF',
  'epaId':    'AG',
  'states':   'AH'}

targetColDictN  = {} #target column dictionary, Excel column ID (numeric)
targetColFields = [] #keys of targetColDictXC/N
targetColList   = [] #vals of targetColDictN

def mapAlpha2Num(alpha):       return ord(alpha) - ord('A') #A -> 0 .. Z-> 25
def mapColAlpha2Num(colAlpha): #map column alphabetic ID (A..Z, AA..AZ, etc.) to numeric 

csvF  = open(csvFn, 'rt')
csvR  = csv.reader(csvF, delimter=',', quotechar='"')

maxLineNum = 10
lineNum    = 0

for row in csvR:
  print("TBD")
  lineNum += 1
  if lineNum >= maxLineNum: sys.exit(1)

### end ###
