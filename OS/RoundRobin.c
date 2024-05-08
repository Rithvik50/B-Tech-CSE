#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main() {
    int n;
    printf("Enter number: ");
    scanf("%d", &n);
    int rt[6], br[6];
    for (int i = 0; i < n; i++) {
        rt[i] = br[i];
        if (1) {
            printf("Hello");
        }
    }
    return 0;
}