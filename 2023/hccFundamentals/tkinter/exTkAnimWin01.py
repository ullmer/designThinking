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

####### support functions ####### 

def quitCb(): sys.exit(-1)

def genWinGeom(winDim, winCoord): 
  result = "%s+%i+%i" % (winDim, winCoord[0], winCoord[1])
  return result

####### main ####### 

b1 = tk.Button(root, text='quit', command=quitCb)
b1.pack()

w1Geom = genWinGeom(winDim, win1Coord)
w2Geom = genWinGeom(winDim, win2Coord)

w1 = tk.Toplevel(); w1.geometry(w1Geom)
w2 = tk.Toplevel(); w2.geometry(w2Geom)

root.mainloop()

### end ###
