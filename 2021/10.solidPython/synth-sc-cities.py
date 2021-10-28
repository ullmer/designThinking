# Join latlong coordinates and population of SC cities
# Brygg Ullmer, Clemson University
# Begun 2021-10-28

import csv

coordsFn = "sc_cities.csv"; coordsF = open(coordsFn, "r")
popFn = "sc-urban-pop.txt"; popF    = open(popFn, "r")

coordReader = csv.reader(coordsF, delimiter=',');
popReader   = csv.reader(popF,    delimiter=',');

### end ###
