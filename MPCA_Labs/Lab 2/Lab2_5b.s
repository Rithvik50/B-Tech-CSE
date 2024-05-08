.data
fib:.word 0,0,0,0,0,0,0,0,0,0

.text
MOV R0,#0 
MOV R1,#1 
LDR R2,=fib
MOV R3,#10

loop:
STR R0,[R2],#4 
ADD R4,R0,R1 
MOV R0,R1 
MOV R1,R4 
SUBS R3,R3,#1 
BNE loop
.end
