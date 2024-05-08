#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd;
    int i, err = 0;
    char buf[10] = "";

    fd = creat("./temp.txt", S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);

    if (fd == -1) {
        printf("Unable to create file\n");
    }

    for (int i = 0; i < 10; i++) {
        write(fd, "0123456789", 10);
    }

    close(fd);

    fd = open("./temp.txt", O_RDWR, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    err = lseek(fd, 5, SEEK_SET);

    if (err == -1) {
        printf("Unable to seek\n");
    }
    err = read(fd, buf, 5);
    
    if (err == -1) {
        printf("Read failed\n");
    }
    printf("Read: %s\n", buf);
    err = lseek(fd, -4, SEEK_END);

    if (err == -1) {
        printf("Unable to seek to the EOF\n");
    }
    memset(buf, 0, strlen(buf));
    err = read(fd, buf, 3);

    return 0;
}