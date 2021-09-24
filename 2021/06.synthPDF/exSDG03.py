# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/
# https://zetcode.com/gfx/pycairo/shapesfills/
# https://zetcode.com/gfx/pycairo/transparency/
# https://pycairo.readthedocs.io/en/latest/reference/surfaces.html

from PIL import Image
import cairo, traceback

def genSdgImgFn(sdgNum): return "images/unsdg/%0.2i.png" % sdgNum

def main():
  ps = cairo.PDFSurface("exSDG03.pdf", 72*15, 72*5)
  cr = cairo.Context(ps)
  s = .05
  cr.scale(s,s)
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  cr.set_font_size(256); cr.move_to(10,200); cr.set_source_rgb(.1,.1,.6)
  cr.show_text('UN SDG')
  xImg = 10; dxImg = 300

  for sdgNum in range(1,18):
  
    yImgOrig = yImg  = 300; dyImg = 300
    imageFn = genSdgImgFn(sdgNum)

    try:
      imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
      cr.set_source_surface(imgSurf, xImg, yImg + dyImg)
      cr.paint()
    except: print("ignoring image:", imageFn); traceback.print_exc()

    if sdgNum %2 == 0: yImg += dyImg
    else:              xImg += dxImg; yImg = yImgOrig

  cr.show_page()
        
if __name__ == "__main__":    
  main()
  
### end ###
