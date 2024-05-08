#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    pid_t p1;
    int y = 0;
    p1 = fork(); //Child process is created

    if (p1 > 0) {
        wait(1);
        for (int i = 0; i < 5; i++) {
            sleep(i);
            y--;
            printf("This is parent process! Process id = %d, y = %d\n", getppid(), y);
        }
    } else if (p1 == 0) {
        for (int i = 0; i < 5; i++) {
            sleep(i);
            y++;
            printf("This is child process! Parent process id = %d, Child process id = %d, y = %d\n", getppid(), getpid(), y);
        }
        exit(0);
    } else {
        printf("Fork has failed!\n");
    }
    return 0;
}