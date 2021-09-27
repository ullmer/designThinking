# https://en.wikipedia.org/wiki/Tkinter

from tkinter   import *
from socDb     import *
from functools import partial

soc = socDb()

def divisionCb(whichCategory):
  print("division %s was pushed" % whichCategory)

root       = Tk() 
divisions  = soc.getDivisions()
colWidth   = 20
headerFont = ('Sans','12','bold')
bodyFont   = ('Sans','12')

#https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/
#https://www.geeksforgeeks.org/partial-functions-python/
#https://stackoverflow.com/questions/15331726/how-does-functools-partial-do-what-it-does
#https://stackoverflow.com/questions/2297336/tkinter-specifying-arguments-for-a-function-thats-called-when-you-press-a-butt

for division in divisions:
  divisionFrame  = Frame(root)
  b    = Button(divisionFrame, text=division, command=partial(divisionCb,division),
                width=colWidth, font=headerFont)

  #b    = Button(root, text=division, command=lambda: divisionCb(division),
  b.pack(side=LEFT)

root.mainloop()                                          

#getFacultyByDivision

### end ###
