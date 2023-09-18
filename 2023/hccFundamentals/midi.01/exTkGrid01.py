# Example of Tkinter grid of buttons
# Brygg Ullmer, Clemson University
# Begun 2023-09-18

# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.tutorialspoint.com/python/tk_button.htm

import tkinter as tk

rows, columns = 8, 8
w, h = 93, 93

mf = mainFrame = tk.Tk()
mf.title("Interactive grid example")
mf.geometry("800x800")

im = tk.PhotoImage(width=1, height=1) # hack introduced here:
# https://www.reddit.com/r/learnpython/comments/th4c6g/how_do_i_make_the_buttons_be_square_in_tkinter/

for i in range(rows):
  for j in range(columns):
    str = "%ix%i" % (i, j)
    button = tk.Button(mf, text=str, image=im, width=w, height=h) #see reddit link for image & dimensions
    button.grid(row=i, column=j)

mf.mainloop()

### end ###

