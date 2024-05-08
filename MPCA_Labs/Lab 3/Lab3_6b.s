.data
A: .word 10,20,30,40,50,60,70,80,90.100
ODD: .word 0
EVEN: .word 0

.text
LDR R0,=A
LDR R1,=ODD
LDR R2,=EVEN
MOV R3,#0
MOV R5,#0
MOV R6,#0

loop:
CMP R3,#0
BEQ end
AND R4,R3,#1
CMP R4,#1
BEQ odd
BNE even

odd:
LDR R7,[R0],#4
ADD R5,R5,R7
ADD R3,R3,#1
B loop

even:
LDR R7,[R0],#4
ADD R6,R6,R7
ADD R3,R3,#1
B loop

end:
STR R6,[R2]
STR R5,[R1]
SWI 0x0111
