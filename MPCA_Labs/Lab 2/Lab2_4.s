.data
A:.word 10,50,41,55,30,20,11,5,100,77

.text
LDR R0,=A 
LDR R1,[R0] 
LDR R3,=10

start:
LDR R4,[R0],#4
CMP R4,R1
BLE not_largest 
MOV R1,R4

not_largest: 
SUBS R3,R3,#1 
BNE start
.end
