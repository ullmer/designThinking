# First Peoples database probe
# By Brygg Ullmer, Clemson University
# Begun    2023-06-09; first revamped 2023-09-17
# Revamped 2023-11-23

import sqlite3
import pandas as pd
import traceback
import yaml
from itertools import islice

###################################################
############### First Peoples class ############### 

class firstPeoplesDb:
  wpDbFn               = 'sdowi.db3'
  firstPeoplesDbFn     = 'firstPeoples.db3'
  wpDbConn             = None
  wpDbCursor           = None
  firstPeoplesDbConn   = None
  firstPeoplesDbCursor = None
  verbose              = False
  fOut                 = None
  currentYear          = 2023
  statesYamlFn         = 'states.yaml'
  statesY              = None
  stateName2Abbrev     = None
  fnOut                = 'firstPeoples.yaml'
  wpLinkCountDict      = None

  ############### constructor ############### 

  def __init__(self):
    #self.firstPeoplesDbConn   = sqlite3.connect(self.firstPeoplesDbFn)
    #self.firstPeoplesDbCursor = self.firstPeoplesDbConn.cursor()

    self.wpDbConn       = sqlite3.connect(self.wpDbFn)
    self.wpDbCursor     = self.wpDbConn.cursor()

    #self.fOut           = open(self.fnOut, 'wt')

    self.wpLinkCountDict = {}

  ############### get firstPeoples  links ############### 

  def getFirstPeoplesLinks(self):

    linksStr = self.getFirstPeoplesLinksStr()

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

  ############### get firstPeoples links ############### 

  def getFirstPeoplesLinksStr(self, titleStr):

    query1 = """select links.outgoing_links as outlinks,
                       links.id             as linksid,
                       pages.id    as pid,
                       pages.title as ptitle
                         from links, pages
                           where ptitle = '%s' and
                                    pid = linksid;""" % titleStr

    try:    df = pd.read_sql_query(query1, self.wpDbConn) 
    except: print("firstPeoplesDb::getFirst PeoplesLilnks error"); traceback.print_exc(); return None

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
      except: print("firstPeoplesDb::getPageNames error"); traceback.print_exc(); return None
  
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
  fpdb      = firstPeoplesDb()
  links     = fpdb.getFirstPeoplesLinksStr('Indigenous_peoples_of_California')
  pagenames = fpdb.getPageNames(links)
  for name in pagenames: print(name)

if __name__ == "__main__":
  main()

### end ###
