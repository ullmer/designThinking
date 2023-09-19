### Split composite image for enodia

#enodiaAbout19a.png PNG 15000x4840 15000x4840+0+0 8-bit sRGB 2.34824MiB 0.000u 0:00.001
#srcDim   = [15000, 4840]

from PIL import Image

class tiledPanel:
  imgSrcFn = 'enodiaAbout20d.png'
  imgSrc   = None
  targPane = None
  #arrayDim = [6, 3]
  arrayDim = [8, 9]
  blockDim = 228  # initially assume square
  padDim   = 76   # between blocks 
  panelWidth  = None
  panelHeight = None

  def __init__(self):
    self.imgSrc = Image.open(self.imgSrcFn)
    #self.imgSrc.show()
    self.panelWidth, self.panelHeight = self.imgSrc.size
    self.tileWidth  = self.panelWidth /self.arrayDim[0]
    self.tileHeight = self.panelHeight/self.arrayDim[1]

  def extractPane(self, tileCol, tileRow):
    x1 = self.tileWidth  * tileCol
    y1 = self.tileHeight * tileRow
    x2 = self.tileWidth  * (tileCol+1)
    y2 = self.tileHeight * (tileRow+1)

    self.targPane = self.imgSrc.crop((x1, y1, x2, y2))
    return self.targPane
    #self.targPane.show()

tp = tiledPanel()

tfnPre = "enodiaAbout20dT"
for i in range(tp.arrayDim[0]):
  targPane = tp.extractPane(i,0)
  fn = tp.imgSrcFn; tfn = tfnPre + str(i) + ".png"
  targPane.save(tfn)

### end ###
