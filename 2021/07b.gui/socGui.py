# Example Clemson School of Computing GUI
# By Brygg Ullmer, Clemson University
# Begun 2021-09-27

from tkinter     import *
#from tkinter.ttk import *
from enoDb       import *
from functools   import partial

#############################################################################
################# Clemson School of Computing GUI : Base    #################
#############################################################################

class socGuiBase:
  soc            = None
  tkRoot         = None
  colWidth       = 17

  fontBase       = "Sans"
  titleFontSize  = 18
  fontSize       = 12
  titleFont      = None
  headerFont     = None
  bodyFont       = None

  colHdr1Bg = '#531'
  colHdr1Fg = '#fff'

  colHdr2Bg = '#555'
  colHdr2Fg = '#fff'

  colRowBg1 = '#eee'
  colRowBg2 = '#ccc'

  colHL1    = '#fc5'
  colHL2    = '#d84'
  #colHL2    = '#d08040'
  
  bodyFrame          = None
  bodyFramePacked    = None

  ##################### constructor ##################### 

  def __init__(self, soc, tkRoot):
    self.soc         = soc
    self.tkRoot      = tkRoot

    self.buildFonts()

  ##################### buildFonts ##################### 

  def buildFonts(self):
    self.titleFont    = (self.fontBase, str(self.titleFontSize), 'bold')
    self.headerFont   = (self.fontBase, str(self.fontSize), 'bold')
    self.bodyFont     = (self.fontBase, str(self.fontSize))

  ##################### callbacks ##################### 

  def bodyCb(self, whichFacet):
    print("body %s was selected" % whichFacet)
    if self.bodyFramePacked: self.bodyFrame.pack_forget(); self.bodyFramePacked = False
    else:                    self.bodyFrame.pack();        self.bodyFramePacked = True

##################################################################################
##################### Clemson School of Computing GUI : Rank ##################### 
##################################################################################

class socGuiRank(socGuiBase):
  socRanks           = None
  rank2but           = None 
  rank2rowNum        = None 
  socHighlightedRank = None
  facultyGui         = None

  ##################### constructor ##################### 

  def __init__(self, soc, tkRoot, facultyGui):
    super().__init__(soc, tkRoot) # call parent (socGuiBase) constructor
    self.rank2but    = {}
    self.rank2rowNum = {}

    self.buildGui()
    self.facultyGui = facultyGui

  ##################### constructor ##################### 
  
  def buildGui(self):
    #self.socRanks = self.soc.getRanks()
    expandedRanks = self.soc.getRanksExpanded([])
    print('expandedRanks:', str(expandedRanks))

    ranksFrame = Frame(self.tkRoot)
    ranksFrame.pack(side=LEFT, anchor=N)

    cb = partial(self.bodyCb, "rank")
    h1 = Button(ranksFrame, text="rank", command=cb,
                bg=self.colHdr1Bg, fg=self.colHdr1Fg, font=self.titleFont)
    h1.pack(side=TOP, expand=True, fill=X)

    self.bodyFrame = rankFrame  = Frame(ranksFrame); rankFrame.pack(side=TOP, anchor=N)

    rowNum = 1
    self.socRanks = []

    for erank in expandedRanks:
      rank, fullRankName = erank
      self.socRanks.append(rank)
      cb = partial(self.rankCb, rank)

      if rowNum % 2 == 0: rbg = self.colRowBg1 # row background
      else:               rbg = self.colRowBg2

      b  = Button(rankFrame, text=fullRankName, command=cb, width=self.colWidth, 
                  font=self.bodyFont, bg = rbg)

      b.pack(side=TOP); self.rank2but[rank] = b
      self.rank2rowNum[rank] = rowNum
      rowNum += 1

    self.bodyFramePacked = True

  ##################### callbacks ##################### 

  def rankCb(self, whichRank):
    print("rank %s was selected" % whichRank)
    facultyInRank = self.soc.getFacultyByRank(whichRank)

    #highlight self appropriately
    self.clearHighlightedRanks()
    self.highlightRank(whichRank, 'primaryFocus')

    #highlight entangled faculty
    self.facultyGui.clearHighlightedFaculty()
    self.facultyGui.highlightFaculty(facultyInRank)

  ##################### highlightRank ##################### 

  def highlightRank(self, rank, highlightColor='defaultHighlight'): 

    rlist = rank
    if isinstance(rank, list) is False: rlist = [rank]  #convert to a list if not already

    self.socHighlightedRank = []
    for rank in rlist:
      if rank in self.rank2but:
        b = self.rank2but[rank]
        if highlightColor == 'defaultHighlight': b.configure(bg=self.colHL1)
        else:                                    b.configure(bg=self.colHL2)
        self.socHighlightedRank.append(rank)
      else: print("socGUIRank.highlightRank: problem argument:", rank)

  ##################### clear Highlighted Ranks ##################### 

  def clearHighlightedRanks (self): 
    if self.socHighlightedRank == None or self.socHighlightedRank == []:
      return

    for rank in self.socHighlightedRank:
      button = self.rank2but[rank]
      rowNum = self.rank2rowNum[rank]
      if rowNum % 2 == 0: rbg = self.colRowBg1 # row background
      else:               rbg = self.colRowBg2
      button.configure(bg=rbg)

#####################################################################################
##################### Clemson School of Computing GUI : Faculty ##################### 
#####################################################################################

class socGuiFaculty(socGuiBase):
  socDivisions   = None
  div2but        = None #division to button
  faculty2but    = None #faculty to button
  faculty2rowNum = None #faculty to button
  socHighlightedFaculty = None

  ##################### constructor ##################### 

  def __init__(self, soc, tkRoot):
    super().__init__(soc, tkRoot) # call parent (socGuiBase) constructor

    self.div2but        = {}
    self.faculty2but    = {}
    self.faculty2rowNum = {}

    self.buildGui()

  ##################### constructor ##################### 
  
  def buildGui(self):
    self.socDivisions = self.soc.getDivisions([])
  
    facultyFrame = Frame(self.tkRoot)
    facultyFrame.pack(side=LEFT, anchor=N)

    cb = partial(self.bodyCb, "faculty")
    h1 = Button(facultyFrame, text="faculty", command=cb,
                bg=self.colHdr1Bg, fg=self.colHdr1Fg, font=self.titleFont)
    h1.pack(side=TOP, expand=True, fill=X)

    self.bodyFrame = divisionsFrame = Frame(facultyFrame)
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
    self.bodyFramePacked = True
  
  ##################### highlightFaculty ##################### 

  def highlightFaculty(self, faculty): # accept either singular name, or list of names

    flist = faculty
    if isinstance(faculty, list) is False: flist = [faculty]  #convert to a list if not already

    self.socHighlightedFaculty = []
    for name in flist:
      if name in self.faculty2but:
        b = self.faculty2but[name]
        #b.itemconfig(bg=self.colHL1)
        b.configure(bg=self.colHL1)
        self.socHighlightedFaculty.append(name)
      else: print("socGUIFaculty.highlightFaculty: problem argument:", name)

  ##################### highlightFaculty ##################### 

  def clearHighlightedFaculty(self): 
    if self.socHighlightedFaculty == None or self.socHighlightedFaculty == []:
      return

    for faculty in self.socHighlightedFaculty:
      button = self.faculty2but[faculty]
      rowNum = self.faculty2rowNum[faculty]
      if rowNum % 2 == 0: rbg = self.colRowBg1 # row background
      else:               rbg = self.colRowBg2
      button.configure(bg=rbg)

  ##################### callbacks ##################### 

  def divisionCb(self, whichDivision):
    print("division %s was selected" % whichDivision)

  def facultyCb(self, whichFaculty):
    print("faculty %s was selected" % whichFaculty)

#####################################################################################
################ Clemson School of Computing GUI : researchAreas ####################
#####################################################################################

class socGuiResearchAreas(socGuiBase):
  socResearchAreas = None
  area2but         = None #major research areas to button
  field2but        = None #research fields      to button
  field2rowNum     = None #research field to row number
  socHighlightedFields = None

  ##################### constructor ##################### 

  def __init__(self, soc, tkRoot, facultyGui):
    super().__init__(soc, tkRoot) # call parent (socGuiBase) constructor

    self.area2but        = {}
    self.field2but    = {}
    self.field2rowNum = {}

    self.buildGui()
    self.facultyGui = facultyGui

    self.fontSize = 7
    self.bodyFont = (self.fontBase, str(self.fontSize))

  ##################### constructor ##################### 
  
  def buildGui(self):
    self.socResearchAreas = self.soc.getMajorResearchAreas([])
  
    rasFrame = Frame(self.tkRoot) #research areas frmae
    rasFrame.pack(side=LEFT, anchor=N)

    cb = partial(self.bodyCb, "areas")
    h1 = Button(rasFrame, text="research areas", command=cb,
                bg=self.colHdr1Bg, fg=self.colHdr1Fg, font=self.titleFont)
    h1.pack(side=TOP, expand=True, fill=X)

    self.bodyFrame = Frame(rasFrame)
    self.bodyFrame.pack(side=TOP, expand=True, fill=BOTH)

    for researchArea in self.socResearchAreas:
      raFrame  = Frame(self.bodyFrame); raFrame.pack(side=LEFT, anchor=N)

      cb = partial(self.raCb, researchArea)
      b  = Button(raFrame, text=researchArea, command=cb, width=self.colWidth, 
                  font=self.headerFont, bg = self.colHdr2Bg, fg = self.colHdr2Fg)

      b.pack(side=TOP); self.area2but[researchArea] = b
      ras = self.soc.getResearchFields(researchArea)
      print("RAs:", ras)
  
      rowNum = 1
      for ra in ras:
        cb = partial(self.raCb, ra)
        if rowNum % 2 == 0: rbg = self.colRowBg1 # row background
        else:               rbg = self.colRowBg2

        b  = Button(raFrame, text=ra, command=cb, font=self.bodyFont, bg=rbg, width=18)
        self.field2rowNum[ra] = rowNum
    
        b.pack(side=TOP, expand=True, fill=BOTH); self.field2but[ra] = b
        rowNum += 1
    self.bodyFramePacked = True
  
  ##################### highlightFaculty ##################### 

  def highlightFaculty(self, faculty): # accept either singular name, or list of names

    flist = faculty
    if isinstance(faculty, list) is False: flist = [faculty]  #convert to a list if not already

    self.socHighlightedFaculty = []
    for name in flist:
      if name in self.faculty2but:
        b = self.faculty2but[name]
        #b.itemconfig(bg=self.colHL1)
        b.configure(bg=self.colHL1)
        self.socHighlightedFaculty.append(name)
      else: print("socGUIFaculty.highlightFaculty: problem argument:", name)

  ##################### highlightFaculty ##################### 

  def clearHighlightedFaculty(self): 
    if self.socHighlightedFaculty == None or self.socHighlightedFaculty == []:
      return

    for faculty in self.socHighlightedFaculty:
      button = self.faculty2but[faculty]
      rowNum = self.faculty2rowNum[faculty]
      if rowNum % 2 == 0: rbg = self.colRowBg1 # row background
      else:               rbg = self.colRowBg2
      button.configure(bg=rbg)

  ##################### callbacks ##################### 

  def raCb(self, whichRa):
    print("research area %s was selected" % whichRa)
    print(self.soc.getFacultyResearchFields(whichRa))

### end ###
