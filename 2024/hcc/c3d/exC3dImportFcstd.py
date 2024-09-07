#copilot 2024-09-07: python code for reading .FCSTd file into pivy SoSeparator within freecad

import FreeCAD as App
import FreeCADGui as Gui
from pivy import coin

# Path to your .FCStd file
fcstd_file_path = "path/to/your/file.FCStd"

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
sg.addChild(importedSeparator)

# Fit the view to the scene
view.fitAll()

### end ###

