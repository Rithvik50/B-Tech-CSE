/*
Write a C program to change the permissions of files in a directory created after a certain date. 
Inputs to the program: directory, date, and new permission to be set as run time arguments
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <dirent.h>
#include <time.h>
#include <string.h>

void changePermissions(const char *dirPath, const char *dateString, mode_t newMode) {
    struct tm date;
    strptime(dateString, "%Y-%m-%d", &date);

    DIR *dir;
    struct dirent *entry;
    struct stat fileStat;
    char filePath[256];

    dir = opendir(dirPath);
    if (dir == NULL) {
        perror("Unable to open directory");
        exit(EXIT_FAILURE);
    }

    while ((entry = readdir(dir)) != NULL) {
        snprintf(filePath, sizeof(filePath), "%s/%s", dirPath, entry->d_name);
        if (stat(filePath, &fileStat) < 0) {
            perror("Unable to get file status");
            continue;
        }
        struct tm *fileDate = localtime(&fileStat.st_mtime);
        if (fileDate->tm_year > date.tm_year ||
            (fileDate->tm_year == date.tm_year && difftime(mktime(fileDate), mktime(&date)) > 0)) {
            if (chmod(filePath, newMode) < 0) {
                perror("Unable to change file permissions");
            } else {
                printf("Changed permissions of file: %s\n", filePath);
            }
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        printf("Usage: %s directory date(YYYY-MM-DD) new_permission\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char *dirPath = argv[1];
    const char *dateString = argv[2];
    mode_t newMode = strtol(argv[3], NULL, 8);

    changePermissions(dirPath, dateString, newMode);

    return EXIT_SUCCESS;
}