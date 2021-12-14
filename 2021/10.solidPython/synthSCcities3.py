# Join latlong coordinates and pop1ulation of SC cities
# Brygg Ullmer, Clemson University
# Begun 2021-10-28

import csv, traceback

coordsFn = "sc_cities.csv";   coordsF = open(coordsFn, "r")
pop1Fn   = "sc-urban-pop.csv"; pop1F = open(pop1Fn, "r")
pop2Fn   = "sc-cities.csv";     pop2F = open(pop2Fn, "r")

coordReader = csv.reader(coordsF, delimiter=",")
pop1Reader  = csv.reader(pop1F,   delimiter=",")
pop2Reader  = csv.reader(pop2F,   delimiter=",")

coordHash = {}; pop1Hash = {}; pop2Hash = {}

for row in coordReader:
  city = row[3]; lat, long = row[5:7]
  coordHash[city] = [lat, long]
  #if rowNum<5: print(city, lat, long); rowNum += 1

rowNum = 0
for row in pop1Reader:
  city = row[1]; pop1 = row[2]
  pop1Hash[city] = pop1
  #if rowNum<5: print(city, pop1); rowNum += 1

rowNum = 0
for row in pop2Reader:
  try:
    #city = row[0]; pop2 = row[4]; pop2b = pop2.replace(",", "")
    city = row[0]; pop2 = row[5]; pop2b = pop2.replace(",", "")
    pop2Hash[city] = pop2b
    #if rowNum<5: print(city, pop2b); rowNum += 1
  except: pass #just ignore for present

cities = coordHash.keys() # more city-coords than city-urban areas

for city in cities:
  coord = coordHash[city]; lat, long = coord
  try:   pop   = pop1Hash[city]
  except:  
    try: pop = pop2Hash[city]
    except: pop = "-"

  outStr = ",".join([city, pop, lat, long])
  print(outStr)

### end ###
