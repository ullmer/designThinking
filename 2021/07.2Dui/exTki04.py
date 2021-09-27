# https://en.wikipedia.org/wiki/Tkinter

from tkinter import *
from socDb   import *

soc = socDb()

def helloCB():
  print("hello was pushed")

root      = Tk() 
divisions = soc.getDivisions()
colWidth  = 30

for division in divisions:
  w    = Button(root, text=division, command=helloCB, width=colWidth)
  w.pack(side=LEFT)

root.mainloop()                                          

#getFacultyByDivision

### end ###
