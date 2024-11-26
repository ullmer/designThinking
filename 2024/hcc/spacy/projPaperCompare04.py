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

  iuiIds             = None
  iuiId2Txt          = None

  nlp                = None
  nlpModel           = "en_core_web_lg"

  def err(self, msg): print("hcaiKwCompare: ", msg)

  ############# constructor #############

  def __init__(self, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor 

    print("Loading spacy model", self.nlpModel)
    self.nlp = spacy.load(self.nlpModel)  # Load a large language model
    self.loadCategories()

  ############## load studentProjects ##############

  def loadCategories(self):
    ### Load class YAML file ###
    try: 
      yf = open(self.studentProjectsYfn)
      self.studentProjectsYfd = yaml.safe_load(yf)
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

    self.projTitles, self.projSummaries = [], []

    for entry in self.studentProjectsYfd:
      try:
        projTitle   = entry['projTitle']
        projSummary = entry['projSummary']
      except: print("problem processing entry:", entry)

      self.projTitles.append(   projTitle)
      self.projSummaries.append(projSummary)

############# main #############

if __name__ == "__main__":
 
  hkc = hcaiKwCompare()

  iuiNlpDb = {}; idx=0
  print("Analysing IUI corpus", end="", flush=True)

  for id in hkc.iuiIds: 
    titleKwTxt   = hkc.iuiId2Txt[id]
    iuiNlpDb[id] = hkc.nlp(titleKwTxt);   idx += 1
    if idx % 100 == 0: print(".", end="", flush=True)

  print("complete")
  numProjectEntries = len(hkc.projTitles)

  for i in range(numProjectEntries):
    pt = hkc.projTitles[i]
    ps = hkc.projSummaries[i]

    try:  
      proj1TitleNlp   = hkc.nlp(pt)
      proj1SummaryNlp = hkc.nlp(ps)
    except: print("nlp problem with", pt); continue

    titleScoresL, summaryScoresL = [], []
    titleScoresD, summaryScoresD = {}, {}

    for id in hkc.iuiIds:
      try:
        iuiNlp = iuiNlpDb[id]
        titleScore   = int(iuiNlp.similarity(proj1TitleNlp)   * 10000)
        summaryScore = int(iuiNlp.similarity(proj1SummaryNlp) * 10000)

        if titleScore   not in titleScoresL:   titleScoresL.append(  titleScore);   titleScoresD[titleScore]     = hkc.iuiId2Txt[id]
        if summaryScore not in summaryScoresL: summaryScoresL.append(summaryScore); summaryScoresD[summaryScore] = hkc.iuiId2Txt[id]

      except: print("ignoring ", id); traceback.print_exc();

    titleScoresL.sort(); summaryScoresL.sort()

    print("=" * 40)
    print(titleScoresL[-5:])
    print(summaryScoresL[-5:])
  
    print(pt); print(ps)

    print("\nsimilarity by project title")
    for i in titleScoresL[-5:]:   print(titleScoresD[i])

    print("\nsimilarity by project summary")
    for i in summaryScoresL[-5:]: print(summaryScoresD[i])

### end ###
