# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

import yaml
fn = 'index.yaml'
f  = open(fn, 'rt')
yd = yaml.safe_load(f)
print(yd)

yc = yd['class']

for classDate in yc:
  classPeriod = yc[classDate]
  for reading in classPeriod:
    r = classPeriod[reading]
    
