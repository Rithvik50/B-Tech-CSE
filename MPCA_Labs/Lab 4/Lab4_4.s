.data
str: .asciz "Hello"
des: .asciz "aaaaa"

.text
LDR R0,=str
MOV R1,#0
LDR R2,=des

loop:
LDRB R3,[R0,R1]
STRB R3,[R2,R1]
ADD R1,R1,#1
CMP R3,#0
BEQ end
B loop

end:
SWI 0x11
