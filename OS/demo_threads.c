#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int g = 0; // Create a global variable which will be changed in the threads

// The function to be executed by all threads
void *myThreadFunction(void *vargp) {
    int *myid = (int*)vargp; // Store the value argument passed to this thread
    static int s = 0; // Let us create a static variable to observe its changes
    int l = 0; // Let us create a local vairable to observe its changes

    ++l; ++s; ++g; // Change local, static, and global variables

    printf("Thread ID: %d, Local: %d, Static: %d, Global: %d\n", *myid, l, s ,g); // Print the argument, static, and global variables

    pthread_exit(NULL);
}

int main() {
    pthread_t tid;

    // Let us create three threads
    for (int i = 0; i < 3; i++) {
        pthread_create(&tid, NULL, myThreadFunction, (void*)&tid);
        pthread_join(tid, NULL);
    }

    printf("In main()\n");
    return 0;
}