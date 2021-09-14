#Clemson Design Thinking, 2021-08-30 (Brygg Ullmer)
import yaml, csv, sys, traceback, dtHelper

################## extract data fields ##################

def getFieldsText(d, fields): # extract specified float fields from list d
  result = []
  for field in fields: result.append(d[field])
  return result

def getFieldsFloat(cd, yd, fields): # extract specified float fields from list d
  tresult = getFieldsText(cd, yd, fields)
  for field in fields: result.append(float(d[field]))
  return result

################## extract percentages ##################

def perc(f): return str(int(100*f))

### end ###
