module fulladd_tb;
reg aa, bb, cc;
wire ss, cy;
fulladd add1(.a(aa), .b(bb), .cin(cc), .sum(ss), .cout(cy));
initial
    begin
        aa = 1'b0; bb = 1'b0; cc = 1'b0; #5
        aa = 1'b0; bb = 1'b0; cc = 1'b1; #5
        aa = 1'b0; bb = 1'b1; cc = 1'b0; #5
        aa = 1'b0; bb = 1'b1; cc = 1'b1; #5
        aa = 1'b1; bb = 1'b0; cc = 1'b0; #5
        aa = 1'b1; bb = 1'b0; cc = 1'b1; #5
        aa = 1'b1; bb = 1'b1; cc = 1'b0; #5
        aa = 1'b1; bb = 1'b1; cc = 1'b1;
    end
initial
    begin
        $monitor($time,"a = %b b = %b c = %b sum = %b carry = %b", aa, bb, cc, ss, cy);
    end
initial
    begin
        $dumpfile ("fulladd_test.vcd");
        $dumpvars (0, fulladd_tb);
    end
endmodule