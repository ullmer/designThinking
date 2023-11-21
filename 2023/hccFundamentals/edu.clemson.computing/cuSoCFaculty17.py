# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/
# https://zetcode.com/gfx/pycairo/shapesfills/
# https://zetcode.com/gfx/pycairo/transparency/
# https://pycairo.readthedocs.io/en/latest/reference/surfaces.html

from PIL import Image
import cairo, traceback, socDb, sys

def name2image(name):
  lowerName = name.lower()
  name2     = lowerName.replace(' ', '_')
  result    = "images/soc/%s.png" % name2
  return result

def main():
  
  #normWidth  = .8
  normWidth  = .7
  #normHeight = 22
  normHeight = .3
  pixelScale = 300

  #https://www.clemson.edu/brand/guide/color.html
  colors = {}; cmap = {}
  colors['bowman']     = [ 84,  98,  35, 0]
  colors['howard']     = [140, 130, 121, 0]
  colors['bridge']     = [  0,  94, 184, 0]
  colors['reflection'] = [  0,  94, 184, 0]
  colors['cbrick']     = [185,  71,   0, 0]
  colors['sflag']      = [  0,  32,  91, 0]
  
  cmap['CS']  = 'howard'
  cmap['FOI'] = 'reflection'
  cmap['HCC'] = 'bowman'
  cmap['VC']  = 'bridge'

  soc = socDb.socDb()
  divisions = soc.getDivisions()

  xImg = 10; xTxt =  315
  rankMap = {'asst':'Asst. Prof.', 'assoc':'Assoc. Prof.', 'full':'Professor',
             'lecturer':'Lecturer', 'slecturer':'Senior Lecturer', 
             'pop':'Prof. of Practice'}

  divisionMap = {'CS':'computer science','HCC':'human-centered computing',
                 'VC':'visual computing','FOI':'faculty of instruction'}

  caiSurface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                         int(normWidth * pixelScale), 122)
  ctx = cairo.Context(caiSurface)
  ctx.scale(pixelScale, pixelScale)

  ps = caiSurface

  cr = cairo.Context(ps)
  s = .38
  cr.scale(s,s)
  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)

  for division in divisions:
  
    cr.set_font_size(40)
    divFaculty = soc.getFacultyRankExtraByDivision(division)
  
    print("divFaculty:", str(division), str(divFaculty))
  
    idx = 0; 
    for faculty in divFaculty:
      ctx.rectangle(0, 0, normWidth, 122)
      ctx.set_source_rgb(0.6, 0.3, 0)
      ctx.fill()

      ctx.rectangle(0, 0, normWidth, normHeight)
      #ctx.set_source_rgb(0.9, 0.9, 1)
      cm = cmap[division]
      r,g,b,a = colors[cm]
      ctx.set_source_rgb(r,g,b,a)
      ctx.fill()

      yTxtOrig = yTxt  = 60;   dyTxt = 325
      yImgOrig = yImg  = 335;  dyImg = 325

      name, rank, extraRole = faculty
      cr.set_source_rgba(0.8, 0.6, 0, .1)

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
        g3 = .35; cr.set_source_rgb(g3,g3,g3)
        cr.show_text(rankMap[rank])
  
      if extraRole != None:
        cr.move_to(xTxt, yTxt+160)
        cr.set_source_rgb(.4, .2, 0)
        cr.show_text(extraRole)
  
      yTxt += dyTxt;    idx += 1
  
      imageFn = name2image(name)
      try:
        imgSurf  = cairo.ImageSurface.create_from_png(imageFn)
        cr.set_source_surface(imgSurf, xImg, yImg - dyImg)
        cr.paint()
      except: print("ignoring image:", imageFn); traceback.print_exc()
  
      idx += 1; yImg += dyImg

      cr.show_page()
      targFn = "images/soc/tiles/" + lastName + ".png"
      ps.write_to_png(targFn)
        
if __name__ == "__main__":    
  main()

### end ###

