# Tile an image into MxN subimages
# Brygg Ullmer, Clemson University
# Begun 2022-10-26

# Drawing from: 
#   https://www.geeksforgeeks.org/python-pil-image-crop-method/

import sys

# Importing Image class from PIL module
from PIL import Image

if len(sys.argv) <= 4: #insufficient command line arguments passed
  print("four arguments required: imgSrc.png imgTarg xTiles yTiles"); sys.exit(-1)

cmdName, imgSrcFn, imgTargFn, xTilesR, yTilesR = sys.argv # extract command-line arguments

xTiles = int(xTilesR); yTiles = int(yTilesR) #convert "R" raw=text to number

#print("y tiles:", yTiles)
#sys.exit(1)
 
# Opens a image in RGB mode
#im = Image.open(r"C:\Users\Admin\Pictures\geeks.png")
im = Image.open(imgSrcFn)
 
# Size of the image in pixels (size of original image) 
width, height = im.size

widthTile  = width/xTiles
heightTile = height/yTiles

for i in range(xTiles):
  for j in range(yTiles):
    left = widthTile * i;  right = left + widthTile
    top  = heightTile * j; bottom = top + heightTile

    im1   = im.crop((left, top, right, bottom))
    #outFn = "%s_%i_%i.png" % (imgTargFn, i+1, j+1)
    outFn = "%s/%i.png" % (imgTargFn, i+1)
    print(outFn)
    im1.save(outFn)

### end ### 

