.data
A: .word 1,2,3,4,5,6,7,8,9

.text
LDR R0,=A
MOV R1,#0
MOV R2,#3
MOV R3,#3
MOV R4,#0
MOV R8,#4

loop_i:
MOV R5,#0

loop_i_j:
STMEA R13!,{R4,R5}
BL loop_get_addr
LDMEA R13!,{R4,R5,R6}
LDR R7,[R0,R6]
ADD R1,R1,R7
ADD R5,R5,#1
CMP R5,#3
BNE loop_i_j
ADD R4,R4,#1
CMP R4,#3
BNE loop_i
B end

loop_get_addr:
LDMEA R13!,{R4,R5}
MLA R7,R3,R4,R5
MUL R6,R8,R7
STMEA R13!,{R4,R5,R6}
BX lr

end:
SWI 0x11
