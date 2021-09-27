# https://en.wikipedia.org/wiki/Tkinter

from tkinter   import *
from socDb     import *
from functools import partial

soc = socDb()

def divisionCb(whichDivision):
  print("division %s was pushed" % whichDivision)

def facultyCb(whichFaculty):
  print("faculty %s was pushed" % whichFaculty)

root       = Tk() 
divisions  = soc.getDivisions()
colWidth   = 17
headerFont = ('Sans','12','bold')
bodyFont   = ('Sans','12')

#https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/
#https://www.geeksforgeeks.org/partial-functions-python/
#https://stackoverflow.com/questions/15331726/how-does-functools-partial-do-what-it-does
#https://stackoverflow.com/questions/2297336/tkinter-specifying-arguments-for-a-function-thats-called-when-you-press-a-butt

for division in divisions:
  divisionFrame  = Frame(root); divisionFrame.pack(side=LEFT, anchor=N)

  b    = Button(divisionFrame, text=division, command=partial(divisionCb,division),
                width=colWidth, font=headerFont)
  b.pack(side=TOP)

  divisionFaculty = soc.getFacultyByDivision(division)
  for faculty in divisionFaculty:
    b    = Button(divisionFrame, text=faculty, command=partial(facultyCb, faculty),
                  font=bodyFont)
    b.pack(side=TOP, expand=True, fill=BOTH)

root.mainloop()                                          


### end ###
