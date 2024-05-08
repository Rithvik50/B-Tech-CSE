.data
A: .word 10
B: .word 5
Z: .word 0

.text
ldr r0, =A
ldr r1, [r0]
mov r2, r1, lsl #2
ldr r0, =B
ldr r3, [r0]
and r3, r3, #15
orr r2, r2, r3
ldr r0, =Z
str r2, [r0]
.end
