# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/

from PIL import Image
import cairo
import socDb

def main():

  soc = socDb.socDb()
  hccFaculty = soc.getFacultyByDivision('HCC')

  print("hccFaculty:", str(hccFaculty))

  imgFn   = 'images/computing2.png'
  imgSurf = cairo.ImageSurface.create_from_png(imgFn)

  ps = cairo.PDFSurface("exCairo4.pdf", 504, 648)
  cr = cairo.Context(ps)

  cr.set_source_rgb(0, 0, 0)
  cr.select_font_face("Oswald", cairo.FONT_SLANT_NORMAL,
      cairo.FONT_WEIGHT_NORMAL)
  cr.set_font_size(24)

  ypos = 150; yx = 30  
  for faculty in hccFaculty:
    cr.move_to(10, ypos)
    cr.show_text(faculty); ypos += yx

  cr.set_source_surface(imgSurf, 10, 10)
  cr.paint()

  cr.show_page()
      
      
if __name__ == "__main__":    
  main()

### end ###
