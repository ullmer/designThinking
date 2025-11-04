import yaml
from tkinter import *

yfn = 'projCats.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)

def getCategories(yamlData):
  result = list(yamlData.keys())
  return result

def getCatEntries(yamlData, whichCategory):
  result = yamlData[whichCategory]
  return result

def helloCB():
  print("hello was pushed")

root      = Tk() 

categories = getCategories(yd)

for category in categories:
  f    = Frame(root); f.pack(side=LEFT)
  b    = Button(f, text=category, command=helloCB, width=15)
  b.pack()

  subthemes = getCatEntries(yd, category)
  for subtheme in subthemes:
    b2 = Button(f, text=subtheme, width=15)
    b2.pack()

root.mainloop()                                          

# https://en.wikipedia.org/wiki/Tkinter
### end ###
