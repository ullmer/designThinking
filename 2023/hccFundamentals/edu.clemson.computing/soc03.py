# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter   import *
from functools import partial
from enoDb     import *
from socGui    import *
try: from tkmacosx import Button
except: 
  print("If running on a Mac, buttons will not change color until tkmacosx installed") 
#https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os

sqliteDbFn   = 'soc.db3'
queriesYFn   = 'soc-queries.yaml'
soc = enoDb(sqliteDbFn, queriesYFn)

root = Tk() 
facultyGui      = socGuiFaculty(soc,       root)
rankGui         = socGuiRank(soc,          root, facultyGui)
researchAreaGui = socGuiResearchAreas(soc, root, facultyGui)

root.mainloop()                                          

### end ###
