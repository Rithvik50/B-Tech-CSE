.data
ARR: .word 1,2,3,4,5,6

.text
LDR R4,=ARR
MOV R0,#4
MOV R1,#0
MOV R2,#5
MOV R3,#0

loop:
ADD R3,R1,R2
MOV R3,R3,ASR #1
CMP R3,R0
BEQ end
BLT high
BGT low

high:
ADD R1,R3,#1
B loop

low:
SUB R2,R3,#1
B loop

end:
.end
