# In-class example in HCC Fundamentals
# Brygg Ullmer, Clemson University
# Begun 2024-09-12

from tkinter             import *
from tkinter.font        import *
from functools           import partial
from hccStudentThemesTki import *
from enoButtonArrayTki   import *

root = Tk() 
cw   = 25 #column width

root.title("HCC student themes navigator")

try:    headerFont = Font(family="Calibri", size=15, weight=BOLD)
except: headerFont = ('Sans','15','bold') #fallback if Calibri not installed

try:    bodyFont = Font(family="Calibri", size=13)
except: bodyFont = ('Sans','13') 

st          = studentThemesTki()
categories  = st.getCategories()

############# main ############# 

bhm = buttonHighlightMgr()

for category in categories:
  f    = Frame(root, bg='#112'); f.pack(side=LEFT, anchor="n", expand=True, fill=BOTH)
  b    = Button(f, text=category, font=headerFont, bg='#000', fg='#eee')
  b.pack(fill=X)

  subthemes = st.getCatEntries(category)
  for subtheme in subthemes:
    cb1 = partial(st.displayStudentTheme, subtheme) #callback to display associated information
    cb2 = partial(bhm.triggerHighlightButton, subtheme)

    b2 = Button(f, text=subtheme, width=cw, anchor="w", font=bodyFont, command=cb2, bg='#444', fg='#ccc') 
    bhm.registerButtonHandleCb(subtheme, b2, cb1)
    b2.pack(side=TOP)

def bindAllWidgets(widget, keybind, cb):
  widget.bind(keybind, cb)
  for child in widget.winfo_children(): bindAllWidgets(child, keybind, cb)

bindAllWidgets(root, '<Right>', bhm.cycleNextButton) 

studentKeys      = st.getStudentKeys()
firstStudent     = studentKeys[0]
studentViewFrame = st.buildStudentThemeView(root, firstStudent)
studentViewFrame.pack(expand=True, fill=BOTH)

root.mainloop()                                          

### end ###
