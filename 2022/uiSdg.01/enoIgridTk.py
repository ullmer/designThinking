# Progressive examples toward simple Python interactivity
# Brygg Ullmer, Clemson University
# Begun 2022-10-13

# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
from functools import partial

################# tkinter interactive grid class #################

class enoIgridTk:

  numButtons      = 10 #how many UN SDGs
  numPerRow       = 4
  buttonWidth     = 10 #button width
  igridParent     = None
  igridFrame      = None
  useImageLabels  = False
  imageLabelDir   = None
  callbackFunc    = None
  imageMapNorm    = None
  imageMapDs      = None
  buttonMapIdx    = None
  lastIdxSelected = None

  ################# constructor #################

  def __init__(self, tkParent, **kwargs):
    self.callbackFunc = self.buttonCallback #default, overridable

    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not
 
    self.buildGui(tkParent)

  ################# button callback #################

  def buttonCallback(self, whichButton):
    print("Callback %i pressed" % whichButton)

    if self.useImageLabels and whichButton in self.imageMapDs:

      b1   = self.buttonMapIdx[whichButton]
      imgN = self.imageMapNorm[whichButton]
      b1.configure(image=imgN)
      self.dimUnselected(whichButton)

    self.lastIdxSelected = whichButton

  ################# dimUnselected #################

  def dimUnselected(self, selectedIdx):
    lis = self.lastIdxSelected
    if lis == None: return
    indices = self.buttonMapIdx.keys()
    for i in indices:
      if i == selectedIdx-1: continue
      b    = self.buttonMapIdx[i]
      imgD = self.imageMapDs[i]
      b.configure(image=imgD)

  ################# generate image filenames #################

  def genImageFn(self, idx):
    result = "%s/%02i.png" % (self.imageLabelDir, idx)
    return result 

  def genImageNormFn(self, idx):
    result = "%s/norm/%02i.png" % (self.imageLabelDir, idx)
    return result 

  def genImageDsFn(self, idx):
    result = "%s/ds/%02i.png" % (self.imageLabelDir, idx)
    return result 

  ################# build gui #################

  def buildGui(self, tkParent):
    self.igridParent = tkParent
    self.igridFrame  = tk.Frame(tkParent)
    self.igridFrame.pack(expand=1)

    rowFrame = tk.Frame(self.igridFrame) # invisible bundle of UI widgets
    rowFrame.pack(expand=1)
    colNum   = 1
    self.buttonMapIdx = {}

    if self.useImageLabels:
      self.imageMapNorm = {}
      self.imageMapDs   = {}

    for i in range(self.numButtons):
      cb = partial(self.callbackFunc, i+1)

      if self.useImageLabels:
        imgNFn = self.genImageNormFn(i+1); imgDFn = self.genImageDsFn(i+1)
        imgN  = tk.PhotoImage(file=imgNFn); self.imageMapNorm[i] = imgN
        imgD  = tk.PhotoImage(file=imgDFn); self.imageMapDs[i]   = imgD
        b1    = tk.Button(rowFrame, image=imgN, command=cb)
      else:
        buttonLabel = "B%i" % (i+1)
        b1 = tk.Button(rowFrame, text=buttonLabel, command=cb, width=self.buttonWidth)

      self.buttonMapIdx[i] = b1

      b1.pack(side=tk.LEFT)
      colNum += 1

      if colNum  > self.numPerRow:
        rowFrame = tk.Frame(self.igridFrame); 
        rowFrame.pack(expand=1, side=tk.TOP)
        colNum = 1

      rowFrame.pack()

### end ###
