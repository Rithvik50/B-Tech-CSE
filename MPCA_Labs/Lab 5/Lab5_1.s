.data
A: .word 1, 2, 3, 4, 5, 6, 7, 8, 9
B: .word 1, 1, 2, 2, 3, 3, 4, 4, 5
C: .word 0, 0, 0, 0, 0, 0, 0, 0, 0

.text
main:
 ldr r1, =A
 ldr r2, =B
 ldr r3, =C
 mov r4, #3

outer_loop:
 mov r0, r2
 mov r9, #3

inner_loop:
 mov r8, #0
 mov r7, #3
 mov r6, r1

innermost_loop:
 ldr r10, [r6], #4
 ldr r11, [r0], #4
 mul r12, r10, r11
 add r8, r8, r12
 subs r7, r7, #1
 bne innermost_loop
 str r8, [r3], #4
 subs r9, r9, #1
 bne inner_loop
 add r1, r1, #12
 subs r4, r4, #1
 bne outer_loop
 mov r0, #0
 mov r7, #1
 swi 0x11

.end
