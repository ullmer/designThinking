import yaml
from tkinter import *

yfn = 'projCats.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)

def helloCB():
  print("hello was pushed")

root      = Tk() 

categories = [1,2,3]

for category in categories:
  w    = Button(root, text=category, command=helloCB)
  w.pack()

root.mainloop()                                          

# https://en.wikipedia.org/wiki/Tkinter
### end ###
