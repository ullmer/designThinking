# Progressive examples toward simple Python interactivity
# Brygg Ullmer, Clemson University
# Begun 2022-10-13

import tkinter as tk

top = tk.Tk()

def buttonCallBack():
   print("button pressed")

numSdgs   = 17 #how many UN SDGs

for i in range(numSdgs):
  buttonLabel = "SDG %i" % i
  b1         = tk.Button(top, text=buttonLabel, command=buttonCallBack)
  b1.pack()

top.mainloop()

### end ###
