#https://forum.freecad.org/viewtopic.php?style=5&t=9663&start=30

from pivy import coin

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


