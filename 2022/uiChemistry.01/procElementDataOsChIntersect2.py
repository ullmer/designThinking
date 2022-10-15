# Brygg Ullmer and Miriam Konkel
# Intersecting periodic table of the elements with OpenStax Chemistry 2e textbook
# Begun 2022-10-15

from edElements import *
import yaml

ed       = edElements()
elements = ed.getElementList()

yfn = 'os-chemistry-2e6.yaml'
yf  = open(yfn, 'rt')
y   = yaml.safe_load(yf)
yd  = y['collection']['content']
print(yd)

countFilesDir = 'os-chem2e-elements'

for element in elements: 
  #execStr = 'grep -ic %s %s > %s/%s' % (element, sourceFiles, targetFiles, element)
  #print(execStr)
  pass

### end ###

