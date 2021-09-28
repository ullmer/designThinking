# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter   import *
from functools import partial
from socDb     import *
from socGui    import *

soc = socDb()

root = Tk() 
gui  = socGuiFaculty(soc, root)

facultyInRank = soc.getFacultyByRank('asst')
gui.highlightFaculty(facultyInRank)

#gui.clearHighlightedFaculty()

root.mainloop()                                          

### end ###
