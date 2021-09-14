#Clemson Design Thinking, 2021-08-30 (Brygg Ullmer)
import yaml, csv, sys, traceback, dt

try:    yamlF         = open(sys.argv[0], 'r')
except: print("problem opening command-line YAML metainfo; aborting"); sys.exit(-1)
yd = yaml.safeload(yamlF) #yd = YAML data
 
covidF        = open(yd['sourceDataCsv'], 'r+t')
dataReader    = csv.reader(covidF, delimiter=','); 

################## main ##################

for cd in dataReader: #cd = CSV Data
  try:
    city, state, date = dt.getFieldsText(cd, yd, ['city', 'state', 'date'])
    tac, tb, taa, icuBeds, icuUsed, icuCovid =
      dt.getFieldsFloat(cd, yd, ['tac', 'tb', 'taa', 'icuBeds', 'icuUsed', 'icuCovid'])
    covidBeds = perc(tac/tb); ocuBeds=perc(taa/tb); percIcu = perc(icuUsed/icuBeds); pIC = perc(icuCovid/icuBeds)
    if float(covidBeds) >= 20: printCSVLine print(','.join([state, city, date, covidBeds, ocuBeds, pIC, percIcu]))
  except: pass #traceback.print_exc()

### end ###
