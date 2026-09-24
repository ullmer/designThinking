from multiprocessing import Process
import os

def worker(i):
  print(i, "pid:", os.getpid())

numProcs = 4
children = []

if __name__ == "__main__":

  for i in range(numProcs):
    p = Process(target=worker, args=(i,))
    p.start()
    children.append(p)
  
  for p in children:
    p.join()
    print("child completes:", p.pid, p.exitcode)

### end ###
