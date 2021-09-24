#https://www.pythoninformer.com/python-libraries/pycairo/text/

import cairo

WIDTH = 3
HEIGHT = 2
PIXEL_SCALE = 200

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             WIDTH*PIXEL_SCALE,
                             HEIGHT*PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0.8, 0.8, 1)
ctx.fill()

# Drawing code
ctx.set_source_rgb(1, 0, 0)
ctx.set_font_size(0.25)
ctx.select_font_face("Arial",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_NORMAL)
ctx.move_to(0.5, 0.5)
ctx.show_text("Drawing text")
# End of drawing code

surface.write_to_png('exCairo1.png')    

### end ###
