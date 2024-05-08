#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int array[] = {1, 6, 2, 4, 5, 8, 9, 0};

void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

void sort(int *arr, int len) {
  bool swapped = true;
  while (swapped) {
    swapped = false;
    for (int i = 0; i < len; i++) {
      if (arr[i] > arr[i + 1]) {
        swapped = true;
        swap(&arr[i], &arr[i + 1]);
      }
    }
  }
}

int main() {
  pid_t pid = fork();
  if (pid == -1) {
    perror("Failed to fork");
    return 1;
  }

  if (pid > 0) {
    wait(NULL);
    printf("From the parent process, PID: %d\n", getpid());
    printf("The values after sorting in child are: ");
    for (int i = 0; i < sizeof(array) / sizeof(*array); i++) {
      printf("%d ", array[i]);
    }
    printf("\n");
  } else {
    printf("From the child process, PID: %d\n", getpid());
    sort(array, sizeof(array) / sizeof(*array));
  }
}
