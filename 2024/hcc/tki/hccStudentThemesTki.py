# Tkinter wrappers around HCC student themes class
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter import *
import traceback 

from hccStudentThemes import *

####### Functionality for viewing themes data ####### 

class studentThemesTki(studentThemes):

  frameText  = None 
  frameWidth = 80

  tkiFrame   = None
  tkiTextbox = None
  scrollbar  = None

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

    self.tkiTextbox   = Text(self.tkiFrame, width=self.frameWidth)
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

  ################## update theme view ##################

  def updateThemeView(self, themeViewText): 
    self.frameText = str(themeViewText)

    self.tkiTextbox.delete(1.0, END)
    self.tkiTextbox.insert(END, self.frameText)

  ################## display student theme ##################

  def displayStudentTheme(self, subtheme):
    themeData = self.retrieveThemeData(subtheme)
    self.updateThemeView(themeData)

########### main ##############
#if __name__ == "__main__":
#  st = studentThemes()
#  print("student keys:", st.getStudentKeys())
#  print("categories:",   st.getCategories())

### end ###
