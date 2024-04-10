module xnor2_test;
reg a, b;
wire c;
xnor xnor2_test(c, a, b);
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
        $dumpfile ("xnor2_test.vcd");
        $dumpvars (0, xnor2_test);
    end
endmodule