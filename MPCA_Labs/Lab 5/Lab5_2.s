.data
A: .word 12,10,3,8,7,4,1

.text
 ldr r0, =A
 mov r4, #0

loop1:
 mov r3, #0

loop2:
 add r5, r0, r3, LSL #2
 add r6, r5, #4
 ldr r1, [r5]
 ldr r2, [r6]
 cmp r1, r2
 movle r7, r1
 movle r1, r2
 movle r2, r7
 strle r1, [r5]
 strle r2, [r6]
 add r3, r3, #1
 cmp r3, #7
 blt loop2
 add r4, r4, #1
 cmp r4, #7
 blt loop1
 mov r7, #1
 swi 0
