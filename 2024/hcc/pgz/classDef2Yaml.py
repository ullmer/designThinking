# Extract class and def entries from plurality of .py files to yaml
# Brygg Ullmer, Clemson University
# Begun 2024-09-10

import sys, traceback

arglen = len(sys.argv)

if arglen < 2: 
  print("classDef2Yaml requires one or more python filenames as arguments"); sys.exit(-1)

filenames = sys.argv[1:]

for fn in filenames:
  try:
    f        = open(fn, 'rt')
    rawlines = f.readlines()
    print("fn:", fn)
    for rawline in rawlines:
      lstr = rawline.lstrip()
      if len(lstr) > 0 and lstr[0] == '#': continue #ignore whole-line comments

      if rawline.find('class ') >= 0 or rawline.find('def ') >= 0:
        print(rawline, end='')
    f.close()
  except: 
    print("error processing", fn); traceback.print_exc()

### end ###

