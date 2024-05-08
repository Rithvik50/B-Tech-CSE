#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <integer1> <integer2>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int x = atoi(argv[1]);
    int y = atoi(argv[2]);

    int product = x * y;

    printf("Product of %d and %d is: %d\n", x, y, product);

    return EXIT_SUCCESS;
}