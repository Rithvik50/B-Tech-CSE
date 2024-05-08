#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    int rv = 0;
    printf("Real UID = %d, Effective UID = %d\n", getuid(), geteuid());
    rv = setuid(1000);

    if (rv < 0) {
        printf("Error setting UID\n");
    }
    rv = setgid(1000);

    if (rv < 0) {
        printf("Error setting GID\n");
    }
    
    printf("Real UID = %d, Effective UID = %d\n", getuid(), geteuid());

    exit(0);
}