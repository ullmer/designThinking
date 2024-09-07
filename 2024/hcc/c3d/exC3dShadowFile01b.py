#fusion of exC3dShadow02b.py and exC3dImportFcstd.py

#Draws from: 
#https://forum.freecad.org/viewtopic.php?style=5&t=9663&start=30
#and Copilot 2024-09-07: python code for reading .FCSTd file into pivy SoSeparator within freecad

import FreeCAD as App
import FreeCADGui as Gui

from pivy import coin

dir = 'c:/git/designThinking/2024/hcc/c3d/'
fcstd_file_path = dir + "mit-campus05.FCStd"

# Open the FreeCAD document
doc = App.openDocument(fcstd_file_path)

# Get the active view's scene graph
view = Gui.ActiveDocument.ActiveView
root = view.getSceneGraph()

sotype=coin.SoType.fromName("SoShadowGroup")
shadow=sotype.createInstance()
shadow.precision.setValue(1)
shadow.quality.setValue(1)

sotype=coin.SoType.fromName("ShadowDirectionalLight")
light=sotype.createInstance()
light.intensity.setValue(200)
light.direction.setValue(-1,-1,-1)

# get the third node of the root (or search for SoSeparator)
scene=root.getChild(2)
root.removeChild(scene)

shadow.addChild(light)
shadow.addChild(scene)
root.addChild(shadow)

shadow.addChild(scene)

### end ###

