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

row = 1
for lpRow in lpRows:
  word1    = lpRow[0]
  wordRest = ' '.join(lpRow[1:]) # a bit inefficient computationally, but...
  word1Len = len(word1)
  coord1 = "%i.0"  % (row)
  coord2 = "%i.%i" % (row, word1Len+1)

  t.insert(coord1, word1)
  t.insert(coord2, wordRest)

  t.tag_add("bold", coord1, coord2)
  t.tag_add("norm", coord2, END)

  row += 1

root.mainloop() 

### end ###
