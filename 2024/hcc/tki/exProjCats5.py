# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter             import *
from hccStudentThemesTki import *

def helloCB():
  print("hello was pushed")

root = Tk() 
cw   = 25 #column width
headerFont = ('Sans','12','bold')
bodyFont   = ('Sans','12')

st          = studentThemesTki()
categories  = st.getCategories()
spacerLabel = Label(root, width=5)

for category in categories:
  f    = Frame(root); f.pack(side=LEFT, anchor="n") #anchor to the north
  b    = Button(f, text=category, command=helloCB, font=headerFont, bg='#aaa')
  b.pack(expand=True, fill=BOTH)

  subthemes = st.getCatEntries(category)
  for subtheme in subthemes:
    b2 = Button(f, text=subtheme, width=cw, anchor="w", font=bodyFont) #anchor to the west means left-aligned
    b2.pack(side=TOP)

spacerLabel.pack()

studentKeys      = st.getStudentKeys()
firstStudent     = studentKeys[0]
studentViewFrame = st.buildStudentThemeView(root, firstStudent)
studentViewFrame.pack(expand=True, fill=BOTH)

root.mainloop()                                          


### end ###
