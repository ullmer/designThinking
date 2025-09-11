# Example of Tkinter grid of buttons
# Brygg Ullmer, Clemson University
# Begun 2023-09-18

# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.tutorialspoint.com/python/tk_button.htm

import tkinter as tk           #Tkinter graphical interface
import PIL.Image, PIL.ImageTk #image manipulation package

rows, columns = 8, 8
w, h          = 93, 93
color1        = (200, 100, 0)
color2        = (200, 100, 0)

mf = mainFrame = tk.Tk()
mf.title("Interactive grid example")
mf.geometry("800x800")

imPil = PIL.Image.new(mode="RGB", size=(w,h), color=color1)
imPTk = PIL.ImageTk.PhotoImage(imPil)
#imPTk = PIL.ImageTk.PhotoImage(file="im_or.png")

for i in range(rows):
  for j in range(columns):
    button = tk.Button(mf, image=imPTk) 
    button.grid(row=i, column=j)

mf.mainloop()

### end ###

