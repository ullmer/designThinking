# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter import *
import traceback 

from hccStudentThemes import *

####### Functionality for viewing themes data ####### 

class studentThemesTki(studentThemes):

  frameText  = 40 #~characters
  frameWidth = 40 #~characters

  tkiFrame   = None
  tkiMsg     = None

  #inherited studentThemes functions
  #__init__()
  #loadYaml()
  #getStudentKeys()
  #getStudentVals(studentKey)
  #getCategories()
  #getCatEntries(whichCategory)

  ################## constructor, error ##################

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    super().__init__()

  def buildStudentThemeView(self, parentTkiWidget, studentKey):
    self.tkiFrame = Frame(parentTkiWidget)
    self.tkiFrame.pack(expand=True, fill=BOTH)

    #frameText = None
    sv = self.getStudentVals(studentKey)
    self.frameText = str(sv)

    self.tkiMsg   = Message(self.tkiFrame, width=self.frameWidth, text=self.frameText)
    self.tkiMsg.pack(expand=True, fill=BOTH)
    return self.tkiFrame

  def clearStudentThemeView(self): pass

########### main ##############
#if __name__ == "__main__":
#  st = studentThemes()
#  print("student keys:", st.getStudentKeys())
#  print("categories:",   st.getCategories())

### end ###
