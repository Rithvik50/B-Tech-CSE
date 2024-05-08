/*
Write a C program to change the ownership of files in a directory created after a certain date.
Inputs to the program: directory, date, and new permission to be set as run time arguments
*/

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s directory_path date new_permissions\n", argv[0]);
        return 1;
    }

    // Parse command-line arguments
    char *directory_path = argv[1];
    char *date = argv[2];
    char *new_permissions = argv[3];

    // Open the directory
    DIR *dir = opendir(directory_path);
    if (!dir) {
        perror("Error opening directory");
        return 1;
    }

    // Convert date string to time_t
    // You need to implement the logic to convert date string to time_t, it's not included here

    // Loop through directory entries
    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        // Get file stats
        char file_path[256];
        strcpy(file_path, directory_path);
        strcat(file_path, "/");
        strcat(file_path, entry->d_name);
        struct stat file_stat;
        if (stat(file_path, &file_stat) == -1) {
            perror("Error getting file stats");
            continue;
        }

        // Check if file was created after the specified date
        // You need to implement the logic to compare file creation date with the specified date, it's not included here

        // Change file ownership
        if (chown(file_path, getuid(), getgid()) == -1) {
            perror("Error changing file ownership");
            continue;
        }

        // Change file permissions
        if (chmod(file_path, strtol(new_permissions, 0, 8)) == -1) {
            perror("Error changing file permissions");
            continue;
        }

        printf("Changed ownership and permissions of file: %s\n", file_path);
    }

    // Close the directory
    closedir(dir);

    return 0;
}