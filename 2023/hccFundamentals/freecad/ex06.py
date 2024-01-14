# First validation of Python port of 1995 3wish code
# Brygg Ullmer, Clemson University
# Original code begun fall 1995; here, 2023-10-20

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin
import sys

sys.path.append('c:/git/tangibles/sw/3wish.02')
from w3core  import *
from w3shift import *

view, doc, sg, root = genViewDocSgRoot()


#Heider & Simmel 1944 variant; https://www.youtube.com/watch?v=VTNmLt7QX8E
stage  = doc.addObject("Part::Plane", "floor")  #https://wiki.freecad.org/Part_Plane
wedge1 = doc.addObject("Part::Wedge", "wedge1") #https://wiki.freecad.org/Part_Wedge#Scripting
wedge2 = doc.addObject("Part::Wedge", "wedge2") #https://wiki.freecad.org/Part_Wedge#Scripting
bldg1a = doc.addObject("Part::Box",   "bldg1a")
bldg1b = doc.addObject("Part::Box",   "bldg1b")

stage.Length     = stage.Width  = 100.
bldg1a.Length    = bldg1a.Width =  50.; bldg1a.Height = 8.
bldg1b.Length    = bldg1b.Width =  46.; bldg1b.Height = 8.
wedge1.Placement = App.Placement(App.Vector( 0, 0, 0), App.Rotation( 0, 0, 0))
wedge2.Placement = App.Placement(App.Vector(20, 0, 0), App.Rotation(90, 0, 0))
bldg1a.Placement = App.Placement(App.Vector( 0, 0, 0), App.Rotation( 0, 0, 0))
bldg1b.Placement = App.Placement(App.Vector( 2, 2, 1), App.Rotation( 0, 0, 0))

bldgCut1   = App.activeDocument().addObject("Part::Cut", "Bldg central void")
bldgCut1.Base = bldg1a
bldgCut1.Tool = bldg1b

doc.recompute()

Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

### end ###
