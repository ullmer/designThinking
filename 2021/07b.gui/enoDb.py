# Wrapper for Clemson SoC example 
#   faculty + research interests SQLite database 
# By Brygg Ullmer, Clemson University
# Begun 2021-09-20

# This support functionality engages SQLite3 database soc.db3
# This database draws from two YAML files:
#    soc-faculty.yaml  soc-research-categories.yaml
# and SQL tables described in: soc-defs.sql
# ... and is synthesized by Python3 code procSoC1.py 

import sqlite3, yaml, traceback, functools

try: import pandas as pd # this has particular value for Jupyter use
except: print("pandas not found; working around")

################################################################################
############### Enodia sqlite wrappers class ############### 

class enoDb: #enodia database class
  sqliteDbFn   = None
  queriesYFn   = None
  queriesYFull = None #more expansive representation, including embedded sqliteDbFn 
  queriesY     = None #just the queries 
  queriesList  = None #list of queries
  queryStrs    = None
  queryArgs    = None
  queryResults = None
  dbConn       = None
  dbCursor     = None
  verbose      = False
  usePandas    = False

############### School of Computing faculty/research areas class ############### 

  def __init__(self, sqliteDbFn='soc.db3', queriesYFn='soc-queries.yaml'):
    self.sqliteDbFn = sqliteDbFn; self.queriesYFn = queriesYFn

    self.dbConn   = sqlite3.connect(self.sqliteDbFn)
    self.dbCursor = self.dbConn.cursor()
    self.loadYamlQueries(self.queriesYFn)

############### load YAML queries ###############

  def loadYamlQueries(self, yamlFn):
    yf           = open(yamlFn, "r+t")
    self.queriesYFull = yaml.safe_load(yf); yf.close()

    self.queryStrs    = {}
    self.queryArgs    = {}
    self.queryResults = {}

    try:    
      self.queriesY = self.queriesYFull['dbDescr']['queries']
      self.queriesList = self.queriesY.keys()
      for queryName in self.queriesList:
        queryFields = self.queriesY[queryName]

        queryStr, queryResults = queryFields['query'], queryFields['results']
        if 'arguments' in queryFields: queryArgs = queryFields['arguments']
        else:                          queryArgs = []
        self.constructPartialQuery(queryName, queryStr, queryArgs, queryResults)

    except: print("enoDb::loadYamlQueries error"); traceback.print_exc(); return 
    #print("Loaded queries from %s: %s" % (yamlFn, self.queriesList))
    #print(self.queriesY)

  ############### construct partial query ###############

  # note list of URLs consulted toward expression of partial queries below

  def constructPartialQuery(self, queryName, queryStr, queryArgs, queryResults):
    self.queryStrs[queryName]    = queryStr
    self.queryArgs[queryName]    = queryArgs
    self.queryResults[queryName] = queryResults

    if self.verbose: print("enoDb::constructPartialQuery:: constructing partial", queryName)
    p = functools.partial(self.queryWrapper, queryName)
    setattr(self, queryName, p) #this worked for me better than partialmethod

############### show major research areas ###############

  def queryWrapper(self, queryName, queryArgs):
    try: 
      queryStrTemplate = self.queryStrs[queryName]
      queryStr         = queryStrTemplate % queryArgs
      queryResults     = self.queryResults[queryName]
      numQueryResults  = len(queryResults)
      rresult = self.execSqlQuery(queryStr); result = []
      if numQueryResults == 1: 
        for entry in rresult: result.append(entry[0])
      else:                    
        for entry in rresult: result.append(entry)
      return result
    except: print("enoDb::queryWrapper error"); traceback.print_exc(); return None

############### exec sql query ############### 

  def execSqlQuery(self, query):
    result = []
    for row in self.dbCursor.execute(query):
      result.append(row)

    return result

####################################
############### main ############### 

def main():
  sqliteDbFn   = 'soc.db3'
  queriesYFn   = 'soc-queries.yaml'
  soc = enoDb(sqliteDbFn, queriesYFn)

  halfline = "=" * 20
  print("\n", halfline, "major research areas", halfline)
  print(soc.getMajorResearchAreas([]))

  print("\n", halfline, "HCC subfields, default ordering", halfline)
  print(soc.getResearchFields('Human-Centered Computing'))
  
  print("\n", halfline, "HCC subfields, custom ordering", halfline)
  print(soc.getResearchFieldsOrdered(('Human-Centered Computing', "f.division,f.lastName")))

if __name__ == "__main__":
  main()

# list of URLs consulted toward expression of partial queries: 
#https://stackoverflow.com/questions/16626789/functools-partial-on-class-method
#https://docs.python.org/3/library/functools.html#functools.partialmethod
#https://florian-dahlitz.de/articles/introduction-to-pythons-functools-module#partialmethod-the-partial-for-methods 
#https://betterprogramming.pub/python-reflection-and-introspection-97b348be54d8
#https://stackoverflow.com/questions/49662666/unable-to-call-function-defined-by-partialmethod
#https://stackoverflow.com/questions/41070352/usage-of-functool-partialmethod-and-functool-partial

  def constructPartialQuery(self, queryName, queryStr, queryArgs, queryResults):
    self.queryStrs[queryName]    = queryStr
### end ###
