#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int sum; // This data is shared by the thread(s)
void *runner(void *param); // Threads call this function

int main(int argc, char *argv[]) {
    pthread_t tid; // Thread identifier
    pthread_attr_t attr; // Set of thread attributes

    if (argc != 2) {
        fprintf(stderr, "Usage: a.out <integer value>\n");
        return -1;
    }
    if (atoi(argv[1] < 0)) {
        fprintf(stderr, "%d must be >= 0\n", atoi(argv[1]));
        return -1;
    }

    // Get the default attributes
    pthread_attr_init(&attr);

    // Create the thread
    pthread_create(&tid, &attr, runner, argv[1]);

    // Wait for the thread to exit 
    pthread_join(tid, NULL);
    printf("Sum = %d\n", sum);

    return 0;
}

// Thread will begin control in this function
void *runner(void *param) {
    int upper = atoi(param);
    sum = 0;
    for (int i = 0; i <= upper; i++) {
        sum += i;
    }
    pthread_exit(0);
}