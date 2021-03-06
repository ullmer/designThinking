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
  lp.ButtonFlush()

  # LedCtrlXY() test
  # -> LedCtrlRaw()
  #    -> midi.RawWriteSysEx()
  #       -> devOut.write_sys_ex()
  print( " - Testing LedCtrlXY()" )
  #colors = [ [63,0,0],[0,63,0],[0,0,63],[63,63,0],[63,0,63],[0,63,63],[63,63,63] ]
  c = [63,45,30,20,10,5,3,2,2]
  colors = []
  #for i in range(9): colors.append([0,0,int(63*(9-i)/9)])
  #for i in range(9): colors.append([0,0,c[i]])
  for i in range(9): colors.append([c[i],0,0])

  for i in range(9):
    for j in range(9):
      lp.LedCtrlXY(i,j, colors[i][0], colors[i][1], colors[i][2])
    time.wait(500)
  time.wait(2500)

  # turn all LEDs off
  print( " - Testing Reset()" )
  lp.Reset()

  # close this instance
  print( " - More to come, goodbye...\n" )
  lp.Close()

  
if __name__ == '__main__':
  main()

