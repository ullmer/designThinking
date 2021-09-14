#Clemson Design Thinking, 2021-08-30 (Brygg Ullmer)
import yaml, csv, sys, traceback, dtHelper

################## extract data fields ##################
# extract specified fields from list cd (short for csvData), using 
# fields with fieldnames specified in yd (yamlData)

def getFieldsText(cd, yd, fields): 
  result = []
  for field in fields: 
    if field in yd:
      idx   = yd[field]
      value = cd[idx]
      result.append(value)
  return result

def getFieldsFloat(cd, yd, fields): # extract specified float fields from list cd
  tresult = getFieldsText(cd, yd, fields)
  for field in fields: result.append(float(d[field]))
  return result

################## extract percentages ##################

def perc(f): return str(int(100*f))

################## extract percentages ##################

def printCSV(fields): 
  if isinstance(fields, list):
    csvList = ','.join(fields) # join together fields, separated by commas
    print(csvList)
  else:
    print("dt.printCSV: argument passed is not list")

### end ###
