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

  for field in fields:
    for faculty in fields[field]:
      if faculty not in personHash: personHash[faculty] = []
      personHash[faculty].append(field)

faculty = personHash.keys()
allInitials = []

print("divisions:")
for person in faculty:
  print("    ", person)

### end ###
