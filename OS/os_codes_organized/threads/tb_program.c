#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int sum = 0;

void* runner(void* param) {
    int till = *(int*)param;
    for(int i=0; i<=till; i++) {
        sum += i;
    }
    return NULL;
}

int main(int argc, char** argv) {
    pthread_t tid;

    if(argc != 2) {
        fprintf(stderr, "Usage: a.out <integer value>");
        return -1;
    }

    int as_int = atoi(argv[1]);
    if (as_int < 0) {
        fprintf(stderr, "Integer value should be greater than zero");
        return -1;
    }

    pthread_create(&tid, NULL, runner, &as_int);
    pthread_join(tid, NULL);

    printf("Thread did work: %d\n", sum);
}
