.data
NUM: .word 85
RES: .word 0,0

.text
LDR R0,=NUM
LDR R0,[R0]
MOV R1,#32
MOV R2,#0
MOV R3,#0
LDR R7,=RES
	
loop:
CMP R1,#0
BEQ save
AND R4,R0,#1
CMP R4,#1
BLEQ one
BNE zero
MOV R6,#1
MOV R0,R0,LSR #1
SUB R1,#1
B loop
	
zero:
ADDS R2,R2,#1
MOV R15,R14
B loop

one:
ADDS R3,R3,#1
MOV R15,R14
B loop

save:
STR R2,[R7],#4
STR R3,[R7]

end:
.end
