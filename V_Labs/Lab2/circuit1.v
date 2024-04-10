module circuit1(A, B, C, Y);
input A, B, C;
output Y;
wire w1;
assign w1 = B & C;
assign Y = A | w1;
endmodule