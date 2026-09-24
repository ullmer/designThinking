from zipfile import *

verbose=False

#zfn   = '/tmp/pg/0.zip'
zfn   = '/dev/shm/pg/0.zip'
zf    = ZipFile(zfn, 'r')
files = zf.namelist()

targetStr="friends"
count=0

for fn in files:
  if verbose: print(fn)
  f     = zf.open(fn)
  lines = f.readlines()
  for rawline in lines: 
    textline = rawline.decode('utf-8') 
    if textline.find(targetStr) >= 0: count += 1
  f.close()

### end ###

