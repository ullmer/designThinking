# Example integrating in-class menu example and earlier Cairo PDF code
# Brygg Ullmer, Clemson University
# Begun 2021-10-14

import yaml
from PIL import Image
import cairo, traceback

yfn = 'smna-m5.yaml'
yf  = open(yfn, 'r+t')
yd  = yaml.safe_load(yf)

#print(yd)
categories = yd.keys()
print(categories)

# https://zetcode.com/gfx/pycairo/backends/
# https://zetcode.com/gfx/pycairo/images/
# https://zetcode.com/gfx/pycairo/shapesfills/
# https://zetcode.com/gfx/pycairo/transparency/
# https://pycairo.readthedocs.io/en/latest/reference/surfaces.html

xImg = 10; xTxt =  315

ps = cairo.PDFSurface("readMenu04.pdf", 2700, 800)
cr = cairo.Context(ps)
s = .38

cr.scale(s,s)

#http://www.mitsitamcafe.com/content/menus.asp

cr.set_font_size(180)
cr.move_to(10,200)
cr.set_source_rgb(.6, .4, 0)
cr.show_text('Mitsitam Native Foods Cafe Menu')

yTxtOrig = yTxt  = 400; dyTxt = 100; dxTxt = 1500
yImgOrig = yImg  = 680; dyImg = 325; endY  = 2000

for category in categories:

  cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                               cairo.FONT_WEIGHT_BOLD)
  cr.set_font_size(80)
  cr.move_to(xTxt-300, yTxt-80)
  cr.set_source_rgb(.5, .3, 0)
  cr.show_text(category)       
  yTxt += dyTxt
  
  if yTxt > endY: yTxt = yTxtOrig; xTxt += dxTxt

  categoryEntries = yd[category]
  lastMain = None
  for entry in categoryEntries:
    mainDish = entry['main']
    if mainDish != lastMain:
      print(mainDish); lastMain = mainDish #ignoring side subentries for present

    cr.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_NORMAL)

    cr.set_font_size(50)
    cr.move_to(xTxt-300, yTxt-80)
    cr.set_source_rgb(.5, .3, 0)
    cr.show_text(mainDish)
    yTxt += dyTxt

    if yTxt > endY: yTxt = yTxtOrig; xTxt += dxTxt
  
cr.show_page()

### end ###
