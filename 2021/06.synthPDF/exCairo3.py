# Integration of text and image examples, rendering to PDF
# Brygg Ullmer, Clemson University
# Begun 2021-09-22

# https://zetcode.com/gfx/pycairo/backends/
# https://stackoverflow.com/questions/7099630/create-pdf-with-resized-png-images-using-pycairo-rescaling-surface-issue

import cairo
from PIL import Image

def main():

    imgFn = 'images/computing2.png'
    imgF  = open(imgFn, 'r+b')
    
    ps = cairo.PDFSurface("exCairo2.pdf", 504, 648)
    cr = cairo.Context(ps)

    
    cr.set_source_rgb(0, 0, 0)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(40)
    
    cr.move_to(10, 50)
    cr.show_text("Forward ho.")
    cr.show_page()
        
        
if __name__ == "__main__":    
    main()

### end ###
