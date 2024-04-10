module halfadd(a, b, sum, cout);
input a, b;
output sum, cout;
xor x0(sum, a, b);
and a0(cout, a, b);
endmodule