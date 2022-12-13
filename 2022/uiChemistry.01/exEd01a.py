# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

from edElements import *

ed = edElements()
print('>> Elements: ' + str(ed.getElementList()))
print('>> Aluminum: ' + str(ed.getElementByFullname('aluminium')))
print('>> Column 1: ' + str(ed.getElsByCol(1)))
print('>> Table dimensions: ' + str(ed.getTableDimensions()))
#print(ed.getFullnameMatrix())
print('>> Symbol matrix: ' + str(ed.getSymbolMatrix()))
print('>> Block S: ' + str(ed.getBlockId('s')))
print('>> Block P: ' + str(ed.getBlockId('p')))
print('>> Block D: ' + str(ed.getBlockId('d')))
print('>> Block F: ' + str(ed.getBlockId('f')))

### end ###

