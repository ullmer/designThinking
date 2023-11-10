# Example code relating to interactive storyboarding
# By Brygg Ullmer, Clemson University
# Begun 2023-11-09

from tkinter import *
import PIL.Image, PIL.ImageTk #image manipulation package

#WIDTH=1024

class globalState:
  imP1   = imP2  = None #image handles, so auto-garbage collection doesn't destroy
  imTk1  = imTk2 = None #image handles, 
  canvas = None
  img1   = None

gs = globalState()

screenStates = ['unsdg2', 'unsdg4']
imgAddUser   = 'person-add-iconic1'

#actorNames          = {a1: "John", a2: "Jane", s1: "screen", b1: "addUser"}
actorOriginalPos     = {}
selectedActor        = None
selectedActorName    = None
selectedActorOrigPos = None

def helloCB():
  print("hello was pushed")

####################### build UI ######################

imP1 = imTk1 = None
imP2 = imTk2 = None

#https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
#translates rgb values of type int to a tkinter friendly color code
def rgb2tk(r, g, b):
  return "#%02x%02x%02x" % (r,g,b)

c                    = None #canvas handle, sigh; should be moved into a class
selectedCanvasObject = None #ID (1,2,3...) of a selected object within canvas c
lastDragXY           = None #coordinates of where a mouse-drag sequence began
img1                 = None

####################### build user interface ######################

def buildUI(f1Screens, f2Spatial, f3Controls):

  imgAddUserFn   = 'person-add-iconic1.png'
  imP1  = PIL.Image.open(imgAddUserFn)
  imTk1 = PIL.ImageTk.PhotoImage(imP1)

  #b = Button(f3Controls, text="add actor", command=helloCB) # Create a label with words
  b  = Button(f3Controls, image=imTk1, command=addCanvasItem)
  b.pack(side=LEFT, expand=True, fill=BOTH) 

  screenFilenames = ['unsdg2.png', 'unsdg4.png']
  imP2   = PIL.Image.open(screenFilenames[0])
  imTk2  = PIL.ImageTk.PhotoImage(imP2)
  label1 = Label(f1Screens, image=imTk2)
  label1.pack()

  bgColor = rgb2tk(10, 10, 10)
  #c = Canvas(f2Spatial, bg="orange", height=200, width=1024)
  c = Canvas(f2Spatial,  bg=bgColor,  height=400, width=1024)
  c.pack()

  img1Fn = 'clemson12d2.png'
  img1   = PhotoImage(file=img1Fn) #transparent image
  c.create_image(100, 100, image=img1,anchor='ne') 

  r1Coords = (10, 10, 60, 60)
  r1 = c.create_rectangle(r1Coords, fill="white")

  r2Coords = (70, 10, 120, 60)
  r2 = c.create_rectangle(r2Coords, fill="orange")

  #print("canvas rectangle ids:", r1, r2)
  #c.move(r1, 50, 50)

  c.bind("<Button-1>",  on_click)
  c.bind("<B1-Motion>", on_drag)

################### mouse click callback ##################

#next pulls from https://stackoverflow.com/questions/65189412/python-canvas-move-items-with-mouse-tkinter

def on_click(event):
  global c, selectedCanvasObj, lastDragXY

  x, y = event.x, event.y
  csr  = 10 #click search radius
  x1, y1, x2, y2 = x-csr, y-csr, x+csr, y+csr
  #print("click event:", event)

  selected = c.find_overlapping(x1, y1, x2, y2)
  if selected: selectedCanvasObj = selected[-1]
  else:        selectedCanvasObj = None

  lastDragXY = (x,y) #for calculating dx, dy movement changes with drag

  #print("selected:", selectedCanvasObj)

################### mouse drag callback ##################

def on_drag(gs, event):
  #print("drag event:", event)

  x0, y0 = gs.lastDragXY
  x1, y1 = event.x, event.y
  dx, dy = x1-x0, y1-y0
  gs.lastDragXY = (x1,y1) 

  gs.canvas.move(gs.selectedCanvasObj, dx, dy)
  print(">>",    gs.selectedCanvasObj, x1, y1)
  
################### add Canvas Item ##################

def addCanvasItem(gs):
  rCoords = (100, 100, 150, 150)
  r = gs.canvas.create_rectangle(rCoords, fill="purple")

####################### main ######################

root = Tk() # Create the root (base) window

f1Screens  = Frame(root)
f2Spatial  = Frame(root)
f3Controls = Frame(root)
buildUI(f1Screens, f2Spatial, f3Controls)

for frame in [f1Screens, f2Spatial, f3Controls]: 
  frame.pack(side=TOP, expand=True, fill=BOTH)

root.mainloop() # Start the event loop

### end ###
