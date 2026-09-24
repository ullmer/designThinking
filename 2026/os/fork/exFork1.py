import os

numProcs = 4

for i in range(numProcs):
  pid = os.fork()
  print(i, "pid:", pid)

### end ###
