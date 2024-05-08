#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    int pipefd[2];
    pipe(pipefd);

    char buffer[32];
    pid_t pid = fork();

    if(pid == 0) {
        close(pipefd[1]); // not writing
        read(pipefd[0], buffer, sizeof(buffer));
        close(pipefd[0]); // finished reading
        printf("Child Recieved: %s\n", buffer);
        exit(EXIT_SUCCESS);
    } else {
        close(pipefd[0]); // not reading
        write(pipefd[1], "Hello from parent!", 19);
        close(pipefd[1]); // finished writing
        wait(NULL);
        printf("Alr done\n");
    }

    return EXIT_SUCCESS;
}
