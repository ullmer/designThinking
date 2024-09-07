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
sg = view.getSceneGraph()

# Create a separator for the imported objects
importedSeparator = coin.SoSeparator()

# Iterate through all objects in the document
for obj in doc.Objects:
    if hasattr(obj, 'Shape'):
        shape = obj.Shape
        shapeNode = coin.SoShapeKit()
        shapeNode.setPart('shape', coin.SoIndexedFaceSet())
        shapeNode.setPart('coordinate', coin.SoCoordinate3())
        shapeNode.setPart('material', coin.SoMaterial())
        importedSeparator.addChild(shapeNode)

# Add the imported objects to the scene graph
#sg.addChild(importedSeparator)

# Fit the view to the scene
view.fitAll()

sotype=coin.SoType.fromName("SoShadowGroup")
shadow=sotype.createInstance()
shadow.precision.setValue(1)
shadow.quality.setValue(1)

sotype=coin.SoType.fromName("ShadowDirectionalLight")
light=sotype.createInstance()
light.intensity.setValue(200)
light.direction.setValue(-1,-1,-1)

view=Gui.ActiveDocument.ActiveView.getViewer()
root=view.getSceneGraph()
# get the third node of the root (or search for SoSeparator)
scene=root.getChild(2)
root.removeChild(scene)

shadow.addChild(light)
shadow.addChild(scene)
root.addChild(shadow)

shadow.addChild(importedSeparator)

### end ###

