/*
Write a C program to truncate the files in a directory created after a certain date to half its original size. 
Inputs to the program: directory and date as run time arguments
*/

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>
#include <time.h>

void trunc(const char *dirPath);

int main() {
    const char *directory = "C:\\Engineering\\4th Sem";
    trunc(directory);
    return 0;
}

void trunc(const char *path) {
    time_t now;
    time(&now);
    struct tm *localTime = localtime(&now);
    SYSTEMTIME systemTime;
    systemTime.wYear = localTime->tm_year + 1900;
    systemTime.wMonth = localTime->tm_mon + 1;
    systemTime.wDay = localTime->tm_mday;
    systemTime.wHour = 0;
    systemTime.wMinute = 0;
    systemTime.wSecond = 0;
    systemTime.wMilliseconds = 0;
    FILETIME fileTime;
    SystemTimeToFileTime(&systemTime, &fileTime);
    HANDLE findHandle;
    WIN32_FIND_DATA findData;
    char searchPath[MAX_PATH];
    snprintf(searchPath, MAX_PATH, "%s\\*", path);
    findHandle = FindFirstFile(searchPath, &findData);
    if (findHandle == INVALID_HANDLE_VALUE) {
        fprintf(stderr, "Error opening directory\n");
        return; 
    }
    do {
        if (!(findData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
            char fullPath[MAX_PATH];
            snprintf(fullPath, MAX_PATH, "%s\\%s", path, findData.cFileName);
            FILETIME fileCreationTime = findData.ftCreationTime;
            if (CompareFileTime(&fileCreationTime, &fileTime) > 0) {
                HANDLE fileHandle = CreateFile(fullPath, GENERIC_WRITE, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
                if (fileHandle == INVALID_HANDLE_VALUE) {
                    fprintf(stderr, "Error opening file %s\n", fullPath);
                    continue;
                }
                DWORD fileSizeLow = GetFileSize(fileHandle, NULL);
                DWORD fileSizeHigh = 0;
                if (fileSizeLow == INVALID_FILE_SIZE && GetLastError() != NO_ERROR) {
                    fprintf(stderr, "Error getting file size for %s\n", fullPath);
                    CloseHandle(fileHandle);
                    continue;
                }
                LARGE_INTEGER newSize;
                newSize.QuadPart = ((LONGLONG)fileSizeLow + ((LONGLONG)fileSizeHigh << 32)) / 2;
                if (!SetFilePointerEx(fileHandle, newSize, NULL, FILE_BEGIN) ||
                    !SetEndOfFile(fileHandle)) {
                    fprintf(stderr, "Error truncating file %s\n", fullPath);
                    CloseHandle(fileHandle);
                    continue;
                }
                CloseHandle(fileHandle);
                printf("Reduced size of %s to half of its original size\n", fullPath);
            }
        }
    } while (FindNextFile(findHandle, &findData) != 0);
    FindClose(findHandle);
}