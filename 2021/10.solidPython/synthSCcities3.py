# Join latlong coordinates and pop1ulation of SC cities
# Brygg Ullmer, Clemson University
# Begun 2021-10-28

import csv, traceback

coordsFn = "sc_cities.csv";   coordsF = open(coordsFn, "r")
pop1Fn   = "sc-urban-pop1.csv"; pop1F = open(pop1Fn, "r")
pop2Fn   = "sc-cities.csv";     pop2F = open(pop2Fn, "r")

coordReader = csv.reader(coordsF, delimiter=",")
pop1Reader  = csv.reader(pop1F,   delimiter=",")
pop2Reader  = csv.reader(pop2F,   delimiter=",")

coordHash = {}; pop1Hash = {}

for row in coordReader:
  city = row[3]; lat, long = row[5:7]
  coordHash[city] = [lat, long]
  #if rowNum<5: print(city, lat, long); rowNum += 1

print("="*10)

rowNum = 0
for row in pop1Reader:
  city = row[1]; pop1 = row[2]
  pop1Hash[city] = pop1
  #if rowNum<5: print(city, pop1); rowNum += 1

cities = coordHash.keys() # more city-coords than city-urban areas

for city in cities:
  coord = coordHash[city]; lat, long = coord
  try:     pop1   = pop1Hash[city]
  except:  pop1   = "-"   # we only have urban-area pop1ulation estimations for subset of cities
  outStr = ",".join([city, pop1, lat, long])
  print(outStr)

### end ###
