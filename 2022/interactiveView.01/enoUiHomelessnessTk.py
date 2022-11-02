# Brygg Ullmer, Clemson University
# Begun 2022-11-01
# Content engaging https://github.com/DataKind-DC/homelessness-service-navigator

import tkinter as tk
from PIL import Image, ImageTk
from enoDomHomelessness import *

class enoUiHomelessnessTk:

  edh          = None  #enoDomHomelessness
  tkParent     = None  #tk parent
  tkFrame      = None
  tkButtons    = None 

  imageHandles = None

  ####################### constructor #######################

  def __init__(self, tkParent):
    self.edh = enoDomHomelessness()
    self.buildUI(tkParent)

  ####################### build UI #######################

  def buildUI(self, tkParent):
    self.tkParent  = tkParent 
    self.tkFrame   = tk.Frame(tkParent)
    self.tkButtons = {}; self.imageHandles = {}
    
    categories = self.edh.getCategories()
    for category in categories:
      imgFn1 = self.edh.getImageFn(category)
      imgFn2 = "images/%s.png" % imgFn1
      img    = ImageTk.PhotoImage(file=imgFn2)
      self.imageHandles[category] = img #amazing; this line necessary, per atlasologist reference here
      # https://stackoverflow.com/questions/22200003/tkinter-button-not-showing-image

      b = tk.Button(self.tkFrame, image=img)
      b.pack()
    self.tkFrame.pack()

####################### main #######################
if __name__ == '__main__':
  top = tk.Tk()
  enoUiH = enoUiHomelessnessTk(top)
  top.mainloop()

### end ###
