#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t p1, p2;
    int y = 0;
    p1 = fork();
    if (p1 > 0) {
        wait(NULL);
        y--;
        printf("Parent, process id: %d". getpid(), y);
        exec1("/bin/ls");
    }
}