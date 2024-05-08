#include <stdio.h>

int simulate_segmentation(int segment_number, int base_address, int segment_limit, int offset) {
    if (offset >= segment_limit) {
        printf("Segmentation fault: Offset exceeds segment limit\n");
        return -1;
    }

    int physical_address = base_address + offset;
    return physical_address;
}

int main() {
    int segment_number, base_address, segment_limit, offset;

    printf("Enter segmentation number: ");
    scanf("%d", &segment_number);

    printf("Enter base address (in hexadecimal format): ");
    scanf("%x", &base_address);

    printf("Enter segment limit: ");
    scanf("%d", &segment_limit);

    printf("Enter offset: ");
    scanf("%d", &offset);

    int physical_address = simulate_segmentation(segment_number, base_address, segment_limit, offset);
    if (physical_address != -1) {
        printf("Physical address: 0x%X\n", physical_address);
    }

    return 0;
}