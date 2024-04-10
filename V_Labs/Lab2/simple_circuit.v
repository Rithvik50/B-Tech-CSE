module simple_circuit(A, B, C, D, E);
input A, B, C;
output D, E;
wire w1;
assign w1 = A & B;
assign E = ~C;
assign D = w1 | E;
endmodule