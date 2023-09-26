# Example of Tkinter grid of buttons
# Brygg Ullmer, Clemson University
# Begun 2023-09-18

# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/python/tk_grid.htm
# https://www.tutorialspoint.com/python/tk_button.htm

import tkinter as tk           #Tkinter graphical interface
import PIL.Image, PIL.ImageTk #image manipulation package
from functools    import partial

rows, columns = 8, 9
w, h          = 94, 94
#w, h          = 113, 113
color1        = (200, 100,   0)
color2        = (200,   0, 200)

root = tk.Tk()
root.title("Interactive grid example")
#root.geometry("800x800")
root.geometry("900x800-0-0")
root.overrideredirect(1) #hide window decorations ~= titlebar
#root.geometry("+200+400")

buttonState = {}
buttonTk    = {}

imP1  = PIL.Image.new(mode="RGB", size=(w,h), color=color1)
imTk1 = PIL.ImageTk.PhotoImage(imP1)

imP2  = PIL.Image.new(mode="RGB", size=(w,h), color=color2)
imTk2 = PIL.ImageTk.PhotoImage(imP2)
    
############### loadImage ############### 

def loadImage(baseFn, x, y, ext='.png'):
  rowId  = chr(ord('A') + x)
  fn     = "%s-%s%i%s" % (baseFn, rowId, y, ext)
  img    = PIL.Image.open(fn)
  result = PIL.ImageTk.PhotoImage(img)
  return result

############### button toggle callback ############### 

def toggleCB(coord):
  global buttonState, buttonCb, imTk1, imTk2

  if buttonState[coord]: 
    buttonState[coord] = False
    buttonTk[coord].configure(image=imTk1)
  else:
    buttonState[coord] = True
    buttonTk[coord].configure(image=imTk2)

############### create widgets ############### 

# images need to be held an a data structure, or else they will be garbage collected
imagesDict = {}
    
imPrefix = "images/cc77g/125/cc77g"
px = py = 15

#background image, per https://stackoverflow.com/questions/62430477/how-to-set-a-background-image-in-tkinter-using-grid-only
bgimg = PIL.Image.open("images/clemson-colleges-77g2-core125.png")
bgi   = PIL.ImageTk.PhotoImage(bgimg)
bgl   = tk.Label(root, image=bgi)
bgl.place(x=0, y=0, relwidth=1, relheight=1)

for i in range(rows):
  for j in range(columns):
    coord  = (i, j)
    cb     = partial(toggleCB, coord) #e.g., https://www.blog.pythonlibrary.org/2016/02/11/python-partials/
    im = imagesDict[coord] = loadImage(imPrefix, i, j)
    
    button = tk.Button(root, image=im, command=cb) 

    buttonState[coord] = False
    buttonTk[coord]    = button
    button.grid(row=i, column=j, padx=px, pady=py)


root.mainloop()

### end ###

