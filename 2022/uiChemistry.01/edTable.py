# Brygg Ullmer and Miriam Konkel
# Support class for engaging periodic table of the elements
# Clemson University
# Begun 2022-10-26

import yaml

#ed prefix = Enodia Data 
  
######################################################################### 
#################### Enodia Data : Periodic Table #################### 

class edPerTable:
  yamlFn   = 'pubchemNcbiNlmNihElements.yaml'
  yamlD    = None
  yamlHash = None

dimensions
rows
spdFPadding
tlBrPadding
imgPath
tables

  verbose = False

  #################### load data ####################

  def loadData(self):
    yamlF      = open(yamlFn, 'rt')
    self.yamlD = yaml.safe_load(yamlF)

    els = self.getElementList()
  
  #################### constructor ####################

  def __init__(self):
    self.elementFullnameHash = {}
    self.loadData()
    self.buildSymbolCoordHash()
    self.buildBlockHash()

  #################### getElementList ####################

  def getElementList(self):
    if self.elementFullnames != None:
      return self.elementFullnames

    if self.elementData == None:
      self.loadData()

    self.elementFullnames = self.elementData["order"]
    return self.elementFullnames

  #################### getElementByFullname ####################

  def getElementByFullname(self, elementFullname):
    if self.elementData == None:
      self.loadData()

    if elementFullname in self.elementFullnameHash:
      result = self.elementFullnameHash[elementFullname]
      return result

    if elementFullname in self.elementData:
      self.elementFullnameHash[elementFullname] = self.elementData[elementFullname]
      return self.elementFullnameHash[elementFullname]

    return None # error message would be preferable

  #################### get elements by row, column####################

  def getElsByRow(self, targRow):
    if targRow not in self.elementRowHash:
      if self.verbose:
        print("edElements: getElsByRow: targRow not in elementRowHash")
      return None

    els = self.elementRowHash[targRow]
    return els

  def getElsByCol(self, targCol):
    if targCol not in self.elementColHash:
      if self.verbose:
        print("edElements: getElsByCol: targColnot in elementColHash")
      return None

    els = self.elementColHash[targCol]
    return els

  #################### buildSymbolHash ####################

  #################### buildSymbolHash ####################

  def buildSymbolCoordHash(self):
    elFullnames = self.getElementList()
    self.elementSymbolHash = {}
    self.elementRowHash    = {}
    self.elementColHash    = {}
    self.elementNumIdHash  = {}
    self.elementTable      = {} # to become 2D hash by integer index
    self.elementFullSymbolHash = {}
    self.elementFullNumIdHash  = {}

    for elFullname in elFullnames:
      elData = self.getElementByFullname(elFullname)
      elSymbol = elData["symbol"]
      xpos     = elData["xpos"]
      ypos     = elData["ypos"]
      numId    = elData["number"]
      #if elFullname == 'lanthanum': print('FOO',xpos,ypos)

      self.elementSymbolHash[elSymbol]       = elFullname
      self.elementNumIdHash[numId]           = elFullname
      self.elementFullSymbolHash[elFullname] = elSymbol
      self.elementFullNumIdHash[elFullname]  = numId

      if ypos not in self.elementRowHash:
        self.elementRowHash[ypos] = []
      self.elementRowHash[ypos].append(elFullname)

      if xpos not in self.elementColHash:
        self.elementColHash[xpos] = []
      self.elementColHash[xpos].append(elFullname)

      if xpos not in self.elementTable:
        self.elementTable[xpos] = {}

      self.elementTable[xpos][ypos] = elFullname
      #if elFullname == 'lanthanum': print('BAR',elFullname)

  #################### getElementBySymbol####################

  def getElementByTableIdx(self, x, y):
    if self.elementTable == None:
      print("edElements getElementByTableIdx error: no elementTable")

    if x not in self.elementTable:    return None
    if y not in self.elementTable[x]: return None
    return self.elementTable[x][y]
  
  #################### get symbol by fullname ####################

  def getSymbolByFullname(self, fullname):
    if fullname in self.elementFullSymbolHash:
      return self.elementFullSymbolHash[fullname]
    return None

  #################### get id by fullname ####################

  def getIdByFullname(self, fullname):
    if fullname in self.elementFullNumIdHash:
      return self.elementFullNumIdHash[fullname]
    return None

  #################### getElementBySymbol####################

  def getElementBySymbol(self, elementSymbol):
    if self.elementData == None:
      self.loadData()

    if elementFullname in self.elementFullnameHash:
      result = self.elementFullnameHash[elementFullname]
      return result

    if elementFullname in self.elementData:
      self.elementFullnameHash[elementFullname] = self.elementData[elementFullname]
      return self.elementFullnameHash[elementFullname]

    return None # error message would be preferable

  #################### get maximum table width (from double-hash) ####################

  def getMaxTableHeight(self):
    maxTableHeight = 0
    xkeys = self.elementTable.keys()
    for x in xkeys:
      ykeys = self.elementTable[x]
      ylen  = len(ykeys)
      if ylen > maxTableHeight: maxTableHeight = ylen
    return maxTableHeight
  
  #################### get maximum table width (from double-hash) ####################

  def getMaxTableWidth(self):
    maxTableWidth = 0
    xkeys = self.elementTable.keys()
    for x in xkeys:
      if x > maxTableWidth: maxTableWidth = x
    return maxTableWidth

  #################### get maximum table width (from double-hash) ####################

  def getTableDimensions(self):
    tableWidth  = self.getMaxTableWidth()
    tableHeight = self.getMaxTableHeight()
    return [tableWidth, tableHeight]

  #################### get maximum table width (from double-hash) ####################

  def getFullnameMatrix(self):
    tableDimensions = self.getTableDimensions()
  
    table = []
    for x in range(1,tableDimensions[0]):
      row = []
      for y in range(1,tableDimensions[1]):
        elFullname = self.getElementByTableIdx(x, y)
        row.append(elFullname)
      table.append(row)
    return table

  #################### get maximum table width (from double-hash) ####################

  def getSymbolMatrix(self):
    tableDimensions = self.getTableDimensions()
  
    table = []
    for x in range(1,tableDimensions[0]):
      row = []
      for y in range(1,tableDimensions[1]):
        elFullname = self.getElementByTableIdx(x, y)
        elSymbol   = self.getSymbolByFullname(elFullname)
        row.append(elSymbol)
      table.append(row)
    return table

  #################### getFullnameByIdRange ####################
  def getFullnameByIdNumRange(self, minIdNum, maxIdNum):
    result = []
    for idx in range(minIdNum, maxIdNum):
      fullname = self.elementNumIdHash[idx]
      result.append(fullname)
    return result

  #################### build block hash ####################
  def getBlockId(self, blockId):
    if blockId not in self.elementBlockIdHash: 
      print("edElements getBlock: blockId not in elementBlockIdHash")
      return None
    return self.elementBlockIdHash[blockId]

  #################### build block hash ####################
  # https://en.wikipedia.org/wiki/Periodic_table#Blocks

  def buildBlockHash(self):
    self.elementBlockIdHash   = {}
    self.elementBlockNameHash = {}
    for block in ['s', 'p', 'd', 'f']: 
      self.elementBlockIdHash[block] = [] # list for each block

    ### s-block ###
    self.elementBlockIdHash['s'] += self.getElsByCol(1)
    self.elementBlockIdHash['s'] += self.getElsByCol(2)
    self.elementBlockIdHash['s'].insert(1,'helium')

    ### p-block ###
    for idx in [21,39,71,103]:
      self.elementBlockIdHash['p'] += self.getFullnameByIdNumRange(idx, idx+10)

    ### d-block ###
    for idx in [5,13,31,49,81,113]:
      self.elementBlockIdHash['d'] += self.getFullnameByIdNumRange(idx, idx+6)

    ### f-block ###
    for idx in [57,89]:
      self.elementBlockIdHash['f'] += self.getFullnameByIdNumRange(idx, idx+14)

    for block in ['s', 'p', 'd', 'f']: 
      blockElements = self.getBlockId(block)
      for el in blockElements:
        self.elementBlockNameHash[el] = block

  #################### build block hash ####################
  def getBlockByElName(self, elName):
    if elName not in self.elementBlockNameHash: 
      if self.verbose:
        print("edElements getBlockByElName: elName not in elementBlockNameHash")
      return None
    return self.elementBlockNameHash[elName]
      
############################################## 
#################### main #################### 

def main():
  ed = edElements()
  print('>> Elements: ' + str(ed.getElementList()))
  print('>> Aluminum: ' + str(ed.getElementByFullname('aluminium')))
  print('>> Column 1: ' + str(ed.getElsByCol(1)))
  print('>> Table dimensions: ' + str(ed.getTableDimensions()))
  #print(ed.getFullnameMatrix())
  print('>> Symbol matrix: ' + str(ed.getSymbolMatrix()))
  print('>> Block S: ' + str(ed.getBlockId('s')))
  print('>> Block P: ' + str(ed.getBlockId('p')))
  print('>> Block D: ' + str(ed.getBlockId('d')))
  print('>> Block F: ' + str(ed.getBlockId('f')))

if __name__ == "__main__":
  main()

### end ###

