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

# Create dictionaries for mappings
element2lines      = {}
chapter2modules    = {}
element2chapters   = {}
chapter2elements   = {}
elementModuleCount = {}

for element in elements:
  fn = '%s/%s' % (countFilesDir, element)
  f  = open(fn, 'rt')
  rawlines = f.readlines()
  element2lines[element] = rawlines
  elementModuleCount[element] = {}

  for line in rawlines:
    cleanline = line.rstrip() #remove trailing newline
    module, count = cleanline.split(' ')

for chapter in yd: #iterate through chapters
  print

for element in elements: 
  #execStr = 'grep -ic %s %s > %s/%s' % (element, sourceFiles, targetFiles, element)
  #print(execStr)
  pass

### end ###

