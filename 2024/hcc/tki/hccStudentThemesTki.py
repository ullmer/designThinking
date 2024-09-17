# Tkinter wrappers around HCC student themes class
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter import *
import traceback 

from hccStudentThemes import *

####### Functionality for viewing themes data ####### 

class studentThemesTki(studentThemes):

  frameText  = None 
  frameWidth = 100

  tkiFrame   = None
  tkiTextbox = None
  scrollbar  = None

  bg = '#333'
  fg = '#ccc'

  #inherited studentThemes functions
  #__init__()
  #loadYaml()
  #getStudentKeys()
  #getStudentVals(studentKey)
  #getCategories()
  #getCatEntries(whichCategory)
  #getAbbrevThemeList()
  #retrieveThemeData(themeName)

  ################## constructor ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()

  ################## build student theme view ##################

  def buildStudentThemeView(self, parentTkiWidget, studentKey):
    self.tkiFrame = Frame(parentTkiWidget)
    self.tkiFrame.pack(expand=True, fill=BOTH)

    sv             = self.getStudentVals(studentKey)
    self.frameText = str(sv)

    self.tkiTextbox   = Text(self.tkiFrame, width=self.frameWidth, bg=self.bg, fg=self.fg)
    self.tkiTextbox.insert(END, self.frameText)

    self.tkiTextbox.pack(expand=True, fill=BOTH, side=LEFT)

    self.scrollbar = Scrollbar(self.tkiFrame, command=self.tkiTextbox.yview)
    self.scrollbar.pack(side=RIGHT, fill=Y)
    self.tkiTextbox.config(yscrollcommand=self.scrollbar.set)

    return self.tkiFrame

  ################## update student theme view ##################

  def updateStudentThemeView(self, studentKey): 
    sv             = self.getStudentVals(studentKey)
    self.frameText = str(sv)

    self.tkiTextbox.delete(1.0, END)
    self.tkiTextbox.insert(END, self.frameText)

  ################## display student theme ##################

  def displayStudentTheme(self, subtheme):
    themeData = self.retrieveThemeData(subtheme)

    self.tkiTextbox.delete(1.0, END) #clear existing text
    self.tkiTextbox.delete(1.0, END)

    if   type(themeData) is list: 
      themeText=''.join(themeData)
      self.tkiTextbox.insert(END, themeText)
      return

    if type(themeData) is dict: 
      try:
        #name     = themeData['name']
        #theme    = themeData['possibleProjectTheme']
        #stSkills = themeData['classRelevantSkills']
        #paSkills = themeData['partnerSkillInterests']

        self.tkiTextbox.tag_configure('bold', font=('Calibri', 13, 'bold'))
        self.tkiTextbox.tag_configure('norm', font=('Calibri', 11))
      
        row = 1
        for key in ['name', 'possibleProjectTheme', 'classRelevantSkills', 'partnerSkillsInterests']:
          try:
            val    = themeData[key]
            val2   = str(val).replace("\n",'')+"\n\n"
            keyLen = len(key); valLen = len(val2)
            coord1 = "%i.0"  % (row)
            coord2 = "%i.%i" % (row, keyLen+2)
            coord3 = "%i.%i" % (row, keyLen+valLen+2)
          
            self.tkiTextbox.insert(coord1, key+': ')
            self.tkiTextbox.insert(coord2, val2)
            self.tkiTextbox.tag_add("bold", coord1, coord2)
            self.tkiTextbox.tag_add("norm", coord2, coord3)
            row += val.count('\n')+1
          except: print("displayStudentTheme: ignoring problem with key", key); traceback.print_exc()

        #self.tkiTextbox.insert("1.0",   "name: ")
        #self.tkiTextbox.insert(END,   name + "\n")

        #self.tkiTextbox.insert(END,   "theme: ")
        #self.tkiTextbox.insert(END,  theme)

        #self.tkiTextbox.tag_add("norm", "1.6", "2.0") 
        #self.tkiTextbox.tag_add("norm", "2.7", END)
        #self.tkiTextbox.tag_add("bold", "1.0", "1.5")
        #self.tkiTextbox.tag_add("bold", "2.0", "2.6")

      except: print("displayStudent theme challenge"); traceback.print_exc()

########### main ##############
#if __name__ == "__main__":
#  st = studentThemes()
#  print("student keys:", st.getStudentKeys())
#  print("categories:",   st.getCategories())

### end ###
