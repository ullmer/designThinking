#!/usr/bin/env python
#
# Quick button test.
# Works with these Launchpads: Mk1, Mk2, Mini Mk3, S/Mini, Pro, Pro Mk3
# And these:                   Midi Figther 64
# 
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys
import time
#import pygame
#from pygame import time

try:
  import launchpad_py as launchpad
except ImportError:
  try:
    import launchpad
  except ImportError:
    sys.exit("error loading launchpad.py")

def main():

  mode = None

  if launchpad.LaunchpadPro().Check( 0 ):
    lp = launchpad.LaunchpadPro()
    if lp.Open( 0 ):
      print("Launchpad Pro")
      mode = "Pro"

  elif launchpad.Launchpad().Check( 0 ):  #TangViz default small
     lp = launchpad.Launchpad()
     if lp.Open( 0 ):
       print("Launchpad Mk1/S/Mini")
       mode = "Mk1"

  if mode is None:
    print("Did not find any Launchpads...")
    return

  lp.ButtonFlush()

  lastBut = (-99,-99)
  tStart = time.time()
  while True:
    if mode == 'Pro' or mode == 'ProMk3': buts = lp.ButtonStateXY( mode = 'pro')
    else:                                 buts = lp.ButtonStateXY()

    if buts != []:
      print(buts[0], buts[1])
      lp.LedCtrlXY(int(buts[0]), int(buts[1]), 0, 0, 63)

      # quit?
      if buts[2] > 0:
        lastBut = ( buts[0], buts[1] )
        tStart = time.time()
      else:
        if lastBut == ( buts[0], buts[1] ) and (time.time() - tStart) > 2:
          break


  print("bye ...")

  lp.Reset() # turn all LEDs off
  lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

  
if __name__ == '__main__':
  main()

### end ###
#!/usr/bin/env python
#
# Launchpad tests for RGB-style variants Mk2, Mini Mk3, Pro, X ...
# 
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys

try:
  import launchpad_py as launchpad
except ImportError:
  try:
    import launchpad
  except ImportError:
    sys.exit("ERROR: loading launchpad.py failed")

import random
import pygame
from pygame import time


def CountdownPrint( n ):
  for i in range(n,0,-1):
    sys.stdout.write( str(i) + " ")
    SYs.stdout.flush()
    time.wait(500)


def main():

  # some basic info
  print( "\nRunning..." )
  print( " - Python " + str( sys.version.split()[0] ) )
  print( " - PyGame " + str( pygame.ver ) )

  # create an instance
  lp = launchpad.Launchpad()

  # try the first Mk2
  if lp.Check( 0, "mk2" ):
    lp = launchpad.LaunchpadMk2()
    if lp.Open( 0, "mk2" ):
      print( " - Launchpad Mk2: OK" )
    else:
      print( " - Launchpad Mk2: ERROR")
      return

  elif launchpad.Launchpad().Check( 0 ):  #TangViz default small
    lp = launchpad.Launchpad()
    if lp.Open( 0 ):
      print("Launchpad Mk1/S/Mini")
      mode = "Mk1"
    
  else:
    print( " - No Launchpad available" )
    return

  # Clear the buffer because the Launchpad remembers everything

  # turn all LEDs off
  print( " - Testing Reset()" )
  lp.Reset()

  # close this instance
  print( " - More to come, goodbye...\n" )
  lp.Close()

  
if __name__ == '__main__':
  main()

