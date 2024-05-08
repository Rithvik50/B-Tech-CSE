.data
VAL: .word 5
RES: .word 0

.text
LDR R0,=VAL
LDR R1,=RES
LDR R2,[R0]
MOV R3,#1
BL factorial
STR R3,[R1]
B end

factorial:
CMP R2,#0
MOVEQ R15,R14
MUL R3,R3,R2
SUB R2,R2,#1
B factorial

end:
.end
