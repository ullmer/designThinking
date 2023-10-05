# Exploration with PyGame Zero-animated tkinter windows.
# By Brygg Ullmer, Clemson University
# Begun 2023-10-05

from   functools import partial
import tkinter as tk
import sys

winDim    = '400x400'


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

####### construct window animation state ####### 

def constructWindowAnimators():
  global winState, winActors, winCoords, winCoordBase, winShift 

  winState  = {}
  winActors = {} #using PyGame Zero Actor animation mechanism to tween-animate Tkinter windows
  winCoords    = {}
  winCoordBase = {}

  winCoordBase["w1"] = (0,   0)
  winCoordBase["w2"] = (800, 0)
  winShift           = 200

  for winId in ["w1", "w2"]:
    winState[winId] = 1
    winCoord[winId] = winCoordBase[winId]

####### construct window animation state ####### 

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
