.data
NUM: .word 123

.text
LDR R0,=NUM
LDR R2,[R0]
MOV R6,#0
MOV R3,R2

div:
MOV R4,#0
loop:
CMP R3,#10
BLT res
SUB R3,R3,#10
ADD R4,R4,#1
B LOOP

res:
ADD R6,R3,R6
CMP R4,#10
MOVGT R3,R4
BGT div
ADDLT R6,R6,R4

end:
.end
