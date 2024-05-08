// Program to demo "First Come First Serve" CPU Scheduling
#include "scheduling.h"
#include <stdio.h>

int main() {
  process processes[4] = {
      input_data("P1", 0, 2),
      input_data("P2", 1, 2),
      input_data("P3", 5, 3),
      input_data("P4", 6, 4),
  };

  int time = 0;
  FOR_EACH(processes) {
    time += saturating_subtract(processes[i].arrival_time, time);

    processes[i].completion_time = time + processes[i].burst_time;

    processes[i].turn_around_time =
        processes[i].completion_time - processes[i].arrival_time;

    processes[i].waiting_time =
        processes[i].turn_around_time - processes[i].burst_time;

    processes[i].response_time = processes[i].waiting_time;

    time += processes[i].burst_time;
  }

  printf("Process-Name\tArrival-Time\tBurst-Time\tCT\tTAT\tWT\tRT\n");
  FOR_EACH(processes) {
    printf("%s\t%d\t%d\t%d\t%d\t%d\t%d\n", processes[i].name,
           processes[i].arrival_time, processes[i].burst_time,
           processes[i].completion_time, processes[i].turn_around_time,
           processes[i].waiting_time, processes[i].response_time);
  }
}
