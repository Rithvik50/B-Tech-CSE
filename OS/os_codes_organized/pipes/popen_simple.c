#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    FILE* fp = popen("python -c 'exit(999)'", "r");
    if(fp == NULL) {
        perror("Couldn't open pipe");
        return 1;
    }

    char output[32];
    printf("Stuff written to pipe:\n");
    while(fgets(output, sizeof(output), fp)) {
        printf("%s", output);
    }

    int status;
    if((status = pclose(fp)) == -1) {
        perror("Couldn't close pipe");
        return 1;
    }

    printf("Pipe closed with status: %d\n", status);
    return 0;
}
