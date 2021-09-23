# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/
# https://pycairo.readthedocs.io/en/latest/reference/surfaces.html

from PIL import Image
import cairo, traceback, socDb

def name2image(name):
  lowerName = name.lower()
  name2     = lowerName.replace(' ', '_')
  result    = "images/soc/%s.png" % name2
  return result

def main():

  soc = socDb.socDb()
  hccFaculty = soc.getFacultyByDivision('HCC')

  print("hccFaculty:", str(hccFaculty))

  ps = cairo.PDFSurface("exCairo7.pdf", 504, 648)
  cr = cairo.Context(ps)

  cr.set_source_rgb(0, 0, 0)
  #cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL,
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  s = .38
  cr.scale(s,s)
  cr.set_font_size(50)

  xImg = 10; xText = 200; idx = 0
  yorig = ypos = 70; dy = 330; imgDy = 370

  for faculty in hccFaculty:
    cr.move_to(xText, ypos)
    cr.show_text(faculty); ypos += dy

    imageFn = name2image(faculty)
    try:
      imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
      cr.set_source_surface(imgSurf, xImg, ypos-imgDy)
      cr.paint()
    except: print("ignoring image:", imageFn); traceback.print_exc()

    idx += 1
    if idx % 5 == 0: ypos = yorig; xImg += 600

  cr.show_page()
      
      
if __name__ == "__main__":    
  main()

### end ###
