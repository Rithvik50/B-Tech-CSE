.data
str: .asciz "Hello"
des: .asciz "AHelloHeloAa"

.text
LDR R0,=str
MOV R1,#0
LDR R3,=des
MOV R4,#0

checkout:
MOV R6,#0
MOV R7,#0
LDRB R2,[R0]
LDRB R5,[R3],#1
CMP R2,R5
BEQ checkin
CMP R5,#0
BNE checkout
B end

checkin:
ADD R6,R6,#1
LDRB R2,[R0,R6]
LDRB R5,[R3,R7]
ADD R7,R7,#1
CMP R2,#0
BEQ add
CMP R2,R5
BEQ checkin
CMP R5,#0
BNE checkout

add:
ADD R1,R1,#1
CMP R5,#0
BNE checkout

end:
SWI 0x11
