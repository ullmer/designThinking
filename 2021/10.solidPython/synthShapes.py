# Synthesize SolidPython shapes
# Brygg Ullmer, Clemson University
# Begun 2019-05-19

from solid import *
from solid.utils import *

############### synthesize cylindrical bar ###############

def synthCylBar(od, id, barThick):
  outerCyl1 = cylinder(r=od/2., h=barThick)
  innerCyl1 = cylinder(r=id/2., h=barThick*2)
  innerCyl2 = translate([0,0,-barThick/2.])(innerCyl1)
  cylBar    = outerCyl1 - innerCyl2
  return cylBar

############## synthesize pipe ##############

def synthPipe(od, id, pipeLen):
  return synthCylBar(od, id, pipeLen)

############## synthesize lite-brite(tm) peg ##############

def synthLBPeg():
  h1 = .37; h2 = .03; h3 = .49    #diameters of peg tiers
  cyl1a  = cylinder(d=.18 , h=h1) #base/lowest tier
  cyl2a  = cylinder(d=.235, h=h2) #retaining ring
  cyl3a  = cylinder(d=.22,  h=h3) #upper tier
  sph1a  = sphere(.11)            # top of lens
  cyl2b  = translate([0,0,h1      ])(cyl2a)
  cyl3b  = translate([0,0,h1+h2   ])(cyl3a) 
  sph1b  = translate([0,0,h1+h2+h3])(sph1a)
  lbPeg  = cyl1a + cyl2b + cyl3b + sph1b
  return lbPeg

############### synthesize bas relief arc ###############

def synthBRArc(diam, thickness, height, beginDegree, endDegree):
  od = diam + thickness/2.
  id = diam - thickness/2.
  l2a   = height * 2
  pip1a = synthPipe(od,id,height)
  l1  = diam   * 1.5; l1b = l1 / 2.
  l2 = height * 2;    l2b = l2 / 2.
 
  cut1a = cube([l1, l1, l2])
  cut1b = translate([0,-l1b, -.01])(cut1a)
  #cut1b = translate([0,-l1b, -l2a])(cut1a)
  cut1c = rotate(a=[0,0,beginDegree])(cut1b)
  cut2c = rotate(a=[0,0,180-endDegree])(cut1b)

  result = pip1a - (cut1b + cut2c)
  #result = pip1a + (cut1b + cut2c)
  return result

############### synthesize bas relief arc ###############

def synthBRArc2(diam, thickness, height, targDegree, targWidth):
 tw2 = targWidth / 2.
 brA1 = synthBRArc(diam, thickness, height, 0, targWidth)
 brA2 = rotate(a=[0,0,targDegree+tw2])(brA1)
 return brA2

############### synthesize cylindrical I-bar ###############

def synthCylIBar(od, id, barThick, wallThick, orient):
  cylBar1   = synthCylBar(od, id, barThick)
  od2       = od - wallThick*2.
  id2       = id + wallThick*2.

  cylBar2 = synthCylBar(od2, id2, barThick)
  cylBar3 = translate([0,0,orient*wallThick])(cylBar2)
  cylBar4 = cylBar1 - cylBar3
  return cylBar4

############### synthesize I-bar ###############

def synthIBar(len, wid, barThick, wallThick, orient1, orient2):
  #bar1 = cube([wid, len, barThick])
  bar1 = cube([len, wid, barThick])
  wid2 = wid - wallThick*2.
  overshoot = .3

  bar2 = cube([len+overshoot, wid2, barThick])
  #bar3 = translate([wallThick,-overshoot/2.,orient*wallThick])(bar2a)
  bar3 = translate([-overshoot/2.,wallThick,orient1*wallThick])(bar2)
  bar4 = bar1 - bar3
  #bar4 = bar1 + bar3
  bar5 = rotate(a=[0,0,orient2])(bar4)
  return bar5


############### synthesize quarter pipe ###############

def synthHalfPipe(od, id, pipeLen):
  cb1   = synthCylBar(od, id, pipeLen)
  l1    = od * 1.5
  l1a   = od / 2.
  l1b   = l1 / 2.
  l2    = pipeLen * 1.5
  l2a   = pipeLen * .1
  cut1a = cube([l1, l1, l2])
  cut1b = translate([0,-l1b, -l2a])(cut1a)

  result = cb1 - cut1b
  return result

############### synthesize quarter pipe ###############

def synthQuarterPipe(od, id, pipeLen):
  cb1   = synthCylBar(od, id, pipeLen)
  l1    = od * 1.5
  l1a   = od / 2.
  l1b   = l1 / 2.
  l2    = pipeLen * 1.5
  l2a   = pipeLen * .1
  cut1a = cube([l1, l1, l2])
  cut1b = translate([0,-l1b, -l2a])(cut1a)
  cut2b = rotate(a=[0,0,90])(cut1b)

  result = cb1 - (cut1b + cut2b)
  return result

############### synthesize cylindrical I-bar ###############

def synthCylIBar(od, id, barThick, wallThick, orient):
  cylBar1   = synthCylBar(od, id, barThick)
  od2       = od - wallThick*2.
  id2       = id + wallThick*2.

  cylBar2 = synthCylBar(od2, id2, barThick)
  cylBar3 = translate([0,0,orient*wallThick])(cylBar2)
  cylBar4 = cylBar1 - cylBar3
  return cylBar4

############### synthesize I-bar ###############

def synthIBar(len, wid, barThick, wallThick, orient1, orient2):
  #bar1 = cube([wid, len, barThick])
  bar1 = cube([len, wid, barThick])
  wid2 = wid - wallThick*2.
  overshoot = .3

  bar2 = cube([len+overshoot, wid2, barThick])
  #bar3 = translate([wallThick,-overshoot/2.,orient*wallThick])(bar2a)
  bar3 = translate([-overshoot/2.,wallThick,orient1*wallThick])(bar2)
  bar4 = bar1 - bar3
  #bar4 = bar1 + bar3
  bar5 = rotate(a=[0,0,orient2])(bar4)
  return bar5

############### synthesize I-box ###############

def synthIBox(len, wid, barWidth, barThick, wallThick, orient):
  bar1 = synthIBar(len, barWidth, barThick, wallThick, orient, 0)
  bar2 = translate([0, wid - barWidth, 0])(bar1)

  bar3 = synthIBar(wid, barWidth, barThick, wallThick, orient, 90)
  bar4 = translate([len - barWidth, 0, 0])(bar3)
  bars5 = bar3 + bar4
  bars6 = translate([barWidth,0,0])(bars5)

  bars1 = bar1 + bar2 + bars6
  bars2 = translate([-len/2., -wid/2., 0])(bars1)
  return bars2

############### synthesize screw point ###############

def synthPaddedScrewpoint(od, id, thickness, padLength, doubleFixtured):

  outerCyl1 = cylinder(r=od/2., h=thickness)
  innerCyl1 = cylinder(r=id/2., h=thickness*2)
  innerCyl2 = translate([0,0,-thickness/2.])(innerCyl1)

  cylpad1 = cube([padLength, od, thickness])
  #cylpad2 = translate([padLength/2., -od/2., 0])(cylpad1)
  cylpad2 = translate([0, -od/2., 0])(cylpad1)

  if doubleFixtured == 0:
    result  = outerCyl1 + cylpad2 - innerCyl2
  else:
    angle=90
    if doubleFixtured < 0:
      angle*=-1
    cylpad3 = rotate(a=[0,0,angle])(cylpad2)
    result  = outerCyl1 + cylpad2 + cylpad3 - innerCyl2

  return result

############### synthesize flange ###############

def synthFlange(od, id):
  cyl1a = cylinder(r=od, h=1)
  sph1a = sphere()
  sph1b = scale([.5,.5,2])(sph1a)
  sph1c = color(Red)(sph1b)
  sph1d = translate([0,0,1.985])(sph1c)
  cub1a = cube([2,2,2])
  cub1b = translate([-1,-1,.05])(cub1a)

  #result = cyl1a + sph1d
  #result += cub1b
  result = cyl1a * sph1d
  result -= cub1b
  return result

############### synthesize multiflanged peg ###############

def synthMultiflangePeg(numFlanges, maxFlanges, od, id, constantHeight):
  flange = synthFlange(od,id)
  flangeHeight    = .05 # better if calculated, but offline presently
  interFlangeDist = .03
  id2      = id  / 2.
  id3      = id2 / 2.
  id4      = id3 / 2.
  od3      = od * 2. / 3.
  ribStyle = 2
  
  sfhifd = flangeHeight+interFlangeDist #sum, flange height + interFD
  if constantHeight:
    height  = sfhifd*maxFlanges
  else:
    height = sfhifd*numFlanges
  height2 = height / 2.

  #rib1a = cube([id2,id2,height])
  #rib1a = cube([id2*2./3.,id,height])
  rib1a = cube([id3,id,height])
  rib1b = translate([-id4,-id2,0])(rib1a)

  #rib2a = cube([id, id2*2./3., height])
  rib2a = cube([id, id3, height])
  rib2b = translate([-id2,-id4,0])(rib2a)

  if constantHeight:
    yoff   = height-flangeHeight
  else:
    yoff   = flangeHeight

  if ribStyle == 1:
    dx     = id2 
    rib1c  = translate([-dx, -dx, 0])(rib1b)
    rib2c  = translate([ dx, -dx, 0])(rib1b)
    rib3c  = translate([-dx,  dx, 0])(rib1b)
    rib4c  = translate([ dx,  dx, 0])(rib1b)
    
  if ribStyle == 2:
    rib1c  = translate([-id2,  0, 0])(rib2b)
    rib2c  = translate([ id2,  0, 0])(rib2b)
    rib3c  = translate([0,  -id2, 0])(rib1b)
    rib4c  = translate([0,   id2, 0])(rib1b)

  ribs = rib1c + rib2c + rib3c + rib4c
  result = ribs

  for i in range(numFlanges):
    flangeN = translate([0,0,yoff])(flange)
    result += flangeN
    if constantHeight:
      yoff -= sfhifd
    else:
      yoff += sfhifd
   
  return result

############### synthesize multiflanged perforated peg ###############

def synthMultiflangePerfPeg(numFlanges, maxFlanges, od, id, constantHeight):
  flangeHeight    = .05 # better if calculated, but offline presently
  interFlangeDist = .03
  sfhifd  = flangeHeight+interFlangeDist #sum, flange height + interFD
  height  = sfhifd*maxFlanges

  peg = synthMultiflangePeg(numFlanges, maxFlanges, od, id, constantHeight)
  cyl1a = cylinder(r=.04, h=height+.5)
  cyl1b = translate([0,0,-.25])(cyl1a)

  result = peg - cyl1b
  return result

############## torus ############## 

def torus(od, id):
  global tokSegments
  cr = (od-id)/4.           #toroidal circle radius
  cir1a = circle(r = cr)    #circle(r = cr, $fn = 100);
  cir1b = translate([od/2.-cr,0,0])(cir1a)

  tor1 = rotate_extrude(segments=tokSegments)(cir1b)
  return tor1

############### synthesize hemisphere shell ###############

def synthHemiShell(od, id):
  shell = sphere(od) - sphere(id)
  s     = od * 2.1
  s2    = -s / 2.
  cut1a = cube([s,s,s])
  cut1b = translate([s2,s2,-s])(cut1a)

  #result = shell + cut1b
  result = shell - cut1b
  return result

############### synthesize squashed hemisphere shell ###############

def synthSqHemiShell(od, height, thick):
  shell1a = sphere()
  shell1b = scale([od,od,height])(shell1a)

  od2 = od     - (2. * thick)
  h2  = height - (2. * thick)

  shell2b = scale([od2, od2, h2])(shell1a)
  shell3c = shell1b - shell2b
  
  s     = od * 2.1
  s2    = -s / 2.
  cut1a = cube([s,s,s])
  cut1b = translate([s2,s2,-s])(cut1a)

  #result = shell3c + cut1b
  result = shell3c - cut1b
  return result

############### synthesize squashed hemisphere shell ###############

def synthSqQHemiShell(od, height, thick):
  sqHemiShell = synthSqHemiShell(od, height, thick)

  s     = od * 2.1
  s2    = -s / 2.
  cut1a = cube([s,s,s])
  cut1b = translate([s2,0,0])(cut1a)

  result = sqHemiShell - cut1b
  return result

############### synthesize half pipe ###############

def synthHalfPipe(od, id, pipeLen):
  cb1   = synthCylBar(od, id, pipeLen)
  l1    = od * 1.5
  l1a   = od / 2.
  l1b   = l1 / 2.
  l2    = pipeLen * 1.5
  l2a   = pipeLen * .1
  cut1a = cube([l1, l1, l2])
  cut1b = translate([0,-l1b, -l2a])(cut1a)

  result = cb1 - cut1b
  return result

############### synthesize assym half pipe ###############

def synthAssymHalfPipe(od1, od2, thick, bandWidth):
  outerCyl1a = cylinder(r=1, h=bandWidth)
  outerCyl1b = scale([od1, od2, 1])(outerCyl1a)

  innerCyl1a = cylinder(r=1, h=thick*2)
  innerCyl1b = scale([od1-thick/2., od2-thick/2., 2])(outerCyl1a)
  innerCyl2b = translate([0,0,-thick/2.])(innerCyl1b)
  pip1 = outerCyl1b - innerCyl2b

  od = od1
  if od2 > od:
    od = od2

  l1    = od * 3
  l1a   = od / 2.
  l1b   = l1 / 2.
  l2    = bandWidth * 1.5
  l2a   = bandWidth * .1
  cut1a = cube([l1, l1, l2])
  cut1b = translate([0,-l1b, -l2a])(cut1a)

  result = pip1 - cut1b
  return result

############### synthesize quarter pipe ###############

def synthQuarterPipe(od, id, pipeLen):
  cb1   = synthCylBar(od, id, pipeLen)
  l1    = od * 1.5
  l1a   = od / 2.
  l1b   = l1 / 2.
  l2    = pipeLen * 1.5
  l2a   = pipeLen * .1
  cut1a = cube([l1, l1, l2])
  cut1b = translate([0,-l1b, -l2a])(cut1a)
  cut2b = rotate(a=[0,0,90])(cut1b)

  result = cb1 - (cut1b + cut2b)
  return result

### end ###

