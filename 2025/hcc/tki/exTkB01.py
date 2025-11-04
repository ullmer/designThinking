# Example of Tkinter grid of buttons
# Brygg Ullmer, Clemson University
# Begun 2023-09-18

# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.tutorialspoint.com/python/tk_button.htm

import tkinter as tk  #Tkinter graphical interface
import PIL.Image, PIL.ImageTk      #image manipulation package

rows, columns = 8, 8
w, h          = 93, 93
color1        = (200, 100, 0)

mf = mainFrame = tk.Tk()
mf.title("Interactive grid example")
mf.geometry("800x800")

imPTk = PIL.ImageTk.PhotoImage(file="images/im_or2.png")
button = tk.Button(mf, image=imPTk) #see reddit link for image & dimensions
button.pack()

mf.mainloop()

### end ###

