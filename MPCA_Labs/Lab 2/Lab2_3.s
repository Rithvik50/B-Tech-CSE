.data
A:.word 10,-3,41,-55,30,22,0,5,83,0 
pos:.word 0,0,0,0,0,0
neg:.word 0,0
zero:.word 0,0

.text
LDR R0,=A 
LDR R1,=pos
LDR R2,=neg 
LDR R3,=zero 
LDR R4,=10

start:
LDR R8,[R0],#4 
CMP R8,#0 
BGT positive 
BLT negative 
STR R8,[R3],#4 
B next

positive:
STR R8,[R1],#4 
B next

negative:
STR R8,[R2],#4 
B next

next:
SUB R4,R4,#1 
CMP R4,#0 
BNE start 
.end
