# Warming up on specific enoButtonArray variants
# Brygg Ullmer, Clemson University
# Begun 2024-09-09

WIDTH, HEIGHT = 800, 800

from enoButtonArray import *

bd        = (70, 40)  #button dimension
bdx       = 75        #x offset between buttons
bp1       = (50, 25)  #button array 1 base position
bp2       = (50, 730) #button array 3 base position
bp3       = (50, 775) #button array 2 base position

bd1Labels   = ['time', 1920, 1940, 1980, 1990, 2000, 2010, 2010, 2020]
bd2Labels   = ['action', 'recall', 'load']
bd3Labels   = ['slot'] + list(range(1,10))
bd4Labels   = ['code', 'homels1', 'homels2', 

kbShortcuts = {1: 'ta49012', 2: 'arl', 3: 's123456789', 4: 'shj}

eba1 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd1Labels, basePos=bp1)
eba2 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd2Labels, basePos=bp2, maxOneToggledOn=True)
eba3 = enoButtonArray(buttonDim=bd, dx=bdx, labelArray=bd3Labels, basePos=bp3, maxOneToggledOn=True)

headerColor = (50, 50, 50)
for ba in [eba1, eba2, eba3]: ba.getButtonIdx(0).bgcolor1 = headerColor

drawables  = [eba1, eba2, eba3]

def draw(): 
  screen.clear(); 
  for drawable in drawables:  drawable.draw(screen)

def on_mouse_down(pos):          
  for touchable in drawables: touchable.on_mouse_down(pos)

def on_key_down(key): #initially hardwired; sigh
   if key == keys.S:   eba2.toggleButtonIdx(1); print('store mode') 
   if key == keys.L:   eba2.toggleButtonIdx(2); print('load  mode')

   if key.name.startswith('K_') and key.name[2].isdigit():
     digit = ord(key.name[2]) - ord('0')
     eba3.toggleButtonIdx(digit)

### end ###
