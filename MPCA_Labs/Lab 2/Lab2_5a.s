.data
A:.byte 10,50,41,55,30,20,11,5,80,16

.text
LDR R0,=A
LDRB R1,[R0],#1 
LDR R2,=9

loop:
LDRB R3,[R0],#1 
ADD R1,R1,R3 
SUBS R2,R2,#1 
BNE loop
.end
