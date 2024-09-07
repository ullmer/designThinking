#copilot 2024-09-07: python code using coin3d and freecad with several cubes shadowcasting using soshadowgroup

import FreeCAD as App
import FreeCADGui as Gui
from pivy import coin

# Create a new document
doc = App.newDocument("ShadowCubes")

# Get the active view's scene graph
view = Gui.ActiveDocument.ActiveView
sg = view.getSceneGraph()

# Create a shadow group
shadowGroup = coin.SoShadowGroup()
shadowGroup.intensity = 0.5  # Adjust shadow intensity

# Create a light source
light = coin.SoDirectionalLight()
light.direction = (0, -1, -1)
shadowGroup.addChild(light)

# Create multiple cubes
for i in range(5):
    for j in range(5):
        cubeTransform = coin.SoTransform()
        cubeTransform.translation = (i * 2, j * 2, 0)
        
        cube = coin.SoCube()
        cube.width = 1
        cube.height = 1
        cube.depth = 1
        
        cubeSeparator = coin.SoSeparator()
        cubeSeparator.addChild(cubeTransform)
        cubeSeparator.addChild(cube)
        
        shadowGroup.addChild(cubeSeparator)

# Add the shadow group to the scene graph
sg.addChild(shadowGroup)

# Fit the view to the scene
view.fitAll()

### end ###
