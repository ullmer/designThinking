# https://en.wikipedia.org/wiki/Tkinter

from tkinter import *

def helloCB():
  print("hello was pushed")

root = Tk()                                                # Create the root (base) window 
b    = Button(root, text="Hello, world!", command=helloCB) # Create a label with words
b.pack()                                                   # Put the label into the window
root.mainloop()                                            # Start the event loop

### end ###
