# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

import yaml
import os, glob, traceback #file pattern matching

####### Functionality for reading and processing student themes data ####### 

class studentThemes:
  verbose           = False
  studentYamlData   = None
  studentLookupDict = None
  themeLookupDict   = None
  projCatsYd        = None
  projCatsYFn       = 'projCats.yaml'
  studentYamlFns    = 'themes/yaml/*.yaml' #
  studentLookupTxt  = 'basap:How Cultur;becke:MCI & AI S;child:Technology assist;coene:Technology-Driv;' + \
    'futia:reducing bias;gozub:Dark Patte;gurri:HCC within;guynu:Autonomous;jiang:AI in Ment;lawso:Working Th;' + \
    'liuna:Trust in A;mcalh:Most effec;mcgra:Genetic Se;mille:Assisting;nguye:team cogni;visse:AI in Educ;' + \
    'wangy:Human Insp;wangz:AI vs Huma;woodw:Cognitive ;wuyun:More inclusive;xudan:autopilot ;yanji:privacy en;' + \
    'yorkd:dummy-proo'

  ################## constructor, error ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    self.studentYamlData = {}
    self.loadYaml() 
    self.mapStudentLookups()

  ########### map student lookups -- heuristic to connect themes with source yaml files ###########
 
  def mapStudentLookups(self): # if the YAML were mostly parsing, this would not be necessary, but meanwhile
    self.studentLookupDict = {}
    self.themeLookupDict   = {}

    pairs = self.studentLookupTxt.split(';') #first, break apart on semicolons

    for pair in pairs:
      student, theme = pair.split(':')
      self.studentLookupDict[student] = theme
      self.themeLookupDict[theme]     = student

  ########### load YAML data ########### 
      
  def loadYaml(self):
    yf = open(self.projCatsYFn, 'rt')
    self.projCatsYd = yaml.safe_load(yf)
    
    filenames = glob.glob(self.studentYamlFns)
    for filename in filenames:
      bn = os.path.basename(filename) #removes directory prefix
      studentName1 = bn[:-5] #removes .yaml extension
      if self.verbose: print(studentName1)
      try:
        yf = open(filename, 'rt')
        self.studentYamlData[studentName1] = yaml.safe_load(yf)
        yf.close()
      except:  # we encountered a problem in reading the YAML.  As fallback, read in the raw text
        yf.close() # the file probably remains open, but we need to re-read as plaintext
        yf = open(filename, 'rt')
        rawlines = yf.readlines() #we call these "rawlines," because each line includes newline characters
        yf.close()
        self.studentYamlData[studentName1] = rawlines

        if self.verbose: print('='*15 + studentName1); traceback.print_exc() #print error
    if self.verbose: print(self.studentYamlData)

  ########### get student keys ########### 

  def getStudentKeys(self):
    result = list(self.studentYamlData.keys())
    return result

  ########### get student vals ########### 

  def getStudentVals(self, studentKey):
    if studentKey not in self.studentYamlData:
      print("studentThemes getStudentVals called on", studentKey, "but no data present")
      return None

    studentThemeInfo = self.studentYamlData[studentKey]

    if type(studentThemeInfo) is list: #we have a list of raw text; join it back together
      result = ''.join(studentThemeInfo)

    elif type(studVal) is dict: 
      return studentThemeInfo

    else: result = "No information found"

    return result

  ########### get abbreviated theme list vals ########### 

  def getAbbrevThemeList(self): 
    if self.themeLookupDict is None: return None
    result = list(self.themeLookupDict.keys())
    return result

  ########### retrieve theme student match ########### 

  def retrieveThemeData(self, themeName): #uses "full" theme names, and matches on abbreviated
    if self.verbose: print("retrieveThemeData:", themeName)

    themeAbbrevs = self.getAbbrevThemeList()
    if themeAbbrevs is None: return None

    studAbbrev = None
    for themeAbbrev in themeAbbrevs:
      if self.verbose: print(">", themeAbbrev)

      if themeName.find(themeAbbrev) >= 0: #we have a theme match
        studAbbrev = self.themeLookupDict[themeAbbrev]; break

    if studAbbrev is None: return None # no data found.

    studentKeys = self.getStudentKeys()
    for studentKey in studentKeys:
      if studentKey.find(studAbbrev) >= 0: #we have a student match
        if studentKey not in self.studentYamlData:
          print("retrieveThemeData problem: student not found:", studentKey); return None
        result = self.studentYamlData[studentKey]
        return result

    return None

  ########### get project categories ########### 

  def getCategories(self):
    result = list(self.projCatsYd.keys())
    return result

  ########### get category entries ########### 

  def getCatEntries(self, whichCategory):
    result = self.projCatsYd[whichCategory]
    return result

########### main ##############
if __name__ == "__main__":
  st = studentThemes()
  print("student keys:", st.getStudentKeys())
  print("categories:",   st.getCategories())

### end ###
