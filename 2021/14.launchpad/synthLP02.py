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
 
  outputFn = "cuSocLP02.pdf"

  rankMap = {'asst':'Asst. Prof.', 'assoc':'Assoc. Prof.', 'full':'Professor',
             'lecturer':'Lecturer', 'slecturer':'Senior Lecturer', 
             'pop':'Prof. of Practice'}

  divisionMap = {'CS':'computer science','HCC':'human-centered computing',
                 'VC':'visual computing','FOI':'faculty of instruction'}

  dimX  = 72 * 11
  dimY  = 72 * 8.5
  xImg  = 10
  xTxt  =  315
  scale = .18  #.38
  ps    = None
  cr    = None
  soc   = None
  divisions = None

  yTxtOrig = yTxt  = 400; dyTxt = 325
  yImgOrig = yImg  = 680; dyImg = 325
  xIncr = 350

  ###################### constructor ######################

  def __init__(self):

    self.ps = cairo.PDFSurface(self.outputFn, self.dimX, self.dimY)
    self.cr = cairo.Context(self.ps)
    self.cr.scale(self.scale,self.scale)

    self.cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                                      cairo.FONT_WEIGHT_BOLD)
    self.cr.set_font_size(256)
    self.cr.move_to(10,200)
    self.cr.set_source_rgb(.6, .4, 0)
    self.cr.show_text('clemson university :: school of computing')

    self.soc = socDb.socDb()
    self.divisions = self.soc.getDivisions()

    for division in self.divisions: self.renderDivision(division)
  
    self.cr.show_page()
  
  ###################### name to image ######################
  
  def name2image(self, name):
    lowerName = name.lower()
    name2     = lowerName.replace(' ', '_')
    result    = "images/soc/%s.png" % name2
    return result
   
  ###################### render division ######################

  def renderDivision(self, division): 
  
    self.cr.set_font_size(60)
    self.cr.move_to(self.xTxt-300, self.yTxt-80)
    self.cr.set_source_rgb(.5, .3, 0)
    divName = self.divisionMap[division]
    self.cr.show_text(divName)       
    
    self.cr.set_font_size(40)
    divFaculty = self.soc.getFacultyRankExtraByDivision(division)
    
    print("divFaculty:", str(division), str(divFaculty))
  
    idx = 0
    for faculty in divFaculty:
      if idx != 0 and idx % 4 == 0:  
        self.yTxt = self.yTxtOrig; self.xTxt += self.xIncr
  
      name, rank, extraRole = faculty
  
      lastNameSpace = name.rfind(' ') #consider "Brian C. Dean"
      lastName  = name[lastNameSpace+1:]
      firstName = name[0:lastNameSpace]
    
      if idx != 0 and idx % 4 == 0: 
        self.yImg = self.yImgOrig; self.xImg += self.xIncr

      name, rank, extra = faculty
      imageFn = self.name2image(name)
      try:
        imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
        #self.cr.set_source_rgba(1, 1, 1, .5)
        self.cr.set_source_rgba(1, 1, 1, .15)
        self.cr.set_source_surface(imgSurf, self.xImg, self.yImg - self.dyImg)
        self.cr.paint()
      except: print("ignoring image:", imageFn); traceback.print_exc()
  
      #self.cr.set_source_rgba(1, .5, 0, .5)
      self.cr.set_source_rgba(1, .5, 0, .85)
      self.cr.rectangle(self.xTxt-305, self.yTxt-45, 100, 300)
      self.cr.fill(); firstOne=False
  
      #cr.set_source_rgba(1, .5, 0, .5)
      #self.cr.set_source_rgba(.05, 0, .05, .7)
      self.cr.set_source_rgba(.05, 0, .05, .85)
      if extraRole == None: self.cr.rectangle(self.xTxt-40, self.yTxt-45, 35, 300)
      else:                 self.cr.rectangle(self.xTxt-70, self.yTxt-45, 70, 300)
      self.cr.fill()
  
      self.cr.set_source_rgba(1, 1, 1, .5)
      self.cr.rectangle(self.xTxt-215, self.yTxt-50, 300, 310)
      self.cr.fill()
  
      self.cr.set_font_size(40)
      self.cr.move_to(self.xTxt-265, self.yTxt+250)
      self.cr.rotate(math.pi/-2.)
      g1 = 1.; self.cr.set_source_rgba(g1,g1,g1, .55)
      self.cr.show_text(firstName)       
      self.cr.rotate(math.pi/2.)

      self.cr.move_to(self.xTxt-230, self.yTxt+250)
      g1 = 1; self.cr.set_source_rgba(g1,g1,g1, .85)
      self.cr.rotate(math.pi/-2.)
      self.cr.show_text(lastName)       
      self.cr.rotate(math.pi/2.)
  
      self.cr.set_font_size(30)
      if rank in self.rankMap:
        self.cr.move_to(self.xTxt-12, self.yTxt+250)
        self.cr.rotate(math.pi/-2.)
        g3 = 1; self.cr.set_source_rgba(g3,g3,g3, .8)
        self.cr.show_text(self.rankMap[rank])
        self.cr.rotate(math.pi/2.)
  
      if extraRole != None:
        self.cr.move_to(self.xTxt-40, self.yTxt+250)
        self.cr.rotate(math.pi/-2.)
        self.cr.set_source_rgba(.9, .9, .9, .8)
        self.cr.show_text(extraRole)
        self.cr.rotate(math.pi/2.)
  
      idx += 1; self.yImg += self.dyImg; self.yTxt += self.dyTxt
  
    self.xImg += self.xIncr; self.xTxt += self.xIncr

def main():
  imr = interactionMapRep()
        
if __name__ == "__main__":    
  main()
  
### end ###
