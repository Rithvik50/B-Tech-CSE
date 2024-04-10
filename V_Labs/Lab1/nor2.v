module nor2(c, a, b);
input a, b;
output c;
assign c = !(a | b);
endmodule