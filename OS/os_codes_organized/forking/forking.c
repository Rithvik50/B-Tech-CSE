#include <stdio.h>
#include <unistd.h>

int main() {
  pid_t pid = fork();
  if (pid == -1) {
    perror("Failed to fork");
    return 1;
  }

  if (pid > 0) {
    printf("From the parent process, PID; %d\n", getpid());
    printf("Child PID: %d\n", pid);
  } else {
    printf("From the child process, PID; %d\n", getpid());
    printf("Parent PID: %d\n", getppid());
  }
}
