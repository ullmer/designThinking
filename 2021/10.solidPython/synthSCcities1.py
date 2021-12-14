# Join latlong coordinates and population of SC cities
# Brygg Ullmer, Clemson University
# Begun 2021-10-28

import csv

coordsFn = "sc_cities.csv"; coordsF = open(coordsFn, "r")
popFn = "sc-urban-pop.csv"; popF    = open(popFn, "r")

coordReader = csv.reader(coordsF, delimiter=",")
popReader   = csv.reader(popF,    delimiter=",")

coordHash = {}; popHash = {}

rowNum = 0
for row in coordReader:
  if rowNum<5: print(row)
  rowNum += 1

print("="*10)

rowNum = 0
for row in popReader:
  if rowNum<5: print(row)
  rowNum += 1

### end ###
