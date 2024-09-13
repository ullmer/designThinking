import yaml
from tkinter import *

yfn = 'projCats.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)

def getCategories(yamlData):
  result = list(yamlData.keys())
  return result

def helloCB():
  print("hello was pushed")

root      = Tk() 

categories = getCategories(yd)

for category in categories:
  w    = Button(root, text=category, command=helloCB, width=15)
  w.pack(side=LEFT)

root.mainloop()                                          

# https://en.wikipedia.org/wiki/Tkinter
### end ###
