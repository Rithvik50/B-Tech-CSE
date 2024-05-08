#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  int x, y;
  printf("Enter x value: ");
  scanf("%d", &x);
  printf("Enter y value: ");
  scanf("%d", &y);

  char x_arg[32];
  char y_arg[32];

  snprintf(x_arg, 32, "%d", x);
  snprintf(y_arg, 32, "%d", y);

  printf("Executing process now\n");
  execl("product", "product", x_arg, y_arg, NULL);
}
