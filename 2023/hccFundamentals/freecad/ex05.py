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

lts  = coin.SoTransformSeparator() #move light, without partioning from scene (like regular Separator) 
ltst = coin.SoTranslation(); ltst.translation.setValue(0, .7, 0)
l1 = coin.SoPointLight()
l1.color.setValue(1,0,0)
l1.intensity.setValue(2)
lts.addChild(ltst); lts.addChild(l1)
root.addChild(lts)

#s3 = coin.SoSeparator()
s3 = coin.SoTransformSeparator()
t3 = coin.SoTranslation(); t3.translation.setValue(.7, 0, 0)
m3 = coin.SoMaterial();    m3.emissiveColor.setValue(80, 0, 0)
c3 = coin.SoCube()
for i in [c3.width, c3.height, c3.depth]: i.setValue(.3)
for i in [t3, m3, c3]: s3.addChild(i)
root.addChild(s3)

c1    = coin.SoSeparator()
c1Mat = coin.SoMaterial()
cone1 = coin.SoCone()
c1.addChild(c1Mat); c1.addChild(cone1)

s2 = coin.SoSeparator()
m1 = coin.SoMaterial()
m1.diffuseColor.setValue(1, 0, 0)
s2.addChild(m1)

addNObj(root,  "cone1", c1)
#moveNObj(root, "cube2", [3,3,3])
#moveNObj(root, "cube2", [3,3,3])

Gui.runCommand('Std_ViewZoomOut',0)
Gui.SendMsgToActiveView("ViewFit")

### end ###
