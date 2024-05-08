#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  int x = atoi(argv[1]);
  int y = atoi(argv[2]);

  printf("Product of %d * %d from executed process: %d\n", x, y, x * y);
}

