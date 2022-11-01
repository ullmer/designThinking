# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

import tkinter as tk
from enoDomHomelessness import *

class enoUiHomelessnessTk:

  edh       = None  #enoDomHomelessness
  tkParent  = None  #tk parent
  tkFrame   = None
  tkButtons = None 

  yamlD        = None
  imagePath    = None
  yOffset      = None #placeholder assignments until read in or assigned
  xOffset      = None
  categories   = None
  descriptions = None

  ####################### constructor #######################

  def __init__(self, tkParent):
    self.edh = enoDomHomelessness()
    self.buildUI(tkParent)

  ####################### build UI #######################

  def buildUI(self, tkParent):
    self.tkParent  = tkParent 
    self.tkFrame   = tk.Frame(tkParent); self.tkFrame.pack()
    self.tkButtons = {}
    
    categories = self.edh.getCategories()
    for category in categories:
      imgFn1 = self.edh.getImageFn(category)
      imgFn2 = "images/%s.png" % imgFn1
      b = tk.Button(self.tkFrame, image=imgFn2)
      b.pack()

####################### main #######################
if __name__ == '__main__':
  top = tk.Tk()
  enoUiH = enoUiHomelessnessTk(top)
  top.mainloop()

### end ###
