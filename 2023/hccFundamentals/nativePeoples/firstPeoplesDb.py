# Garden database probe
# By Brygg Ullmer, Clemson University
# Begun 2023-06-09
# Revamped 2023-09-17

import sqlite3
import pandas as pd
import traceback
import yaml
from itertools import islice

################################################################################
############### Garden class ############### 

class gardenDb:
  wpDbFn         = 'sdowi.db3'
  gardenDbFn     = 'garden.db3'
  wpDbConn       = None
  wpDbCursor     = None
  gardenDbConn   = None
  gardenDbCursor = None
  verbose        = False
  fOut           = None
  currentYear    = 2023
  statesYamlFn   = 'states.yaml'
  statesY          = None
  stateName2Abbrev = None
  fnOut            = 'players1b.yaml'
  scyfn            = 'bb6.yaml'
  wpLinkCountDict  = None

  ############### constructor ############### 

  def __init__(self):
    #self.gardenDbConn   = sqlite3.connect(self.gardenDbFn)
    #self.gardenDbCursor = self.gardenDbConn.cursor()

    self.wpDbConn       = sqlite3.connect(self.wpDbFn)
    self.wpDbCursor     = self.wpDbConn.cursor()

    #self.fOut           = open(self.fnOut, 'wt')

    self.wpLinkCountDict = {}

  ############### get garden plant links ############### 

  def getGardenPlantLinks(self):

    linksStr = self.getGardenPlantLinksStr()

    ilinks = []
    for link in links: ilinks.append(int(link))

    return ilinks

  ############### splitListSublists ############### 

  def splitListSublists(self, targetlist, maxlenSublists):

    targListLen = len(targetlist)
    div = int(targListLen / maxlenSublists)
    rem = targListLen % maxlenSublists
    sublistLengths = [maxlenSublists] * div + [rem]

    #next two lines apply magic from here:
    #https://www.geeksforgeeks.org/python-split-a-list-into-sublists-of-given-lengths/

    targetlistIter = iter(targetlist)
    result = [list(islice(targetlistIter, n)) for n in sublistLengths]
    return result

  ############### get garden plant links ############### 

  def getGardenPlantLinksStr(self):

    query1 = "select outgoing_links from links where id = 334173;"
    try:    df = pd.read_sql_query(query1, self.wpDbConn) 
    except: print("gardenDb::getGardenPlantLilnks error"); traceback.print_exc(); return None

    ilinks = []

    for index, row in df.iterrows():
      linkstr = row['outgoing_links']
      links = linkstr.split('|')
      return links

  ############### get page names ############### 

  def getPageNames(self, links):
    #print('gpn:', links)
    #query1 = "select id, title from pages where id in [%s]" % ','.join(links)

    linkSublists = self.splitListSublists(links, 25) #

    pageNames = []

    for links in linkSublists:
      query1 = "select title from pages where id in (%s);" % (','.join(links))
      #print(query1)

      try:    df = pd.read_sql_query(query1, self.wpDbConn) 
      except: print("gardenDb::getPageNames error"); traceback.print_exc(); return None
  
      for index, row in df.iterrows():
        #id, title = row['id'], row['title']
        title = row['title']
        pageNames.append(title)

    return pageNames

  ########### extract a list of specified fields from a dictionary ############

  def getFields(self, dictionary, fields):
    result = []
    for fieldName in fields:
      fieldVal = dictionary[fieldName]
      result.append(fieldVal) 

    return result

  ########### load state abbreviations ############

  def loadStateAbbrevs(self):
    self.stateName2Abbrev = {}

    try:
      f = open(self.statesYamlFn, 'rt')
      self.statesY = yaml.safe_load(f)
      f.close()
     
      for stateAbbrev in self.statesY:
        stateName = self.statesY[stateAbbrev]
        self.stateName2Abbrev[stateName] = stateAbbrev

    except:
      print("problem in loadStateAbbrevs:", traceback.print_exc())

  ########### get abbrev state ############

  def getAbbrevState(self, birthState):
    if self.statesY == None:  self.loadStateAbbrevs()

    if birthState in self.stateName2Abbrev:
      abbrev = self.stateName2Abbrev[birthState]
      return abbrev.lower()

    return birthState
 
####################################
############### main ############### 

def main():
  gdb       = gardenDb()
  links     = gdb.getGardenPlantLinksStr()
  pagenames = gdb.getPageNames(links)
  for name in pagenames: print(name)

if __name__ == "__main__":
  main()

### end ###
