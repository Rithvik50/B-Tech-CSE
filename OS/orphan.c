#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int pid;
    pid = fork();
    if (pid < 0) {
        printf("For error\n");
        exit(1);
    } else if (pid == 0) {
        sleep(5);
        printf("Child process\n");
        printf("Child id: %d, Parent id: %d", getpid(), getppid());
    } else {
        printf("Parent process\n");
        printf("Parent id: %d, Child id: %d", getppid(), getpid());
        exit(1);
    }
    return 0;
}