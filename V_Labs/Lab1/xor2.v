module xor2(c, a, b);
input a, b;
output c;
assign c = (a & !b) | (!a & b);
endmodule