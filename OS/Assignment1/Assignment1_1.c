#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main() {
    pid_t p1;
    p1 = fork();
    if (p1 > 0) {
    	wait(NULL);
        printf("This is parent process! Process id = %d\n", getpid());
    } else if (p1 == 0) {
        printf("This is a child process! Process id = %d\n", getpid());
        execlp("ps", "ps", "u", NULL);
       	exit(0);
    } else printf("Fork is failed");
    return 0;
}