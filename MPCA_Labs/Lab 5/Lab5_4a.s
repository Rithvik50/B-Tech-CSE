.data
A: .word 12
B: .word 2
C: .word 3
X: .word 0

.text
 ldr r0, =A
 ldr r1, [r0]
 ldr r0, =B
 ldr r2, [r0]
 add r1, r1, r2
 ldr r0, =C
 ldr r2, [r0]
 sub r1, r1, r2
 ldr r0, =X
 str r1, [r0]
 mov r0, #0
 bx lr

.end
