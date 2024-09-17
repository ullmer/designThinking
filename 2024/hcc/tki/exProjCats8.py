# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter             import *
from tkinter.font        import *
from hccStudentThemesTki import *
from functools           import partial

root = Tk() 
cw   = 25 #column width

root.title("HCC student themes navigator")

try:    headerFont = Font(family="Calibri", size=15, weight=BOLD)
except: headerFont = ('Sans','15','bold') #fallback if Calibri not installed

try:    bodyFont = Font(family="Calibri", size=13)
except: bodyFont = ('Sans','13') 

st          = studentThemesTki()
categories  = st.getCategories()

############# simple button highlight manager ############# 

class buttonHighlightMgr: 
  handle2Button = {}
  bg1, bg2 = '#444', '#ccc'
  def registerButtonHandle(self, handleStr, button): self.handle2Button[handleStr] = button

############# main ############# 

for category in categories:
  f    = Frame(root, bg='#112'); f.pack(side=LEFT, anchor="n", expand=True, fill=BOTH)
  b    = Button(f, text=category, font=headerFont, bg='#000', fg='#eee')
  b.pack(fill=X)

  subthemes = st.getCatEntries(category)
  for subtheme in subthemes:
    cb = partial(st.displayStudentTheme, subtheme) #callback to display associated information
    b2 = Button(f, text=subtheme, width=cw, anchor="w", font=bodyFont, command=cb, bg='#444', fg='#ccc') 
    b2.pack(side=TOP)

studentKeys      = st.getStudentKeys()
firstStudent     = studentKeys[0]
studentViewFrame = st.buildStudentThemeView(root, firstStudent)
studentViewFrame.pack(expand=True, fill=BOTH)

root.mainloop()                                          

### end ###
