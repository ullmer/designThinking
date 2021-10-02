# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter   import *
from functools import partial
from enoDb     import *
from socGui    import *

sqliteDbFn   = 'soc.db3'
queriesYFn   = 'soc-queries.yaml'
soc = enoDb(sqliteDbFn, queriesYFn)

root = Tk() 
facultyGui      = socGuiFaculty(soc,       root)
rankGui         = socGuiRank(soc,          root, facultyGui)
researchAreaGui = socGuiResearchAreas(soc, root, facultyGui)

root.mainloop()                                          

### end ###
