module fulladdR(input wire [3:0] a, b, input wire cin, output wire [3:0] sum, output wire cout);

wire [2:0] c;
  fulladd u0 (a[0], b[0], cin, sum[0], c[0]);
  fulladd u1 (a[1], b[1], c[0], sum[1], c[1]);
  fulladd u2 (a[2], b[2], c[1], sum[2], c[2]);
  fulladd u3 (a[3], b[3], c[2], sum[3], cout);

endmodule 


    
