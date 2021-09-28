### ttk (toward antialiased text, etc.) ###

#https://stackoverflow.com/questions/61714097/tk-call-tkinter-tclerror-unknown-option-bg

from tkinter     import *
import tkinter as tk
from tkinter import ttk
from ttkthemes 

root = ThemedTk()

style = Style()
style.configure("BW.TLabel", background="white")
l1 = Label(text="Test", style="BW.TLabel")

root.mainloop()

### end ###
