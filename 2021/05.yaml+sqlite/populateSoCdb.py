# Populate SQLite database with Clemson 
# School of Computing research areas, drawing from two YAML defs
# Brygg Ullmer, Clemson University, 2021-09-16

import yaml, sqlite3
verbose = False #debugging output

yfn1 = 'soc-research-categories.yaml'
yfn2 = 'soc-faculty.yaml'

yf1  = open(yfn1, 'r+t');   yf2 = open(yfn2, 'r+t')
yd1  = yaml.safe_load(yf1); yd2 = yaml.safe_load(yf2) 

researchCategories = yd1.keys()
raPersonHash = {} #research area person hash

## work through research areas ##

divisions = yd2['divisions'].keys()
ranks     = yd2['rank'].keys()

dPersonHash = {} #divisions person hash
rPersonHash = {} #rank person hash

for division in divisions:
  personList = yd2['divisions'][division]
  for person in personList: dPersonHash[person] = division

for rank in ranks:
  personList = yd2['rank'][rank]
  for person in personList: rPersonHash[person] = rank

personList = dPersonHash.keys()
#print(personList)

#### populate base person record ####

peopleRecords = []; faculty2fidHash = {}; idx = 1
for person in personList:
  firstNameSpace = person.find(' ')
  firstName = person[0:firstNameSpace]
  lastName  = person[firstNameSpace+1:]
  if lastName[1] == '.': lastName = lastName[3:]

  if verbose: print('<%s> <%s>'%(firstName, lastName))

  division      = dPersonHash[person]
  rank = None;
  if lastName in rPersonHash: rank = rPersonHash[lastName]
  researchAreas = []
  if person in raPersonHash: researchAreas = raPersonHash[person]
  record = (idx, person, firstName, lastName, division, rank)
  peopleRecords.append(record); 
  faculty2fidHash[person] = idx; idx+=1

#https://pythonexamples.org/python-sqlite3-insert-multiple-rows-to-table/
conn = sqlite3.connect('soc.db3')
c = conn.cursor()
c.executemany('insert into faculty values(?,?,?,?,?,?);', peopleRecords);
conn.commit()

## work through research areas ##

raRecords = [];   raID = 1 #research area records, ID
rarRecords = []; rarID = 1 #research area relation records, ID
prrRecords = []; prrID = 1 #person research relation records, ID

# research area, researchAreaRelation, personResearchRelation 

for researchCategory in researchCategories:
  raRecords.append(   (raID, researchCategory)) # add a major research category
  rarRecords.append( (rarID, 0, raID))          # indicate that the parent is 0 ("root")
  categoryID = raID
  raID += 1; rarID += 1                         # increment the table record IDs

  fields    = yd1[researchCategory]
  numFields = len(fields)

  for field in fields:
    raRecords.append(  (raID, field))             # add a subfield research record
    rarRecords.append( (rarID, categoryID, raID)) # and link this to its parent category

    for faculty in fields[field]:
      if faculty not in raPersonHash: raPersonHash[faculty] = []
      raPersonHash[faculty].append(field)
      fid = faculty2fidHash[faculty] 
      prrRecords.append((prrID, raID, fid)) # relation between faculty and individual research field
      prrID += 1

      prrRecords.append((prrID, categoryID, fid)) # relation between faculty and research category
      prrID += 1

    raID += 1; rarID += 1                         # increment the table record IDs

c.executemany('insert into researchArea values(?,?);', raRecords);
conn.commit()

c.executemany('insert into researchAreaRelation values(?,?,?);', rarRecords);
conn.commit()

c.executemany('insert into personResearchRelation values(?,?,?);', prrRecords);
conn.commit()

conn.close()

### end ###
