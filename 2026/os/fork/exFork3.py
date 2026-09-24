import os

numProcs = 4

for i in range(numProcs):
  pid = os.fork()
  if pid == 0: 
    print(i, "pid:", os.getpid())
    os._exit(0)
  else: os.wait()

### end ###
