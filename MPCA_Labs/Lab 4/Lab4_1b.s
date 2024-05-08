.data
A: .word 10,20,30,40,50 
B: .word 10,20,30,40,50
	
.text
LDR R0,=A
LDR R1,=B
MOV R2,#5
MOV R5,#0
LDR R3,[R0],#4
LDR R4,[R1],#4
	
loop:
CMP R2,#0
BEQ end
MLA R5,R3,R4,R5
SUB R2,R2,#1
LDR R3,[R0],#4
LDR R4,[R1],#4
B loop
	
end:
.end
