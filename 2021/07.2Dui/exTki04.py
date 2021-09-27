# https://en.wikipedia.org/wiki/Tkinter

from tkinter import *
from socDb   import *

soc = socDb()

def helloCB():
  print("hello was pushed")

root       = Tk() 
divisions  = soc.getDivisions()
colWidth   = 20
headerFont = ('Sans','12','bold')
bodyFont   = ('Sans','12')

for division in divisions:
  w    = Button(root, text=division, command=helloCB, 
                width=colWidth, font=headerFont)
  w.pack(side=LEFT)

root.mainloop()                                          

#getFacultyByDivision

### end ###
