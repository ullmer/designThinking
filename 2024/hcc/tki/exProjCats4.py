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
  studentYamlData   = None
  studentLookupDict = None
  studentYamlFns     = 'themes/yaml/*.yaml' #
  studentLookupTxt   = 'basap:How Cultur;becke:MCI & AI S;child:Technology;coene:Technology;' +
    'futia:3 to 5 wor;gozub:Dark Patte;gurri:HCC within;guynu:Autonomous;jiang:AI in Ment;lawso:Working Th' +
    ';liuna:Trust in A;mcalh:Most effec;mcgra:Genetic Se;mille:Assisting ;nguye:team cogni;visse:AI in Educ;' +
    'wangy:Human Insp;wangz:AI vs Huma;woodw:Cognitive ;wuyun:uyuntaoli.;xudan:autopilot ;yanji:privacy en;' +
    'yorkd:dummy-proo;'

  def __init__(self): self.studentYamlData = {}; self.loadYaml() # "constructor"

  def mapStudentLookups(self): # if the YAML were mostly parsing, this would not be necessary, but meanwhile
    self.studentLookupDict = {}
    pairs = self.studentLookupTxt.split(';') #first, break apart on semicolons

    for pair in pairs:
      student, theme = pair.split(':')
      self.studentLookupPair[student] = theme
      

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
