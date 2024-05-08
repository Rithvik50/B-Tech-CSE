#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  pid_t pid = fork();

  if (pid == -1) {
    perror("Failed to fork");
    return 1;
  }

  if (pid > 0) {
    wait(NULL);
  } else {
    printf("From the child process, PID; %d\n", getpid());
    printf("All currently executing processes are: \n");
    system("ps ax");
  }
}

