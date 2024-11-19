# Enodia keyword comparison
# Brygg Ullmer, Clemson University
# Begun 2024-07-08

import yaml, traceback
import spacy
import csv
import heapq

class enoKwCompare:

  #categoriesYfn = 'kw_jelle2.yaml'
  categoriesYfn = 'kw_jb1.yaml'
  categoriesYfd = None

  categoryList       = None
  cats2primaryKws    = None
  cats2primaryKwsNlp = None

  cats2entries       = None
  nlp                = None

  def err(self, msg): print("enoKwCompare: ", msg)

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor 

    self.nlp = spacy.load("en_core_web_lg")  # Load a medium-sized language model
    self.loadCategories()

  ############## load categories ##############

  def loadCategories(self):
    try:
      yf = open(self.categoriesYfn)
      self.categoriesYfd = yaml.safe_load(yf)
      yf.close()
    except:
      self.err("loadCategories exception:")
      traceback.print_exc(); return None

    self.categoryList       = []
    self.cats2primaryKwsNlp = {}

    for category in self.categoriesYfd:
      self.categoryList.append(category)
      primaryKws = self.categoriesYfd[category]

      self.cats2primaryKwsNlp[category] = self.genNlpBundle(primaryKws)
  
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

  def procKwCsv(self, kwCsvFn):

    self.cats2entries = {}
    for cat in self.categoryList:
      self.cats2entries[cat] = {}

    try:
      f  = open(kwCsvFn, 'rt')
      cr = csv.reader(f)
      for row in cr:
        id, kw, count = row

        cat = self.compareKw2Cats(kw)
        self.cats2entries[cat][kw] = count
        
    except:
      self.err("procKwCsv exception")
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
 
  kws = ['storytelling', 'play', 'gesture', 'craft', 'capacitive sensing', 'NFC tag', 'tangible user interface']

  ekwc = enoKwCompare()

  #for kw in kws:
  #  cat = ekwc.compareKw2Cats(kw)
  #  print("%s\t%s" % (kw, cat))

  ekwc.procKwCsv('tei-kw.csv')
  #ekwc.procKwCsv('tei-kw500.csv')
  ekwc.tallyCatsYaml()

### end ###
