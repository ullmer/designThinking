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
  divisions = soc.getDivisions()

  xImg = 10; xTxt =  315
  rankMap = {'asst':'Asst. Prof.', 'assoc':'Assoc. Prof.', 'full':'Professor',
             'lecturer':'Lecturer', 'slecturer':'Senior Lecturer', 
             'pop':'Prof. of Practice'}

  ps = cairo.PDFSurface("exCairo10.pdf", 2700, 648)
  cr = cairo.Context(ps)
  s = .38
  cr.scale(s,s)

  for division in divisions:
  
    yTxtOrig = yTxt =   70; dyTxt = 325
    yImgOrig = yImg =  350; dyImg = 325

    divFaculty = soc.getFacultyRankExtraByDivision(division)
  
    print("divFaculty:", str(division), str(divFaculty))
  
    #ps = cairo.PDFSurface("exCairo8.pdf", 504, 648)
  
    cr.set_source_rgb(0, 0, 0)
    #cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL,
    cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_BOLD)
    cr.set_font_size(40)

    idx = 0; 
    for faculty in divFaculty:
      if idx != 0 and idx % 5 == 0:  yTxt = yTxtOrig; xTxt += 600

      name, rank, extraRole = faculty
      if idx % 1 == 0: cr.set_source_rgba(0.8, 0.6, 0, .1)
      else:            cr.set_source_rgba(0.8, 0.6, 0, .95)
      cr.rectangle(xTxt-295, yTxt-50, xTxt+350, yTxt-50+dyImg)
      cr.fill()

      lastNameSpace = name.rfind(' ') #consider "Brian C. Dean"
      lastName  = name[lastNameSpace+1:]
      firstName = name[0:lastNameSpace]
  
      cr.move_to(xTxt, yTxt)
      g1 = .3; cr.set_source_rgb(g1,g1,g1)
      cr.show_text(firstName)       
  
      cr.move_to(xTxt, yTxt+40)
      g1 = 0; cr.set_source_rgb(g1,g1,g1)
      cr.show_text(lastName)       
  
      if rank in rankMap:
        cr.move_to(xTxt, yTxt+100)
        g3 = .55; cr.set_source_rgb(g3,g3,g3)
        cr.show_text(rankMap[rank])
  
      if extraRole != None:
        cr.move_to(xTxt, yTxt+160)
        cr.set_source_rgb(.4, .2, 0)
        cr.show_text(extraRole)
  
      yTxt += dyTxt;    idx += 1
  
    idx = 0
    for faculty in divFaculty:
      if idx != 0 and idx % 5 == 0: yImg = yImgOrig; xImg += 600
      name, rank, extra = faculty
      imageFn = name2image(name)
      try:
        imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
        cr.set_source_surface(imgSurf, xImg, yImg - dyImg)
        cr.paint()
      except: print("ignoring image:", imageFn); traceback.print_exc()
  
      idx += 1; yImg += dyImg
  

    xImg += 600; xTxt +=  600
  
  cr.show_page()
        
if __name__ == "__main__":    
  main()
  
### end ###
