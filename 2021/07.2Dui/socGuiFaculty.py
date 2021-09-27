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

  colHdr1Bg     = '#531'
  colHdr1Fg     = '#fff'

  colHdr2Bg     = '#555'
  colHdr2Fg     = '#fff'

  colRowBg1    = '#eee'
  colRowBg2    = '#ccc'

  colHL1       = '#fc5'

  socDivisions   = None
  div2but        = None #division to button
  faculty2but    = None #faculty to button
  faculty2rowNum = None #faculty to button
  soc            = None

  ##################### constructor ##################### 

  def __init__(self, tkRoot):
    self.soc         = socDb()
    self.tkRoot      = tkRoot

    self.div2but        = {}
    self.faculty2but    = {}
    self.faculty2rowNum = {}

    self.buildGui()

  ##################### constructor ##################### 
  
  def buildGui(self):
    self.headerFont   = (self.fontBase, str(self.fontSize), 'bold')
    self.bodyFont     = (self.fontBase, str(self.fontSize))
    self.socDivisions = self.soc.getDivisions()
  
    facultyFrame = Frame(self.tkRoot)
    facultyFrame.pack()

    h1 = Label(facultyFrame, text="faculty", 
               bg=self.colHdr1Bg, fg=self.colHdr1Fg, font=self.headerFont)
    h1.pack(side=TOP, expand=True, fill=X)

    divisionsFrame = Frame(facultyFrame)
    divisionsFrame.pack(side=TOP, expand=True, fill=BOTH)
  
    for division in self.socDivisions:
      divisionFrame  = Frame(divisionsFrame); divisionFrame.pack(side=LEFT, anchor=N)

      cb = partial(self.divisionCb, division)
      b  = Button(divisionFrame, text=division, command=cb, width=self.colWidth, 
                  font=self.headerFont, bg = self.colHdr2Bg, fg = self.colHdr2Fg)

      b.pack(side=TOP); self.div2but[division] = b
  
      divisionFaculty = self.soc.getFacultyByDivision(division)
  
      rowNum = 1
      for faculty in divisionFaculty:
        cb = partial(self.facultyCb, faculty)
        if rowNum % 2 == 0: rbg = self.colRowBg1 # row background
        else:               rbg = self.colRowBg2

        b  = Button(divisionFrame, text=faculty, command=cb, font=self.bodyFont, bg=rbg)
        self.faculty2rowNum[faculty] = rowNum
    
        b.pack(side=TOP, expand=True, fill=BOTH); self.faculty2but[faculty] = b
        rowNum += 1
  
  ##################### highlightFaculty ##################### 

  def highlightFaculty(self, faculty): # accept either singular name, or list of names

    flist = faculty
    if isinstance(faculty, list) is False: flist = [faculty]  #convert to a list if not already

    for name in flist:
      if name in self.faculty2but:
        b = self.faculty2but[name]
        #b.itemconfig(bg=self.colHL1)
        b.configure(bg=self.colHL1)
      else: print("socGUIFaculty.highlightFaculty: problem argument:", name)

  ##################### callbacks ##################### 

  def divisionCb(self, whichDivision):
    print("division %s was pushed" % whichDivision)

  def facultyCb(self, whichFaculty):
    print("faculty %s was pushed" % whichFaculty)

### end ###
