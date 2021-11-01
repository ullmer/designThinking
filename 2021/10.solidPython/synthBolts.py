# Synthesize bolts within SolidPython
# Brygg Ullmer, Clemson University
# Begun 2021-10-31

from solid import *
from solid.utils import *
import yaml

#############################################
############### mcmaster bolt ###############

class mcmBolt: 

############### synthesize cylindrical bar ###############

def synthCylBar(od, id, barThick):
############### synthesize cylindrical bar ###############

def synthCylBar(od, id, barThick):
  outerCyl1 = cylinder(r=od/2., h=barThick)
  innerCyl1 = cylinder(r=id/2., h=barThick*2)
  innerCyl2 = translate([0,0,-barThick/2.])(innerCyl1)
  cylBar    = outerCyl1 - innerCyl2
  return cylBar

### end ###

