#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/shm.h>

int main() {
    void *shm;
    char buf[128];
    int shmid;

    shmid = shmget((key_t)2345, 1024, 0666 | IPC_CREAT);
    printf("Key used for shm: %d\n", shmid);

    shm = shmat(shmid, NULL, 0);
    printf("Shared memory segment created at: %p\n", shm);

    printf("Data to write: ");
    fgets(buf, 128, stdin);

    strncpy(shm, buf, 128);

    sleep(5);

    shmdt(shm);
    return 0;
}
