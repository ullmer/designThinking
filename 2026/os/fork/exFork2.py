import os

numProcs = 4

for i in range(numProcs):
  pid = os.fork()
  if pid == 0: print(i, "pid:", pid)
  else: os.wait()

### end ###
