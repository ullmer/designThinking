# First validation of Python port of 1995 3wish code
# Brygg Ullmer, Clemson University
# Original code begun fall 1995; here, 2023-10-20

import FreeCAD as App
import FreeCADGui as Gui
import pivy.coin as coin
import sys

sys.path.append('c:/git/designThinking/2023/hccFundamentals/3wish')
from w3core  import *
from w3shift import *

##################### main #####################

if Gui.ActiveDocument is None:
  doc  = App.newDocument()
  doc.recompute()
  viewer = Gui.createViewer()
  view   = viewer.getViewer()
else:
  view = Gui.ActiveDocument.ActiveView

Gui.activeDocument().activeView().setCameraType("Perspective")

sg      = view.getSceneGraph()
root    = coin.SoSeparator()
sg.addChild(root)
cube1, cube2 = coin.SoCube(), coin.SoCube()

s2 = coin.SoSeparator()
m1 = coin.SoMaterial()
m1.diffuseColor.setValue(1, 0, 0)
s2.addChild(m1)
s2.addChild(cube2)

s3 = coin.SoSeparator()
t3 = coin.SoTranslation(); t3.translation.setValue(1.3, 0, 0)
m3 = coin.SoMaterial();    m3.emissiveColor.setValue(80, 0, 0)
c3 = coin.SoCube()
for i in [c3.width, c3.height, c3.depth]: i.setValue(.3)

for i in [t3, m3, c3]: s3.addChild(i)
root.addChild(s3)

s4 = coin.SoSeparator()
l4 = coin.SoPointLight()
l4.color.setValue(1,0,0)
l4.intensity.setValue(10)
l4.location.setValue(0, 1.3, 0)
s4.addChild(l4); root.addChild(s4)

print(0); addNObj(root, "cube1", cube1)
print(1); addNObj(root, "cube2", s2)
print(2); moveNObj(root, "cube2", [3,3,3])
print(3)

Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

output = coin.SoOutput()
wa     = coin.SoWriteAction(output)
result = wa.apply(s2)

#bs = output.getBufferSize()
#print("bs:", bs)
#b  = output.getBuffer(bs)

print(">>>", dir(output))
print(">>", output)
#print(">>", b)

### end ###
