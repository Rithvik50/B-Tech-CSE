// modify value of a variable in each iteration
#include <stdio.h>
#include <unistd.h>

int main() {
  pid_t pid = fork();
  int j = 0, y = 0;

  if (pid == -1) {
    perror("Failed to fork");
    return 1;
  }

  if (pid > 0) {
    for (int i = 0; i < 5; i++) {
      printf("From the parent process, PID: %d, pid_var: %d, y=%d\n", getpid(),
             pid, y);
      sleep(1);
      y += 1;
    }
  } else {
    for (int i = 0; i < 5; i++) {
      printf("From the child process, PID: %d, pid_var: %d, j=%d\n\n", getpid(),
             pid, j);
      sleep(1);
      j += 1;
    }
  }
}
