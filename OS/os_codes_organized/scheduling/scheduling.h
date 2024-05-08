#include <stdbool.h>

#define FOR_EACH(x) for (int i = 0; i < sizeof(x) / sizeof(*x); i++)
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
