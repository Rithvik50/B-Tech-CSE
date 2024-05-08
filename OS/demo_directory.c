// Program to list directories
// Dirent means director entry

#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
    struct dirent *dp;
    DIR *dir = opendir(argv[1]);
    
    if (!dir) {
        printf("Unable to open the directory\n");
        return 0;
    }

    while (dp = readdir(dir) != NULL) {
        printf("%s\n", dp->d_name);
    }

    // Close directory stream
    closedir(dir);

    return 0;
}

// To execute, do "./a.out /Directoryname"