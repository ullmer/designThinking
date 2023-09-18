# Example of Tkinter grid of buttons
# Brygg Ullmer, Clemson University
# Begun 2023-09-18

# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.tutorialspoint.com/python/tk_button.htm

import tkinter as tk           #Tkinter graphical interface
import PIL.Image, PIL.ImageTk #image manipulation package
from functools    import partial

rows, columns = 8, 8
w, h          = 93, 93
color1        = (200, 100,   0)
color2        = (200,   0, 200)

mf = mainFrame = tk.Tk()
mf.title("Interactive grid example")
mf.geometry("800x800")

buttonState = {}

def toggleCB(x, y):
 
 

imP1  = PIL.Image.new(mode="RGB", size=(w,h), color=color1)
imTk1 = PIL.ImageTk.PhotoImage(imP1)

imP2  = PIL.Image.new(mode="RGB", size=(w,h), color=color2)
imTk2 = PIL.ImageTk.PhotoImage(imP2)

for i in range(rows):
  for j in range(columns):
    cb = partial(toggleCB, i, j)
    button = tk.Button(mf, image=imPTk, callback=cb) 
    button.grid(row=i, column=j)

mf.mainloop()

### end ###

