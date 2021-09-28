# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter   import *
from functools import partial
from socDb         import *
from socGuiFaculty import *

soc = socDb()

root = Tk() 
gui  = socGuiFaculty(root)

facultyInRank = soc.getFacultyByRank('asst')
for faculty in facultyInRank:
  gui.highlightFaculty(faculty)

root.mainloop()                                          



### end ###
