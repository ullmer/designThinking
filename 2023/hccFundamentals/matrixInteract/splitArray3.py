### Split composite image for enodia

#enodiaAbout19a.png PNG 15000x4840 15000x4840+0+0 8-bit sRGB 2.34824MiB 0.000u 0:00.001
#srcDim   = [15000, 4840]

from PIL import Image

class tiledPanel:
  imgSrcFn = None
  imgSrc   = None
  targPane = None
  #arrayDim = [6, 3]
  arrayDim = [8, 9]
  blockDim = 228  # initially assume square
  padDim   = 76   # between blocks 
  panelWidth  = None
  panelHeight = None

  def __init__(self, imgSrc):
    self.imgSrc = imgSrc
    self.imgSrc = Image.open(self.imgSrcFn)
    #self.imgSrc.show()
    self.panelWidth, self.panelHeight = self.imgSrc.size
    self.tileWidth  = self.panelWidth /self.arrayDim[0]
    self.tileHeight = self.panelHeight/self.arrayDim[1]

    self.tileWidth  = self.blockDim + self.padDim
    self.tileHeight = self.blockDim + self.padDim

  def getTilesWide(self): return self.arrayDim[0]
  def getTilesHigh(self): return self.arrayDim[1]

  def extractPane(self, tileCol, tileRow):
    x1 = self.tileWidth  * tileCol
    y1 = self.tileHeight * tileRow
    x2 = x1 + self.blockDim
    y2 = y1 + self.blockDim

    self.targPane = self.imgSrc.crop((x1, y1, x2, y2))
    return self.targPane
    #self.targPane.show()

srcImg = "images/clemson-colleges-77g2-core.png"
tp = tiledPanel(srcImg)

tfnPre = "images/cc77g-"
for i in tp.getTilesWide():
  for j in tp.getTilesHigh():
    targPane = tp.extractPane(i,j)
    rowId    = chr(ord('A') + j)
    coordStr = "%s%i" % (rowId, i)

    tfn = tfnPre + coordStr + ".png"
    targPane.save(tfn)

### end ###
