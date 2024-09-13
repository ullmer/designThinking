# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter             import *
from tkinter.font        import *
from hccStudentThemesTki import *
from functools           import partial

def helloCB():
  print("hello was pushed")

root = Tk() 
root.title("HCC student themes navigator")
cw   = 25 #column width

try:    headerFont = Font(family="Calibri", size=15, weight=BOLD)
except: headerFont = ('Sans','15','bold') #fallback if Calibri not installed

try:    bodyFont = Font(family="Calibri", size=13)
except: bodyFont = ('Sans','13') 

#bodyFont = Font(family="Oswald", size=12, slant=ROMAN)

st          = studentThemesTki()
categories  = st.getCategories()

for category in categories:
  f    = Frame(root); f.pack(side=LEFT, anchor="n") #anchor to the north
  b    = Button(f, text=category, command=helloCB, font=headerFont, bg='#aaa')
  b.pack(expand=True, fill=BOTH)

  subthemes = st.getCatEntries(category)
  for subtheme in subthemes:
    cb = partial(st.displayStudentTheme, subtheme) #callback to display associated information
    b2 = Button(f, text=subtheme, width=cw, anchor="w", font=bodyFont, command=cb) #anchor to the west means left-aligned
    b2.pack(side=TOP)

studentKeys      = st.getStudentKeys()
firstStudent     = studentKeys[0]
studentViewFrame = st.buildStudentThemeView(root, firstStudent)
studentViewFrame.pack(expand=True, fill=BOTH)

root.mainloop()                                          


### end ###
