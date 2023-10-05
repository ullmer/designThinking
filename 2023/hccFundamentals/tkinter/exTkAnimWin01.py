# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

import tkinter as tk
import sys

winDim    = '400x400'
win1Coord = (0, 0)
win2Coord = (800, 0)

winController = '300x50-0-0'

root = tk.Tk()
root.title('example controller')
root.geometry(winController)

def quitCb(): sys.exit(-1)

b1 = tk.Button(root, text='quit')
b1.pack

root.mainloop()

### end ###
