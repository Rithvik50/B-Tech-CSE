#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <integer1> <integer2>\n", argv[0]);
        return EXIT_FAILURE;
    }

    char *product_program = "./product"; // Assuming product is in the same directory

    // Use execl to execute the product program with the provided integers
    execlp(product_program, product_program, argv[1], argv[2], NULL);

    // If execl fails, print an error message
    perror("execl");
    return EXIT_FAILURE;
}