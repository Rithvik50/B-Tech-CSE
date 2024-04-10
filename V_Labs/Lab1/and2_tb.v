module and2_test;
reg a, b;
wire c;
and and2_test(c, a, b);
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
        $dumpfile ("and2_test.vcd");
        $dumpvars (0, and2_test);
    end
endmodule

//Command lines to run verilog code:
    //iverilog -o test and2.v and2_tb.v
    //vvp test
    //gtkwave and2_test.vcd