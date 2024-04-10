module or2_test;
reg a, b;
wire c;
or or2_test(c, a, b);
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
        $dumpfile ("or2_test.vcd");
        $dumpvars (0, or2_test);
    end
endmodule