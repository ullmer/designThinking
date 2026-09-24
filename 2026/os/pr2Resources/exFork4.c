#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
  int numProcs = 4;

  for(int i=0; i<numProcs; i++) {
    int pid=fork();
    if (pid==0) {
      printf("%i pid: %i\n", i, getpid());
      exit(0); 
    }
  }

  int pid, statloc;
  for(int i=0; i<numProcs; i++) {
    pid = wait(&statloc);
    printf("child completes: %i %i\n", pid, statloc);
  }
}

/// end ///
