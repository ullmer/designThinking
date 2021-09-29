# Wrapper for Clemson SoC example 
#   faculty + research interests SQLite database 
# By Brygg Ullmer, Clemson University
# Begun 2021-09-20

# This support functionality engages SQLite3 database soc.db3
# This database draws from two YAML files:
#    soc-faculty.yaml  soc-research-categories.yaml
# and SQL tables described in: soc-defs.sql
# ... and is synthesized by Python3 code procSoC1.py 

import sqlite3, yaml

try: import pandas as pd # this has particular value for Jupyter use
except: print("pandas not found; working around")

################################################################################
############### School of Computing faculty/research areas class ############### 

class socDb:
  sqliteDbFn = 'soc.db3'
  queriesYFn = 'soc-queries.yaml'
  queriesY   = None
  dbConn     = None
  dbCursor   = None
  verbose    = False
  usePandas  = False

############### School of Computing faculty/research areas class ############### 

  def __init__(self):
    self.dbConn   = sqlite3.connect(self.sqliteDbFn)
    self.dbCursor = self.dbConn.cursor()
    self.loadYamlQueries(self.queriesYFn)

############### load YAML queries ###############

  def loadYamlQueries(self, yamlFn):
    yf       = open(yamlFn, "r+t")
    queriesY = yaml.safe_load(yf)
    yf.close()

    print(queriesY)

############### show major research areas ###############

  def getMajorResearchAreas(self):
    query = """select ra.name from researchArea as ra, 
               researchAreaRelation as rar 
               where rar.parentID = 0 and ra.id = rar.childID;"""
    rresult = self.execSqlQuery(query); result = []
    for entry in rresult: result.append(entry[0])
    return result

############### exec sql query ############### 

  def execSqlQuery(self, query):
    result = []
    for row in self.dbCursor.execute(query):
      result.append(row)

    return result

####################################
############### main ############### 

def main():
  soc = socDb()
  halfline = "=" * 20
  print(halfline, "major research areas", halfline)
  print(soc.showMajorResearchAreas())

  print("\n", halfline, "HCC subfields, default ordering", halfline)
  print(soc.showResearchFields('Human-Centered Computing'))
  
  print("\n", halfline, "HCC subfields, custom ordering", halfline)
  print(soc.showResearchFieldsOrdered('Human-Centered Computing', "f.division,f.lastName"))

if __name__ == "__main__":
  main()

### end ###
