# https://en.wikipedia.org/wiki/Tkinter

from tkinter import *
from socDb   import *

soc = socDb()

def helloCB():
  print("hello was pushed")

root      = Tk() 
divisions = soc.getDivisions()

for division in divisions:
  w    = Button(root, text=division, command=helloCB)
  w.pack()

root.mainloop()                                          

#getFacultyByDivision

### end ###
