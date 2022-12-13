# Brygg Ullmer and Miriam Konkel
# Intersecting periodic table of the elements with OpenStax Chemistry 2e textbook
# Begun 2022-10-15

from edElements import *

ed       = edElements()
elements = ed.getElementList()

sourceFiles = 'osbooks-chemistry-bundle/modules/*/*'
targetFiles = 'os-chem2e-elements'

for element in elements: 
  execStr = 'grep -ic %s %s > %s/%s' % (element, sourceFiles, targetFiles, element)
  print(execStr)

### end ###

