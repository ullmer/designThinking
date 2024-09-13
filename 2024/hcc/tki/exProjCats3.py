# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

import yaml
import os, glob, traceback #file pattern matching
from tkinter import *

yfn = 'projCats.yaml'
yf  = open(yfn, 'rt')
yd  = yaml.safe_load(yf)
print(yd)

####### small class for ingesting student themes data ####### 
class studentThemes:
  studentYamlData = None
  studentYamlFns  = 'themes/yaml/*.yaml' #

  def __init__(self): self.studentYamlData = {}; self.loadYaml() # "constructor"

  def loadYaml(self):
    filenames = glob.glob(self.studentYamlFns)
    for filename in filenames:
      bn = os.path.basename(filename) #removes directory prefix
      studentName1 = bn[:-5] #removes .yaml extension
      print(studentName1)
      try:
        yf = open(filename, 'rt')
        self.studentYamlData[studentName1] = yaml.safe_load(yf)
        yf.close()
      except: 
        self.studentYamlData[studentName1] = True; 
        print('='*15 + studentName1); traceback.print_exc() #print error
    print(self.studentYamlData)


def getCategories(yamlData):
  result = list(yamlData.keys())
  return result

def getCatEntries(yamlData, whichCategory):
  result = yamlData[whichCategory]
  return result

def helloCB():
  print("hello was pushed")

root = Tk() 
cw   = 25 #column width
headerFont = ('Sans','12','bold')
bodyFont   = ('Sans','12')

categories = getCategories(yd)
studTh     = studentThemes()

for category in categories:
  f    = Frame(root); f.pack(side=LEFT, anchor="n") #anchor to the north
  b    = Button(f, text=category, command=helloCB, font=headerFont, bg='#aaa')
  b.pack(expand=True, fill=BOTH)

  subthemes = getCatEntries(yd, category)
  for subtheme in subthemes:
    b2 = Button(f, text=subtheme, width=cw, anchor="w", font=bodyFont) #anchor to the west means left-aligned
    b2.pack(side=TOP)

root.mainloop()                                          

# https://en.wikipedia.org/wiki/Tkinter
### end ###
