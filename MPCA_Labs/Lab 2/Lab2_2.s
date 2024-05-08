.data
A:.word 10,3,41,55,30,22,11,5,83,90 
odd:.word 0,0,0,0,0,0
even:.word 0,0,0,0

.text
LDR R0,=A 
LDR R1,=odd 
LDR R2,=even 
LDR R3,=10

start:
CMP R3,#0 
BEQ end
LDR R4,[R0],#4 
AND R5,R4,#1 
CMP R5,#0 
BEQ evennum 
BNE oddnum

evennum:
STR R4,[R2],#4 
SUB R3,R3,#1 
B start

oddnum:
STR R4,[R1],#4 
SUB R3,R3,#1 
B start

end: 
.end
