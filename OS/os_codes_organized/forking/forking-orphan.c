// Demonstrates orphan processes
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
    sleep(1);
    printf("From the child process (which might be orphaned), PID; %d\n", getpid());
    // PID one takes ownership of this process then
    printf("Parent PID: %d\n", getppid());
  }
}
