#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>

#define BUFFER_SIZE 100

int main() {
    int fd;
    char buff[BUFFER_SIZE] = "";

    // FIFO filepath
    char myfifo[BUFFER_SIZE] = "/tmp/myfifo"; // Filepath figure it out
    
    printf("Enter the message to be passed\n");
    read(0, buff, BUFFER_SIZE);

    // Creating a file named myfifo
    mkfifo(myfifo, 0666);

    fd = open(myfifo, O_RDONLY);

    // Write the input to FIFO and close it
    read(fd, buff, strlen(buff) + 1);
    close(fd);

    close(100);
    return 0;
}