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
#import time
import random
import pygame
from pygame import time

try:
  import launchpad_py as launchpad
except ImportError:
  try:
    import launchpad
  except ImportError:
    sys.exit("error loading launchpad.py")

def main():

  mode = None

  if launchpad.Launchpad().Check( 0 ):  #TangViz default small
     lp = launchpad.Launchpad()
     if lp.Open( 0 ):
       print("Launchpad Mk1/S/Mini")
       mode = "Mk1"

  if mode is None:
    print("Did not find Launchpad...")
    return

  print("QUIT: Push a single button for longer than 3s and release it.")

  print( "\nRunning..." )
  print( " - Python " + str( sys.version.split()[0] ) )
  print( " - PyGame " + str( pygame.ver ) )

  # create an instance
  lp = launchpad.Launchpad()

  if launchpad.Launchpad().Check( 0 ):  #TangViz default, mini + large
    lp = launchpad.Launchpad()
    if lp.Open( 0 ):
      print("Launchpad Mk1/S/Mini")
      mode = "Mk1"
    
  else:
    print( " - No Launchpad available" )
    return

  # Clear the buffer because the Launchpad remembers everything
  #lp.ButtonFlush()

  # List the class's methods
  print( " - Available methods:" )
  for mName in sorted( dir(lp) ):
    if mName.find( "__") >= 0: continue
    if callable( getattr( lp, mName ) ): print( "     " + str( mName ) + "()" )

  # LedAllOn() test
  print( " - Testing LedAllOn()" )
  for i in [ 5, 21, 79, 3]:
    lp.LedAllOn( i )
    time.wait(500)
  lp.LedAllOn( 0 )

  # LedCtrlXY() test
  # -> LedCtrlRaw()
  #    -> midi.RawWriteSysEx()
  #       -> devOut.write_sys_ex()
  print( " - Testing LedCtrlXY()" )
  colors = [ [63,0,0],[0,63,0],[0,0,63],[63,63,0],[63,0,63],[0,63,63],[63,63,63] ]
  for i in range(4):
    for y in range( i + 1, 8 - i + 1 ):
      for x in range( i, 8 - i ):
        lp.LedCtrlXY( x, y, colors[i][0], colors[i][1], colors[i][2])
    time.wait(500)

  # turn all LEDs off
  print( " - Testing Reset()" )
  lp.Reset()

  # close this instance
  #print( " - More to come, goodbye...\n" )
  #lp.Close()

  lastBut = (-99,-99)
  tStart = time.time()
  while True:
    if mode == 'Pro' or mode == 'ProMk3': buts = lp.ButtonStateXY( mode = 'pro')
    else:                                 buts = lp.ButtonStateXY()

    if buts != []:
      print( buts[0], buts[1], buts[2] )

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
