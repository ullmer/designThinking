# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

from   functools import partial
import tkinter as tk
import sys

winDim    = '400x400'
win1CoordBase = (0, 0)
win2CoordBase = (800, 0)
winShift      = 200

win1Coord = win1CoordBase
win2Coord = win2CoordBase

winController = '300x50-0-0'

root = tk.Tk()
root.title('example controller')
root.geometry(winController)

####### support functions ####### 

def quitCb(): 
  print("contemplating quitting")
  sys.exit(-1)

def genWinGeom(winDim, winCoord): 
  result = "%s+%i+%i" % (winDim, winCoord[0], winCoord[1])
  return result

winState  = {}
winActors = {} #using PyGame Zero Actor animation mechanism to tween-animate Tkinter windows

winState["w1"] = 1
winState["w2"] = 1

def winShift(whichWin):

####### main ####### 

w1b = tk.Button(root, text="w1 shift", command=partial(winShift, "w1"))
w2b = tk.Button(root, text="w2 shift", command=partial(winShift, "w2"))

b1 = tk.Button(root, text='quit', command=quitCb)
b1.pack()

w1Geom = genWinGeom(winDim, win1Coord)
w2Geom = genWinGeom(winDim, win2Coord)

w1 = tk.Toplevel(); w1.geometry(w1Geom)
w2 = tk.Toplevel(); w2.geometry(w2Geom)

def update(): 
  root.update() #keeps TkInter alive

#root.mainloop()

### end ###
