# Example code relating to interactive storyboarding
# By Brygg Ullmer, Clemson University
# Begun 2023-11-08

from tkinter import *
import PIL.Image, PIL.ImageTk #image manipulation package

#WIDTH=1024

screenStates = ['unsdg2', 'unsdg4']
imgAddUser   = 'person-add-iconic1'

#actorNames          = {a1: "John", a2: "Jane", s1: "screen", b1: "addUser"}
actorOriginalPos     = {}
selectedActor        = None
selectedActorName    = None
selectedActorOrigPos = None

def helloCB():
  print("hello was pushed")

#screen.draw.circle((800, 500), 50, defaultEllipseColor)
#
####################### on mouse down/press ######################
#
#def addUser():
#  newActor = Actor('red-hl-1in-200dpi',  pos=(200, 200))
#  moveableActors.append(newActor)
#  actorNames[newActor] = 'new actor'
#
####################### on mouse down/press ######################
#
#def on_mouse_down(pos):
#  global selectedActor, selectedActorName, selectedActorOrigPos, stableActors
#  for actor in (stableActors + moveableActors):
#    if actor.collidepoint(pos): 
#      name = actorNames[actor]
#      print("\nactor selected:", name)
#
#      if name == "screen": 
#        print("update the virtual screen images")
#        stableActors = [s2, b1]
#
#      elif name == "addUser":
#        addUser()
#
#      else:
#        actorOriginalPos[actor] = pos     
#        selectedActor           = actor
#        selectedActorName       = name
#        selectedActorOrigPos    = selectedActor.pos
#
#  print("=" * 25)
#
#def on_mouse_move()
#
####################### on mouse up ######################
#
#def on_mouse_up():
#  global selectedActor, selectedActorName, selectedActorOrigPos
#  selectedActor = selectedActorName = selectedActorOrigPos = None
#
####################### on key down ######################
#
#numTimesSpaceHit = 0
#
#def on_key_down(key):
#  global numTimesSpaceHit
#
#  if key == keys.SPACE:  # keys.RIGHT, keys.H, keys.C, etc.
#    print("space pressed")
#
#    #match numTimesSpaceHit:
#    #  case 0:
#
#    if numTimesSpaceHit == 0:
#      animate(a1, pos=(400, 500), tween='accel_decel', duration=.75)
#    else:
#      animate(a2, pos=(500, 500), tween='accel_decel', duration=.75)
#
#    numTimesSpaceHit += 1
#
####################### build UI ######################

imP1 = imTk1 = None
imP2 = imTk2 = None

#https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
#translates rgb values of type int to a tkinter friendly color code
def rgb2tk(r, g, b):
  return "#%02x%02x%02x" % (r,g,b)

c                    = None #canvas handle, sigh; should be moved into a class
selectedCanvasObject = None #ID (1,2,3...) of a selected object within canvas c
lastDragXY          = None #coordinates of where a mouse-drag sequence began

####################### build user interface ######################

def buildUI(f1Screens, f2Spatial, f3Controls):
  global imP1, imTk1, imP2, imTk2, c

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

def on_drag(event):
  global c, selectedCanvasObj, lastDragXY
  #print("drag event:", event)

  x0, y0 = lastDragXY
  x1, y1 = event.x, event.y
  dx, dy = x1-x0, y1-y0
  lastDragXY = (x1,y1) 

  c.move(selectedCanvasObj, dx, dy)
  
################### add Canvas Item ##################

def addCanvasItem():
  global c
  rCoords = (100, 100, 150, 150)
  r = c.create_rectangle(rCoords, fill="purple")

####################### main ######################

root = Tk() # Create the root (base) window

f1Screens  = Frame(root)
f2Spatial  = Frame(root)
f3Controls = Frame(root)
buildUI(f1Screens, f2Spatial, f3Controls)

for frame in [f1Screens, f2Spatial, f3Controls]: 
  frame.pack(side=TOP, expand=True, fill=BOTH)

root.mainloop()                                            # Start the event loop

### end ###
