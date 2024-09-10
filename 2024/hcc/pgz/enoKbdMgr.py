# Enodia keyboard manager 
# Brygg Ullmer, Clemson University
# Begun 2024-09-10

############### enodia keyboard manager ############### 

class enoKbdMgr:
  registeredKeys = None

  kbShortcuts = {1: 'ta49012', 2: 'arl', 3: 's123456789', 4: 'shj}

  ############### constructor ############### 

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
  
    self.registeredKeys = {} #dictionary

 ############### on key down ############### 

 def on_key_down(key): 
   if key in self.registeredKeys:
   if key == keys.S:   eba2.toggleButtonIdx(1); print('store mode')
   if key == keys.L:   eba2.toggleButtonIdx(2); print('load  mode')

   if key.name.startswith('K_') and key.name[2].isdigit():
     digit = ord(key.name[2]) - ord('0')
     eba3.toggleButtonIdx(digit)

 ############### on key up ############### 

 def on_key_up(key): pass

### end ###
