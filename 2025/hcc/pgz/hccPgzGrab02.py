# Example parsing class reading list
# Brygg Ullmer, Clemson University
# Begun 2024-09-05

from hccReadingsPg  import *
import sys, time

#WIDTH, HEIGHT = 1200, 800
WIDTH, HEIGHT = 335, 94

hrpg = HccReadingsPg(x0=0, y0=0)

numReadings= hrpg.getNumReadings()
print("num readings:", numReadings)

def draw(): 
  screen.clear()
  hrpg.moveActorOffscreen(0)
  hrpg.draw(screen)
  return

  for i in range(numReadings):
    time.sleep(1.)
    print("FOO" + str(i))
    screen.clear()
    if i>0: hrpg.moveActorOffscreen(i-1)
    hrpg.moveActorHome(i)
    hrpg.draw(screen)
    strN = str(i).zfill(2)
    pygame.image.save(screen.surface, "tiles/t%s.png" % strN)
  sys.exit(1)

### end ###
