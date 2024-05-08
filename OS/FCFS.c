#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void swap() {
    
}

int main() {
    char *a = "P1";
    char *b = "P2";
    char *c = "P3";
    int arv[3] = {2, 1, 3}; //Arrival order
    int burst[3] = {10, 5, 3}; //Burst
    int n = 3; //Number of processes
    for (int i = 0; i < n - 1; i++) {
        if (i == 0) {
            start[i] = arv[i];
        } else {
            start[i] = finish[i-1];
        }
    }
}