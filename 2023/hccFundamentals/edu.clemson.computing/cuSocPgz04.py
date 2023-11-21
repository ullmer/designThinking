#Clemson University School of Computing faculty interaction
#Brygg Ullmer, Clemson University
#Begun 2022-01-24

from enoElements import *
from enoDb       import *
from enoButton   import *

import traceback, sys

TITLE = "Clemson Computing people"
#WIDTH = 1920; HEIGHT = 1080
WIDTH = 1400; HEIGHT = 850

sqliteDbFn   = 'soc.db3'
queriesYFn   = 'soc-queries.yaml'
soc = enoDb(sqliteDbFn, queriesYFn)

global ba1 
baText = ['CECAS', 'AAH', 'SCIENCE']
ba1 = enoButtonArray(baText, buttonDim=(150, 30), dx=160)

divisions = soc.getDivisions([])
names     = []

divisionNames = {}

for division in divisions:
  divFaculty = soc.getFacultyRankExtraLByDivision(division)
  divisionNames[division] = []

  for faculty in divFaculty:
    lastName, rank, extraRole = faculty
    names.append(lastName)
    divisionNames[division].append(lastName)

people = enoElements(names)

numNames  = len(names); halfNames = int(numNames / 2)
firstHalf = names[0:halfNames]; secondHalf = names[halfNames:]
clusterDict1 = {}
clusterDict1['first'] = firstHalf; clusterDict1['last'] = secondHalf

clusterDict2 = {}; clusterDict2['all'] = names

clusters1 = enoElClusters(clusterDict1) #;cluster1.printSummary()
clusters2 = enoElClusters(clusterDict2)
clusters3 = enoElClusters(divisionNames)

people.addCluster(clusters1)
people.addCluster(clusters2)
people.addCluster(clusters3)

people.animToClusters(clusters1)
clock.schedule_interval(people.animNextCluster, 2)

def on_mouse_down(pos):      
  global people; people.on_mouse_down(pos)
  global ba1;    ba1.on_mouse_down(pos)

def on_mouse_move(pos, rel): global people; people.on_mouse_move(pos, rel)
def on_mouse_up(pos):        global people; people.on_mouse_up()
def draw():                  
  global people; screen.clear(); people.draw()
  global ba1; ba1.draw(screen)

### end ###
