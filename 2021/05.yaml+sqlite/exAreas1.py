# Process Clemson School of Computing research areas
# Brygg Ullmer, Clemson University, 2021-09-16

import yaml

yfn = 'soc-research-categories.yaml'
yf  = open(yfn, 'r+t')
yd  = yaml.safe_load(yf)  #yd: yaml data

#print(yd)
categories = yd.keys()
personHash = {}

for category in categories:
  fields    = yd[category]
  numFields = len(fields)
  print("\n==== %s (%i) ====" % (category, numFields))

  print

  for field in fields:
    numPeople = len(fields[field])
    print("%s (%i)" % (field, numPeople))

    for faculty in fields[field]:
      if faculty not in personHash: personHash[faculty] = []
      personHash[faculty].append(field)

print("VBZ: ", str(personHash['Victor Zordan']))

### end ###
