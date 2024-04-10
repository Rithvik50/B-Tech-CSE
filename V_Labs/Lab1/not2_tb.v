module not2_test;
reg a;
wire b;
not not2_test(b, a);
initial 
    begin
        #000 a = 0;
        #100 a = 1;
    end
initial
    begin
        $monitor($time,"a = %b b = %b", a, b);
    end
initial
    begin
        $dumpfile ("not2_test.vcd");
        $dumpvars (0, not2_test);
    end
endmodule