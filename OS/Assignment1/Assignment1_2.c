#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

// Global array
int arr[] = {1, 6, 2, 4, 5, 8, 9, 0};
int arr_size = sizeof(arr) / sizeof(arr[0]);

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    pid_t child_pid = fork(); // Create a child process

    if (child_pid < 0) {
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (child_pid == 0) {
        // Child process

        // Sorting the array in ascending order
        for (int i = 0; i < arr_size - 1; i++) {
            for (int j = 0; j < arr_size - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap if the element found is greater than the next element
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        // Display the sorted array in the child process
        printf("Sorted array in the child process: ");
        printArray(arr, arr_size);

        // Child process exits after sorting
        exit(EXIT_SUCCESS);
    } else {
        // Parent process

        // Wait for the child process to complete
        waitpid(child_pid, NULL, 0);

        // Display the original array in the parent process
        printf("Original array in the parent process: ");
        printArray(arr, arr_size);
    }

    return 0;
}