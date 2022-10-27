# Progressive examples toward simple Python interactivity
# Brygg Ullmer, Clemson University
# Begun 2022-10-13

# https://docs.python.org/3/library/tkinter.html
# https://www.geeksforgeeks.org/python-tkinter-scale-widget/

import tkinter as tk
from enoIgridTk import *

top  = tk.Tk()
tkig = enoIgridTk(top, numButtons=17, imageLabelDir="sdg", useImageLabels=True)

sdgIdx = Int()

def sdgSliderCb(event):
  global tkig, sdgIdx
  tkig.buttonCallback(sdgIdx)

slider = tk.Scale(top, var=sdgIdx, from=1, to=18, command=sdgSliderCb)
slider.pack()

top.mainloop()

### end ###
