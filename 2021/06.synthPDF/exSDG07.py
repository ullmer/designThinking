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
  pageWidth = 72*7; pageHeight = 72*5 # 5x7" pages
  ps = cairo.PDFSurface("exSDG07.pdf", pageWidth, pageHeight)
  cr = cairo.Context(ps)
  s = .05
  cr.scale(s,s)
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  xImgOrig = xImg = 500; dxImg = 3000
  yImgOrig = yImg = 1000; dyImg = 3000
  pageNum = 1

  for sdgNum in range(1,18):
    imageFn = genSdgImgFn(sdgNum)

    if sdgNum % 6 == 1:
      cr.set_source_rgba(0.8, 0.6, 0, .95)
      cr.rectangle(0, 0, pageWidth*20, 1000)
      cr.fill()

      cr.set_font_size(1000); cr.move_to(10,800); cr.set_source_rgba(1,1,1,.8)
      cr.show_text('un sdg :: p%i' % pageNum); pageNum += 1

    try:
      imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
      cr.set_source_surface(imgSurf, xImg, yImg)
      cr.paint()
    except: print("ignoring image:", imageFn); traceback.print_exc()

    if sdgNum %2 == 1: yImg += dyImg
    else:              xImg += dxImg;  yImg = yImgOrig
    if sdgNum %6 == 0: cr.show_page(); xImg = xImgOrig # render + new page
        
if __name__ == "__main__":    
  main()
  
### end ###
