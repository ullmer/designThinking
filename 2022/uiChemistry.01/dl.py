# Export Element representations from NIH NLM periodic tables
# Brygg Ullmer, Clemson University
# Begun 2022-10-26

from edTable import *
import os

ed = edPerTable()

tableNames = ed.getTableNames()

baseurl='https://pubchem.ncbi.nlm.nih.gov/periodic-table/png/'

path = ed.getVal('imgPath')

for table in tableNames:
  fn      = ed.getVal('tables')[table][1]
  cmd = 'wget %s%s' % (baseurl, fn)
  print(cmd)

### end ###
