// program to demonstrate forking but also running external programs via execl
// and execve
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
    y += 5;
    printf("\nFrom the parent process, PID: %d, y=%d\n", getpid(), y);
    execl("/bin/ls", "ls", "..", NULL);
  } else {
    pid_t pid = fork();
    if (pid > 0) {
      wait(NULL);
      y += 1;
      printf("\nFrom the child process, PID: %d, y=%d\n", getpid(), y);
      execl("/bin/ls", "ls", "../labs", NULL);
    } else {
      y -= 1;
      printf("\nFrom the grand child process, PID: %d, y=%d\n", getpid(), y);
      execl("/bin/ls", "ls", ".", NULL);
    }
  }
}
