# Wrapper for Clemson SoC example 
#   faculty + research interests SQLite database 
# By Brygg Ullmer, Clemson University
# Begun 2021-09-20

# This support functionality engages SQLite3 database soc.db3
# This database draws from two YAML files:
#    soc-faculty.yaml  soc-research-categories.yaml
# and SQL tables described in: soc-defs.sql
# ... and is synthesized by Python3 code procSoC1.py 

import sqlite3
import pandas as pd # this has particular value for Jupyter use

################################################################################
############### School of Computing faculty/research areas class ############### 

class socDb:
  sqliteDbFn = 'soc.db3'
  dbConn     = None
  dbCursor   = None
  verbose    = False

############### School of Computing faculty/research areas class ############### 

  def __init__(self):
    self.dbConn   = sqlite3.connect(self.sqliteDbFn)
    self.dbCursor = self.dbConn.cursor()

############### list all faculty ############### 

  def showFaculty(self):
    query = "select * from faculty";
    df = pd.read_sql_query(query, self.dbConn)
    return df

############### show major research areas ############### 

  def showMajorResearchAreas(self):
    query = "select ra.name from researchArea as ra, researchAreaRelation as rar \
               where rar.parentID = 0 and ra.id = rar.childID;"
    df = pd.read_sql_query(query, self.dbConn)
    return df

############### list all faculty ############### 

  def showFacultyRank(self, rank):
    query = "select * from faculty where rank='%s'" % rank;
    df = pd.read_sql_query(query, self.dbConn)
    return df

############### list all faculty ############### 

  def showFacultyRankDivision(self, rank, division):
    query = "select * from faculty where rank='%s' and division='%s'" % \
      (rank, division);
    df = pd.read_sql_query(query, self.dbConn)
    return df

############### show subarea ############### 

  def showResearchFields(self, subarea):
    query = \
     """select f.name, f.division, f.rank 
          from faculty as f, researchArea as ra, personResearchRelation as prr
          where ra.name = '%s' and 
                prr.raid = ra.id and prr.fid = f.id
          group by f.name order by f.rank, f.division""" % subarea
  
    df = pd.read_sql_query(query, self.dbConn)
    return df

############### show subarea, with custom ordering  ############### 

  def showResearchFieldsOrdered(self, subarea, orderList):
    if type(orderList) is not list:
       print("socDB::showResearchFieldsOrdered: 2nd arg orderList not passed as list!"); return None

    #orderList examples: [f.division, f.lastName] ; [f.rank, f.division]

    orderStr = ",".join(orderList) 

    query = """select f.name, f.division, f.rank 
                from faculty as f, researchArea as ra, personResearchRelation as prr
                where ra.name = '%s' and prr.id = ra.id and prr.id = f.id
                group by f.name order by %s""" % (subarea, orderStr)

    if verbose: print("socDB::showResearchFieldsOrdered query:", query)
  
    try:    df = pd.read_sql_query(query, self.dbConn); return df
    except: print("socDB::showResearchFieldsOrdered error")

####################################
############### main ############### 

def main():
  soc = socDb()
  halfline = "=" * 20
  print(halfline, "major research areas", halfline)
  print(soc.showMajorResearchAreas())

  print("\n", halfline, "HCC subfields, default ordering", halfline)
  #print(soc.showResearchFields('Human-Centered Computing'))
  print(soc.showResearchFields('Human-Centered Computing'))

if __name__ == "__main__":
  main()

### end ###
