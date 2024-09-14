# Tkinter Text widget tagging experiment
# Brygg Ullmer, Clemson University
# Begun 2024-09-14

from tkinter import *
import lorem

#https://pypi.org/project/lorem/

lp      = lorem.paragraph()
lpWords = lp.split()
lpRows  = []

blockSize = 5
idx       = 0

for i in range(blockSize): #blockSize lines of blockSize words
  lpRow = []
  for j in range(blockSize):
    lpRow.append(lpWords[idx])
    idx += 1
  lpRows.append(lpRow)
  lpRow = []

root = Tk()              

t = Text(root, width=400) 
t.pack(expand=True, fill=BOTH)    

t.tag_configure('bold', font=('Calibri', 13, 'bold'))
t.tag_configure('norm', font=('Calibri', 11))

for lpRow in lpRows:
  word1    = lpRow[0]
  wordRest = ' '.join(lpRow[1:]) # a bit inefficient computationally, but...

.insert("1.0",   "name: ")
.insert(END,   name + "\n")

.insert(END,   "theme: ")
.insert(END,  theme)

.tag_add("norm", "1.6", "2.0") 
.tag_add("norm", "2.7", END)
.tag_add("bold", "1.0", "1.5")
.tag_add("bold", "2.0", "2.6")

root.mainloop() 

### end ###
