# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

import yaml
import os, glob, traceback #file pattern matching

####### small class for ingesting student themes data ####### 

class studentThemes:

  studentYamlData   = None
  studentLookupDict = None
  projCatsYd        = None
  projCatsYFn       = 'projCats.yaml'
  studentYamlFns    = 'themes/yaml/*.yaml' #
  studentLookupTxt  = 'basap:How Cultur;becke:MCI & AI S;child:Technology assist;coene:Technology-Driv;' +
    'futia:reducing bias;gozub:Dark Patte;gurri:HCC within;guynu:Autonomous;jiang:AI in Ment;lawso:Working Th;' +
    'liuna:Trust in A;mcalh:Most effec;mcgra:Genetic Se;mille:Assisting;nguye:team cogni;visse:AI in Educ;' +
    'wangy:Human Insp;wangz:AI vs Huma;woodw:Cognitive ;wuyun:More inclusive;xudan:autopilot ;yanji:privacy en;' +
    'yorkd:dummy-proo'

  def __init__(self): self.studentYamlData = {}; self.loadYaml() # "constructor"

  def mapStudentLookups(self): # if the YAML were mostly parsing, this would not be necessary, but meanwhile
    self.studentLookupDict = {}
    pairs = self.studentLookupTxt.split(';') #first, break apart on semicolons

    for pair in pairs:
      student, theme = pair.split(':')
      self.studentLookupPair[student] = theme
      
  def loadYaml(self):
    yf = open(self.projCatsYFn, 'rt')
    self.projCatsYd = yaml.safe_load(yf)
    
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

  def getStudentKeys(self):
    result = list(self.studentYamlData.keys())
    return result

  def getCategories(self):
    result = list(self.projCatsYd.keys())
    return result

  def getCatEntries(self, whichCategory):
    result = self.projCatsYd[whichCategory]
    return result

### end ###
