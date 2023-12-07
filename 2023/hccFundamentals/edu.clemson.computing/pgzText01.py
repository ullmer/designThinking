# https://pygame-zero.readthedocs.io/en/stable/ptext.html
# https://pythonprogramming.altervista.org/pygame-4-fonts/

WIDTH=600
HEIGHT=600

def draw(): 
  rect1  = Rect((0, 0), (180, 30))
  color1 = (0, 0, 130)
  screen.draw.filled_rect(rect1, color1)
  screen.draw.text("hello world", (0,0), fontsize=48, color="#bbbbbb", alpha=.8)

#    color="#AAFF00", gcolor="#66AA00", ocolor="black", alpha=0.8)
#midbottom=(427,460), width=360, fontname="Oswald", fontsize=48,

### end ###
