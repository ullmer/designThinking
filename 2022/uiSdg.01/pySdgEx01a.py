# Progressive examples toward simple Python interactivity
# Brygg Ullmer, Clemson University
# Begun 2022-10-13

import tkinter as tk

top = tk.Tk()

def buttonCallBack():
   print("button pressed")

b1 = tk.Button(top, text="test", command=buttonCallBack)

b1.pack()
top.mainloop()

### end ###
