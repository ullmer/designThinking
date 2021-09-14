#Clemson Design Thinking, 2021-08-30 (Brygg Ullmer)
import csv, sys, traceback

try:    yamlF         = open(sys.argv[0], 'r')
except: print("problem opening command-line YAML metainfo; aborting"); sys.exit(-1)
yd = yaml.safeload(yamlF)
 
covidF        = open(yd['sourceDataCsv'], 'r+t')
dataReader    = csv.reader(covidF, delimiter=','); 

def getFieldsFloat(d, fields): # extract specified float fields from list d
  result = []
  for field in fields: result.append(float(d[field]))
  return result

def perc(f): return str(int(100*f))

for d in dataReader:
  try:
    city, state, date                        = d[6], d[2], d[1]
    tac, tb, taa, icuBeds, icuUsed, icuCovid = getFieldsFloat(d, [35, 31, 34, 21, 24, 25])
    covidBeds = perc(tac/tb); ocuBeds=perc(taa/tb); percIcu = perc(icuUsed/icuBeds); pIC = perc(icuCovid/icuBeds)
    if float(covidBeds) >= 20: print(','.join([state, city, date, covidBeds, ocuBeds, pIC, percIcu]))
  except: pass #traceback.print_exc()

### end ###
