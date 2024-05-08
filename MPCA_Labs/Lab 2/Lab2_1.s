.data
A:.word 10,20 
res:.word 0

.text
LDR R0,=A
LDR R2,=res 
LDR R1,[R0] 
LDR R3,[R0,#4] 
ADD R1,R1,R3 
STR R1,[R2]
