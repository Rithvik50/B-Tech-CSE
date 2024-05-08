// the parent waits until the child completes its execution
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  pid_t pid = fork();
  int y = 0;

  if (pid == -1) {
    perror("Failed to fork");
    return 1;
  }

  if (pid > 0) {
    wait(NULL);
    y += 1;
    printf("From the parent process, PID: %d, y=%d\n", getpid(), y);
  } else {
    y -= 1;
    printf("From the child process, PID: %d, y=%d\n", getpid(), y);
    exit(0);
  }
}
