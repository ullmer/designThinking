# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/
# https://zetcode.com/gfx/pycairo/shapesfills/
# https://zetcode.com/gfx/pycairo/transparency/
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
  hccFaculty = soc.getFacultyRankByDivision('HCC')

  print("hccFaculty:", str(hccFaculty))

  ps = cairo.PDFSurface("exCairo8.pdf", 504, 648)
  cr = cairo.Context(ps)

  cr.set_source_rgb(0, 0, 0)
  #cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL,
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  s = .38
  cr.scale(s,s)
  cr.set_font_size(40)

  xImg = 10; xTxt =  315;   idx = 0
  yTxtOrig = yTxt =   70; dyTxt = 325
  yImgOrig = yImg =  350; dyImg = 325

  rankMap = {'asst':'Asst. Prof.', 'assoc':'Assoc. Prof.', 'full':'Professor'}
  
  for faculty in hccFaculty:
    name, rank = faculty
    if idx % 1 == 0: cr.set_source_rgba(0.8, 0.6, 0, .1)
    else:            cr.set_source_rgba(0.8, 0.6, 0, .95)
    cr.rectangle(xTxt-295, yTxt-50, xTxt+350, yTxt-50+dyImg)
    cr.fill()

    cr.move_to(xTxt, yTxt)
    cr.set_source_rgb(0,0,0)
    cr.show_text(name)       

    cr.move_to(xTxt, yTxt+50)
    cr.set_source_rgb(.3, .3, .3)
    cr.show_text(rankMap[rank])

    yTxt += dyTxt;    idx += 1
    if idx % 5 == 0:          yTxt = yTxtOrig; xTxt += 605

  idx = 0
  for faculty in hccFaculty:
    name, rank = faculty
    imageFn = name2image(name)
    try:
      imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
      cr.set_source_surface(imgSurf, xImg, yImg - dyImg)
      cr.paint()
    except: print("ignoring image:", imageFn); traceback.print_exc()

    idx += 1; yImg += dyImg

    if idx % 5 == 0: yImg = yImgOrig; xImg += 600

  cr.show_page()
      
      
if __name__ == "__main__":    
  main()

### end ###
