# First validation of Python port of 1995 3wish code
# Brygg Ullmer, Clemson University
# Original code begun fall 1995; here, 2023-10-20

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin

##################### add object #####################

def addObj(parent, obj):
   try:
     #input = coin.SoInput()
     #input.setBuffer(ivObj)        #https://www.coin3d.org/Coin/html/classSoInput.html
     #newNode = sdb.readAll(input)  #https://www.coin3d.org/Coin/html/classSoDB.html
     #parent.addChild(newNode)
     #Swig hadn't yet had a release when above original was written, and given Tcl dynamics, 
     #   had made different choices at the time https://www.swig.org/history.html

     parent.addChild(obj)           #uninteresting, for simplest version
   except:
     print("addObj exception:"); traceback.print_exc()
     return False

   return True

##################### main #####################

if Gui.ActiveDocument is None:
  doc  = App.newDocument()
  doc.recompute()
  viewer = Gui.createViewer()
  view   = viewer.getViewer()
else:
  view = Gui.ActiveDocument.ActiveView

sg      = view.getSceneGraph()
root    = coin.SoSeparator()
sg.addChild(root)

cub1 = coin.SoCube()
addObj(root, cub1)

Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

### end ###
