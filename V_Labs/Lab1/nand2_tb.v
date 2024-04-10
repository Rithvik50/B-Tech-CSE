module nand2_test;
reg a, b;
wire c;
nand nand2_test(c, a, b);
initial 
    begin
        #000 a = 0; b = 0;
        #100 a = 0; b = 1;
        #100 a = 1; b = 0;
        #100 a = 1; b = 1;
    end
initial
    begin
        $monitor($time,"a = %b b = %b c = %b", a, b, c);
    end
initial
    begin
        $dumpfile ("nand2_test.vcd");
        $dumpvars (0, nand2_test);
    end
endmodule