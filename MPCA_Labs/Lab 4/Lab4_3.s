.data
str: .asciz "Hello"

.text
LDR R0,=str
MOV R1,#0

loop:
LDRB R2,[R0,R1]
CMP R2,#0
BEQ end
ADD R1,R1,#1
B loop

end:
SWI 0x11
