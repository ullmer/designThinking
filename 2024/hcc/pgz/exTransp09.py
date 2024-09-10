# Simple animation against (on MS Windows) transparent window
# Brygg Ullmer, Clemson University
# Begun 2024-08-26

import sys; sys.path.append("..")

WIDTH, HEIGHT = 300, 300

from functools         import partial
from enoWinMgr         import *
from enoTranspWinDance import *

################## example transparency 09 ##################

class exTransp09(enoTranspWinDance): 

  def subwinAnimBounce(self, whichSubwin, nextDest, subsequentDest):
    cb = partial(self.subwinAnimBounce, whichSubwin, subsequentDest, nextDest) #callback on completion
    animate(whichSubwin, pos=nextDest, tween=self.tween, duration=self.dur1, on_finished=cb)

  def firstFrame(self): # invoked on rendering of first frame
    super().firstFrame()

    for winId in [1, 2]:
      w      = self.getWinCoordProxies(winId)
      x1, y1 = w.pos
      x2, y2 = x1 + 1700, y1

      cb = partial(self.subwinAnimBounce, w, (x1, y1), (x2, y2)) #callback on animation completion
      animate(w, pos=(x2, y2), tween=self.tween, duration=self.dur1, on_finished=cb)

################## main ##################
  
ewm = enoWinMgr()
et9 = exTransp09(ewm=ewm)

def draw(): et9.draw() #requires invocation via pgzrun, per its ~simplification of scope
  
### end ###

