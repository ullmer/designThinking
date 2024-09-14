from tkinter import *
root = Tk()              
t = Text(root, width=400) 
t.pack(expand=True, fill=BOTH)    

t.tag_configure('bold', font=('Calibri', 13, 'bold'))
t.tag_configure('norm', font=('Calibri', 11))

for i in range(20):

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
