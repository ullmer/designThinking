# Export Element representations from NIH NLM periodic tables
# Brygg Ullmer, Clemson University
# Begun 2022-10-26

from edTable import *
import os

ed = edPerTable()

tableNames = ed.getTableNames()
elements   = ed.getElements()

for table in tableNames:
  path = ed.getVal('imgPath')
  dirname = '%s/%s' % (path, table)
  print(dirname)

  try:
    os.mkdir(dirname)
  except:
    print("error attempting to create directory", dirname)

  imgSrc = ed.getTableImage(table)

  for element in elements:
    x1, y1 = ed.getElementPos2(element)
    x2, y2 = (x1 + ed.getCellsWide(), y1 + ed.getCellsHigh())
    imgTarg = imgSrc.crop((x1,y1,x2,y2))
    imgFn   = '%s/%s.png' % (imgSrc, element)
    print("writing", imgFn)
    imgTarg.save(imgFn)

### end ###
