# Progressive examples toward simple Python interactivity
# Brygg Ullmer, Clemson University
# Begun 2022-10-13

# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
from functools import partial

top = tk.Tk()

def buttonCallback(whichSDG):
   print("Callback %i pressed" % whichSDG)

numSdgs   = 17 #how many UN SDGs
numPerRow = 4
bw        = 10 #button width
colNum    = 1

rowFrame = tk.Frame(top) # invisible bundle of UI widgets
rowFrame.pack(expand=1)

for i in range(numSdgs):
  buttonLabel = "SDG %i" % (i+1)

  cb = partial(buttonCallback, i)
  b1 = tk.Button(rowFrame, text=buttonLabel, command=cb, width=bw)
  b1.pack(side=tk.LEFT)
  colNum += 1

  if colNum  > numPerRow:
    rowFrame = tk.Frame(top); 
    rowFrame.pack(expand=1, side=tk.TOP)
    colNum = 1

rowFrame.pack()
top.mainloop()

### end ###
