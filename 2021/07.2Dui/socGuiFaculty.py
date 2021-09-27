# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter   import *
from socDb     import *
from functools import partial

#####################################################################################
##################### Clemson School of Computing GUI : Faculty ##################### 
#####################################################################################

class socGuiFaculty:
  tkRoot       = None
  colWidth     = 17

  fontBase     = "Sans"
  fontSize     = 12
  headerFont   = None
  bodyFont     = None

  socDivisions = None
  div2but      = None #division to button
  faculty2but  = None #faculty to button
  soc          = None

  ##################### constructor ##################### 

  def __init__(self, tkRoot):

    self.soc         = socDb()
    self.tkRoot      = tkRoot
    self.div2but     = {}
    self.faculty2but = {}
    self.buildGui()

  ##################### constructor ##################### 
  
  def buildGui(self):
    self.headerFont   = (self.fontBase, str(self.fontSize), 'bold')
    self.bodyFont     = (self.fontBase, str(self.fontSize))
    self.socDivisions = self.soc.getDivisions()
  
    for division in self.socDivisions:
      divisionFrame  = Frame(self.tkRoot); divisionFrame.pack(side=LEFT, anchor=N)
  
      cb = partial(self.divisionCb, division)
      b  = Button(divisionFrame, text=division, command=cb, width=self.colWidth, font=self.headerFont)
      b.pack(side=TOP); self.div2but[division] = b
  
      divisionFaculty = self.soc.getFacultyByDivision(division)
  
      for faculty in divisionFaculty:
        cb = partial(self.facultyCb, faculty)
        b  = Button(divisionFrame, text=faculty, command=cb, font=self.bodyFont)
        b.pack(side=TOP, expand=True, fill=BOTH); self.faculty2but[faculty] = b
  
  ##################### callbacks ##################### 

  def divisionCb(self, whichDivision):
    print("division %s was pushed" % whichDivision)

  def facultyCb(self, whichFaculty):
    print("faculty %s was pushed" % whichFaculty)

### end ###
