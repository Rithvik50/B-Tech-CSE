.data
	word: .asciz "trial"
	len: .word 5
.text
.global main

main:
	ldr r0, =word
	bl exchange_letters
	bl print_string
	bx lr
exchange_letters:
		ldrb r1, [r0, #1]
		ldrb r2, [r0, #3]
		strb r2, [r0, #1]
		strb r1, [r0, #3]
		bx lr

print_string:
	ldr r0, =word
	ldr r1, =len
	mov r7, #4
	mov r2, #1
	swi 0
	bx lr
