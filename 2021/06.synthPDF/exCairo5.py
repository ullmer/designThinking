# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/

from PIL import Image
import cairo
import socDb

def name2image(name):
  lowerName = name.lower()
  name2     = lowerName.replace(' ', '_')
  result    = "images/soc/%s.jpg" % name2
  return result

def main():

  soc = socDb.socDb()
  hccFaculty = soc.getFacultyByDivision('HCC')

  print("hccFaculty:", str(hccFaculty))

  ps = cairo.PDFSurface("exCairo5.pdf", 504, 648)
  cr = cairo.Context(ps)

  cr.set_source_rgb(0, 0, 0)
  #cr.select_font_face("Futura Bk BT")
  cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_NORMAL)
  cr.set_font_size(24)

  xImg = 10;  xText = 30
  ypos = 150; yx = 30  
  for faculty in hccFaculty:
    cr.move_to(xText, ypos)
    cr.show_text(faculty); ypos += yx

    imgSurf = cairo.ImageSurface.create_from_png(name2image(faculty))
    cr.set_source_surface(imgSurf, xImg, ypos)
    cr.paint()

  cr.show_page()
      
      
if __name__ == "__main__":    
  main()

### end ###
