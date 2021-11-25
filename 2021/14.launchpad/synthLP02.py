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

class interactionMapRep:
 
  rankMap = {'asst':'Asst. Prof.', 'assoc':'Assoc. Prof.', 'full':'Professor',
             'lecturer':'Lecturer', 'slecturer':'Senior Lecturer', 
             'pop':'Prof. of Practice'}

  divisionMap = {'CS':'computer science','HCC':'human-centered computing',
                 'VC':'visual computing','FOI':'faculty of instruction'}

  dimX = 72 * 11
  dimY = 72 * 8.5
  xImg = 10
  xTxt =  315
  s    = .18  #.38
  ps   = None
  cr   = None


  ###################### constructor ######################

  def __init__(self):

    self.ps = cairo.PDFSurface("cuSocLP01.pdf", dimX, dimY)
    self.cr = cairo.Context(ps)
    self.cr.scale(s,s)

  ###################### name to image ######################

  def name2image(self, name):
    lowerName = name.lower()
    name2     = lowerName.replace(' ', '_')
    result    = "images/soc/%s.png" % name2
    return result
   
  ###################### render division ######################

  def renderDivision(self, divisionName): 
      yTxtOrig = yTxt  = 400; dyTxt = 325
      yImgOrig = yImg  = 680; dyImg = 325
      xIncr = 350
  
      cr.set_font_size(60)
      cr.move_to(xTxt-300, yTxt-80)
      cr.set_source_rgb(.5, .3, 0)
      divName = divisionMap[division]
      cr.show_text(divName)       
    
      cr.set_font_size(40)
      divFaculty = soc.getFacultyRankExtraByDivision(division)
    
      print("divFaculty:", str(division), str(divFaculty))
  
      idx = 0
      for faculty in divFaculty:
        if idx != 0 and idx % 4 == 0:  yTxt = yTxtOrig; xTxt += xIncr
  
        name, rank, extraRole = faculty
  
        lastNameSpace = name.rfind(' ') #consider "Brian C. Dean"
        lastName  = name[lastNameSpace+1:]
        firstName = name[0:lastNameSpace]
    
        if idx != 0 and idx % 4 == 0: yImg = yImgOrig; xImg += xIncr
        name, rank, extra = faculty
        imageFn = name2image(name)
        try:
          imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
          cr.set_source_rgba(1, 1, 1, .5)
          cr.set_source_surface(imgSurf, xImg, yImg - dyImg)
          cr.paint()
        except: print("ignoring image:", imageFn); traceback.print_exc()
  
        cr.set_source_rgba(1, .5, 0, .5)
        cr.rectangle(xTxt-305, yTxt-45, 100, 300)
        cr.fill(); firstOne=False
  
        #cr.set_source_rgba(1, .5, 0, .5)
        cr.set_source_rgba(.05, 0, .05, .7)
        if extraRole == None: cr.rectangle(xTxt-40, yTxt-45, 35, 300)
        else:                 cr.rectangle(xTxt-70, yTxt-45, 70, 300)
        cr.fill()
  
        cr.set_source_rgba(1, 1, 1, .5)
        cr.rectangle(xTxt-215, yTxt-50, 300, 310)
        cr.fill()
  
        cr.set_font_size(40)
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
    
        cr.set_font_size(30)
        if rank in rankMap:
          cr.move_to(xTxt-12, yTxt+250)
          cr.rotate(math.pi/-2.)
          g3 = 1; cr.set_source_rgba(g3,g3,g3, .8)
          cr.show_text(rankMap[rank])
          cr.rotate(math.pi/2.)
    
        if extraRole != None:
          cr.move_to(xTxt-40, yTxt+250)
          cr.rotate(math.pi/-2.)
          cr.set_source_rgba(.9, .9, .9, .8)
          cr.show_text(extraRole)
          cr.rotate(math.pi/2.)
    
        idx += 1; yImg += dyImg; yTxt += dyTxt
    
      xImg += xIncr; xTxt += xIncr
  
def main():
  soc = socDb.socDb()
  divisions = soc.getDivisions()


  #cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL,
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  cr.set_font_size(256)
  cr.move_to(10,200)
  cr.set_source_rgb(.6, .4, 0)
  cr.show_text('clemson university :: school of computing')

  for division in divisions: renderDivision(division)
  
  cr.show_page()
        
if __name__ == "__main__":    
  main()
  
### end ###
