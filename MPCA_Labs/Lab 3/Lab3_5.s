.data
A: .word 10,20,30,40,50,60,70,80,90,100
KEY: .word 40

.text
LDR R0,=A
LDR R1,=KEY
MOV R3,#10
LDR R6,[R1]
MOV R2,#0

loop:
CMP R3,#0
BEQ exit
LDR R5,[R0],#4
CMP R5,R6
BEQ found
SUB R3,#1
B loop

found:
MOV R2,#1

end:
.end
