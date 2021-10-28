# Join latlong coordinates and population of SC cities
# Brygg Ullmer, Clemson University
# Begun 2021-10-28

import csv, traceback

coordsFn = "sc_cities.csv"; coordsF = open(coordsFn, "r")
popFn = "sc-urban-pop.csv"; popF    = open(popFn, "r")

coordReader = csv.reader(coordsF, delimiter=",")
popReader   = csv.reader(popF,    delimiter=",")

coordHash = {}; popHash = {}

for row in coordReader:
  city = row[3]; lat, long = row[5:7]
  coordHash[city] = [lat, long]
  #if rowNum<5: print(city, lat, long); rowNum += 1

print("="*10)

rowNum = 0
for row in popReader:
  city = row[1]; pop = row[2]
  popHash[city] = pop
  #if rowNum<5: print(city, pop); rowNum += 1

cities = coordHash.keys() # more city-coords than city-urban areas

### end ###
