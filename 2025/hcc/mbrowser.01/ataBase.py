# Animist Tangible Allomorphs Base class
# Brygg Ullmer, Clemson University
# Begun 2025-07-09

import traceback

########## animist tangible allomorphs domain ##########

class AtaBase:
  verbose  = True

  ########## message ##########
  def msg(self, mstr: str): 
    mstr2 = self.getClassName() + ' msg: ' + str(mstr); print(mstr2)

  def getClassName(self): return self.__class__.__name__

  ########## error ##########
  def err(self, estr: str):
    estr2 = self.getClassName() + ' err: ' + str(estr); print(estr2)
    traceback.print_exc(); 

########## main ##########
if __name__ == "__main__":
  ab = AtaBase()
  ab.msg("hello world")

### end ###
