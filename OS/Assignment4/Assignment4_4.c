/*
Write a C program to list all files whose name matches the filter.
Inputs to the program as run time arguments: directory and filename (need to support wildcard)
*/

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <fnmatch.h>

void list_files(const char *dir_path, const char *filter) {
    DIR *dir;
    struct dirent *entry;
    char full_path[1024];

    dir = opendir(dir_path);
    if (dir == NULL) {
        perror("Error opening directory");
        exit(EXIT_FAILURE);
    }

    while ((entry = readdir(dir)) != NULL) {
        if (fnmatch(filter, entry->d_name, FNM_PATHNAME) == 0) {
            sprintf(full_path, "%s/%s", dir_path, entry->d_name);
            printf("%s\n", full_path);
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <directory> <filename>\n", argv[0]);
        return EXIT_FAILURE;
    }

    char *dir_path = argv[1];
    char *filter = argv[2];

    list_files(dir_path, filter);

    return EXIT_SUCCESS;
}