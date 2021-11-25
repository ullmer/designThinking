# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/
# https://zetcode.com/gfx/pycairo/shapesfills/
# https://zetcode.com/gfx/pycairo/transparency/
# https://pycairo.readthedocs.io/en/latest/reference/surfaces.html

from PIL import Image
import cairo, traceback, socDb, math

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

  divisionMap = {'CS':'computer science','HCC':'human-centered computing',
                 'VC':'visual computing','FOI':'faculty of instruction'}

  dimX = 72 * 11
  dimY = 72 * 8.5

  ps = cairo.PDFSurface("cuSocLP01.pdf", dimX, dimY)
  cr = cairo.Context(ps)
  #s = .38
  s = .18
  cr.scale(s,s)


  #cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL,
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  cr.set_font_size(256)
  cr.move_to(10,200)
  cr.set_source_rgb(.6, .4, 0)
  cr.show_text('clemson university :: school of computing')

  firstOne = True
  for division in divisions:
  
    yTxtOrig = yTxt  = 400; dyTxt = 325
    yImgOrig = yImg  = 680; dyImg = 325

    cr.set_font_size(80)
    cr.move_to(xTxt-300, yTxt-80)
    cr.set_source_rgb(.5, .3, 0)
    divName = divisionMap[division]
    cr.show_text(divName)       
  
    cr.set_font_size(40)
    divFaculty = soc.getFacultyRankExtraByDivision(division)
  
    print("divFaculty:", str(division), str(divFaculty))

    idx = 0
    for faculty in divFaculty:
      if idx != 0 and idx % 8 == 0:  yTxt = yTxtOrig; xTxt += 600

      name, rank, extraRole = faculty

      lastNameSpace = name.rfind(' ') #consider "Brian C. Dean"
      lastName  = name[lastNameSpace+1:]
      firstName = name[0:lastNameSpace]
  
      if rank in rankMap:
        cr.move_to(xTxt, yTxt+100)
        g3 = .55; cr.set_source_rgb(g3,g3,g3)
        cr.show_text(rankMap[rank])
  
      if extraRole != None:
        cr.move_to(xTxt, yTxt+160)
        cr.set_source_rgb(.4, .2, 0)
        cr.show_text(extraRole)
  
      if idx != 0 and idx % 8 == 0: yImg = yImgOrig; xImg += 600
      name, rank, extra = faculty
      imageFn = name2image(name)
      try:
        imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
        cr.set_source_rgba(1, 1, 1, .5)
        cr.set_source_surface(imgSurf, xImg, yImg - dyImg)
        cr.paint()
      except: print("ignoring image:", imageFn); traceback.print_exc()

      if firstOne:
        cr.set_source_rgba(1, .5, 0, .5)
        cr.rectangle(xTxt-300, yTxt-50, xTxt-215, yTxt-50+dyImg)
        cr.fill(); firstOne=False

        cr.set_source_rgba(1, .5, 0, .5)
        cr.rectangle(xTxt-85, yTxt-50, xTxt, yTxt-50+dyImg)
        cr.fill()

      cr.set_source_rgba(1, 1, 1, .5)
      cr.rectangle(xTxt-215, yTxt-50, xTxt+310, yTxt-50+dyImg)
      cr.fill()

      cr.move_to(xTxt-265, yTxt+250)
      cr.rotate(math.pi/-2.)
      g1 = 1.; cr.set_source_rgba(g1,g1,g1, .55)
      cr.show_text(firstName)       
      cr.rotate(math.pi/2.)

      cr.move_to(xTxt-230, yTxt+250)
      g1 = 1; cr.set_source_rgba(g1,g1,g1, .85)
      cr.rotate(math.pi/-2.)
      cr.show_text(lastName)       
      cr.rotate(math.pi/2.)
  
      idx += 1; yImg += dyImg; yTxt += dyTxt
  

    xImg += 600; xTxt +=  600
  
  cr.show_page()
        
if __name__ == "__main__":    
  main()
  
### end ###
