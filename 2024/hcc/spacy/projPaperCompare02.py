# Enodia keyword comparison
# Brygg Ullmer, Clemson University
# Begun 2024-07-08

import yaml, traceback
import spacy
import csv
import heapq

class hcaiKwCompare:

  studentProjectsYfn = 'meta.yaml'
  iuiFn              = 'iuiEx.psv'
  studentProjectsYfd = None

  projTitles         = None
  projSummaries      = None

  categoryList       = None
  cats2primaryKws    = None
  cats2primaryKwsNlp = None
  cats2entries       = None
 
  iuiIds             = None
  iuiId2Txt          = None

  nlp                = None

  def err(self, msg): print("hcaiKwCompare: ", msg)

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor 

    self.nlp = spacy.load("en_core_web_lg")  # Load a medium-sized language model
    self.loadCategories()

  ############## load studentProjects ##############

  def loadCategories(self):
    ### Load class YAML file ###
    try: 
      yf = open(self.studentProjectsYfn)
      self.studentProjectsYfd = yaml.safe_load(yf)
      yf.close()
    except:
      self.err("loadCategories yaml exception:")
      traceback.print_exc(); return None

    ### Load IUI file ###
    try: 
      iuiF           = open(self.iuiFn, 'rt')
      rawlines       = iuiF.readlines()
      self.iuiId2Txt = {}
      self.iuiIds    = []

      for rawline in rawlines:
        cleanline = rawline.rstrip()
        id, txt = cleanline.split('|'); #print(id)
        self.iuiIds.append(id)
        self.iuiId2Txt[id] = txt
    except:
      self.err("loadCategories iuiF exception:")
      traceback.print_exc(); return None

    self.categoryList       = []
    self.cats2primaryKwsNlp = {}

    self.projTitles    = []
    self.projSummaries = []

    for entry in self.studentProjectsYfd:
      try:
        projTitle   = entry['projTitle']
        projSummary = entry['projSummary']
      except: print("problem processing entry:", entry)

      self.projTitles.append(   projTitle)
      self.projSummaries.append(projSummary)

    #for category in self.studentProjectsYfd:
    #  self.categoryList.append(category)
    #  primaryKws = self.studentProjectsYfd[category]
    #  self.cats2primaryKwsNlp[category] = self.genNlpBundle(primaryKws)
  
  ############## generate nlp bundle ##############

  def genNlpBundle(self, kwlist):
    result = []
    for pkw in kwlist:
      kwNlp = self.nlp(pkw)
      result.append(kwNlp)

    return result

  ############## compareKw2Cats ##############

  def compareKw2Cats(self, kw):
    kwNlp = self.nlp(kw)

    minSimilarity = None
    maxSimilarity = None

    minSimIdx = None
    maxSimIdx = None

    idx = -1

    for category in self.categoryList:
      idx += 1
      nlpBundle    = self.cats2primaryKwsNlp[category]
      similarities = []

      for el in nlpBundle: sim = kwNlp.similarity(el); similarities.append(sim)

      minSim = min(similarities)
      maxSim = max(similarities)
      #print("%s\t%f\t%f" % (category, minSim, maxSim))

      if minSimilarity is None:    minSimilarity=minSim; minSimIdx = idx
      elif minSim < minSimilarity: minSimilarity=minSim; minSimIdx = idx

      if maxSimilarity is None:    maxSimilarity=maxSim; maxSimIdx = idx
      elif maxSim > maxSimilarity: maxSimilarity=maxSim; maxSimIdx = idx

    #print("compareKw2Cats, kw=", kw)
    #print(minSimIdx, maxSimIdx)
    #print("minSim: ", minSimilarity, self.categoryList[minSimIdx])
    #print("maxSim: ", maxSimilarity, self.categoryList[maxSimIdx])
    #print("")
    return self.categoryList[maxSimIdx]

  ############# process kw csv #############

  def procKwPsv(self, kwPsvFn):

    self.cats2entries = {}
    for cat in self.categoryList:
      self.cats2entries[cat] = {}

    try:
      f  = open(kwPsvFn, 'rt')
      cr = csv.reader(f, delimiter='|')
      for row in cr:
        id, kw, count = row

        cat = self.compareKw2Cats(kw)
        self.cats2entries[cat][kw] = count
        
    except:
      self.err("procKwPsv exception")
      traceback.print_exc(); return None

  ############# tallyCats #############

  def tallyCats(self):

    eq = '='*20

    for cat in self.categoryList:
      cat1, cat2, cat3 = [], [], []
      catKws = self.cats2entries[cat]
      numCats = len(catKws.keys())

      print(eq, cat, eq)
      print("numCats:", numCats)

      kwCount = 0
      for kw in catKws: 
        try:    
           cnt = int(catKws[kw])
           catKws[kw] = cnt
           kwCount += cnt
           #print("%s\t%i" % (kw, cnt))

           if cnt   >= 10: cat1.append(kw)
           elif cnt >= 2:  cat2.append(kw)
           else:           cat3.append(kw)

        except: self.err("tallyCats" + kw + str(cnt))

      print("kwCount:", kwCount)
      print(">=10:", cat1)
      print("2..9:", cat2)
      print("   1:", len(cat3))

      #nl = heapq.nlargest(10, catKws)
      #for el in nl:
      #  count = catKws[el]
      #  if count>1: print(el, count)

  ############# tallyCats #############

  def tallyCatsYaml(self):

    for cat in self.categoryList:
      cat1, cat2, cat3 = [], [], []
      catKws = self.cats2entries[cat]
      numCats = len(catKws.keys())

      print(cat + ":")
      print("  numCats:", numCats)

      kwCount = 0
      for kw in catKws: 
        try:    
           cnt = int(catKws[kw])
           catKws[kw] = cnt
           kwCount += cnt
           #print("%s\t%i" % (kw, cnt))

           if cnt   >= 10: cat1.append(kw)
           elif cnt >= 2:  cat2.append(kw)
           else:           cat3.append(kw)

        except: self.err("tallyCats" + kw + str(cnt))

      print("  kwCount:", kwCount)
      print("  kwG10: ", cat1)
      print("  kwG2_9:", cat2)
      print("  kw1:   ", len(cat3))

############# main #############

if __name__ == "__main__":
 
  hkc = hcaiKwCompare()

  iid1 = hkc.iuiIds[0]
  iid2 = hkc.iuiIds[1]

  i1   = hkc.iuiId2Txt[iid1]
  i2   = hkc.iuiId2Txt[iid2]

  is1  = hkc.nlp(i1)
  is2  = hkc.nlp(i2)

  print(i1)
  print(i2)

  p1 = hkc.projSummaries[0]
  p2 = hkc.projSummaries[1]

  #p1 = hkc.projTitles[0]
  #p2 = hkc.projTitles[1]

  ps1  = hkc.nlp(p1)
  ps2  = hkc.nlp(p2)

  print(p1)
  print(p2)

  print(is1.similarity(ps1))
  print(is2.similarity(ps1))

  #for kw in kws:
  #  cat = ekwc.compareKw2Cats(kw)
  #  print("%s\t%s" % (kw, cat))

  #ekwc.procKwPsv('tei-kw.csv')
  #ekwc.procKwPsv('extract02.psv')
  #ekwc.procKwPsv('tei-kw500.csv')
  #ekwc.tallyCatsYaml()

### end ###
