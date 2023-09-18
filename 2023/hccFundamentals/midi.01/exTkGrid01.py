# Example of Tkinter grid of buttons
# Brygg Ullmer, Clemson University
# Begun 2023-09-18

import tkinter as tk

rows, columns = 8, 8

mf = mainFrame = tk.Tk()
mf.title("Interactive grid example")
mf.geometry("800x600")

for i in seq(rows):
  for j in seq(columns):
    str = "%ix%i" % (i, j)
    button = tk.Button(mf, text=str)
    button.grid(row=i, column=j)

mf.mainloop()

### end ###

