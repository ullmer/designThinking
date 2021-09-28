# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter   import *
from functools import partial
from socDb     import *
from socGui    import *

soc = socDb()

root = Tk() 
facultyGui      = socGuiFaculty(soc,       root)
rankGui         = socGuiRank(soc,          root, facultyGui)
researchAreaGui = socGuiResearchAreas(soc, root, facultyGui)

root.mainloop()                                          

### end ###
