from glob import *

verbose=False

globpat='/tmp/pg/0/*'
files = glob(globpat)

targetStr="friends"
count=0

for i in files:
  if verbose: print(i)
  f     = open(i, 'rt')
  lines = f.readlines()
  for line in lines: 
    if line.find(targetStr) >= 0: count += 1
  f.close()

print(count)
### end ###

