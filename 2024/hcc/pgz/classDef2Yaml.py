# Extract class and def entries from plurality of .py files to yaml
# Brygg Ullmer, Clemson University
# Begun 2024-09-10

import glob, sys 

arglen = len(sys.argv)

if arglen < 2: 
  print("classDef2Yaml requires one or more python filenames as arguments"); sys.exit(-1)

### end ###

