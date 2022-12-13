# Progressive examples toward simple Python interactivity
# Brygg Ullmer, Clemson University
# Begun 2022-10-13

# https://docs.python.org/3/library/tkinter.html

import tkinter as tk

top = tk.Tk()

def buttonCallBack():
   print("button pressed")

numSdgs   = 17 #how many UN SDGs
numPerRow = 4
bw        = 10 #button width
colNum    = 1

rowFrame = tk.Frame(top) # invisible bundle of UI widgets
rowFrame.pack(expand=1)

for i in range(numSdgs):
  buttonLabel = "SDG %i" % (i+1)
  b1          = tk.Button(rowFrame, text=buttonLabel, command=buttonCallBack, width=bw)
  b1.pack(side=tk.LEFT)
  colNum += 1

  if colNum  > numPerRow:
    rowFrame = tk.Frame(top); 
    rowFrame.pack(expand=1, side=tk.TOP)
    colNum = 1

rowFrame.pack()
top.mainloop()

### end ###
