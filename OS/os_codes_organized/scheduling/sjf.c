// Program to demo "Shortest Job First" CPU Scheduling
#include <stdbool.h>
#include <stdio.h>

#define len(x) sizeof(x) / sizeof(*x)
#define input_data(n, at, bt)                                                  \
  { .name = n, .arrival_time = at, .burst_time = bt }

typedef struct {
  char *name;
  int arrival_time;
  int burst_time;
  int completion_time;
  int turn_around_time;
  int waiting_time;
  int response_time;
} process;

int saturating_subtract(int a, int b) { return a < b ? 0 : a - b; }

void swap(process *a, process *b) {
  process t = *a;
  *a = *b;
  *b = t;
}

void sort(process *arr, int len) {
  bool swapped = true;
  while (swapped) {
    swapped = false;
    for (int i = 0; i < len - 1; i++) {
      if (arr[i].arrival_time > arr[i + 1].arrival_time ||
          arr[i].burst_time > arr[i + 1].burst_time) {
        swapped = true;
        swap(&arr[i], &arr[i + 1]);
      }
    }
  }
}

int main() {
  process processes_[4] = {
      input_data("P1", 1, 3),
      input_data("P2", 2, 4),
      input_data("P3", 1, 2),
      input_data("P4", 4, 4),
  };

  sort(processes_, len(processes_));

  int time = 0;

#define for_each(x) for (int i = 0; i < sizeof(x##es_) / sizeof(*x##es_); i++)
#define process processes_[i]
#define in
#define processes

  for_each(process) in processes {
    time += saturating_subtract(process.arrival_time, time);

    process.completion_time = time + process.burst_time;
    process.turn_around_time = process.completion_time - process.arrival_time;
    process.waiting_time = process.turn_around_time - process.burst_time;
    process.response_time = process.waiting_time;

    time += process.burst_time;
  }

  printf("Process-Name\tArrival-Time\tBurst-Time\tCT\tTAT\tWT\tRT\n");
  for_each(process) {
    printf("%s\t%d\t%d\t%d\t%d\t%d\t%d\n", process.name, process.arrival_time,
           process.burst_time, process.completion_time,
           process.turn_around_time, process.waiting_time,
           process.response_time);
  }
}
