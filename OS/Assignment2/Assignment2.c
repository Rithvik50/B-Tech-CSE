#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void reverse_string(char *str) {
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
}

int main() {
    int pipes[2];
    pid_t pid;

    if (pipe(pipes) == -1) {
        printf("Pipe failed\n");
        return 1;
    }

    pid = fork();

    if (pid > 0) { // Parent process
        close(pipes[0]);
        printf("Enter a string: ");
        char input_string[256];
        fgets(input_string, sizeof(input_string), stdin);
        write(pipes[1], input_string, strlen(input_string));
        close(pipes[1]);
        wait(NULL);
    } else if (pid == 0) { // Child process
        close(pipes[1]);
        char buffer[256];
        ssize_t bytes_read = read(pipes[0], buffer, sizeof(buffer));
        if (bytes_read > 0) {
            buffer[bytes_read] = '\0';
            reverse_string(buffer);
            printf("Reversed string in child process: %s\n", buffer);
        }
        close(pipes[0]);
    } else {
        printf("Fork failed\n");
    }

    return 0;
}