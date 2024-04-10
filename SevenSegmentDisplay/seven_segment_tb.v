module seven_segment_tb;
    reg [0:3] ii;
    seven_segment seven_segment_display(.i(ii));
    initial
        begin
            ii = 4'b0000;#5
            ii = 4'b0001;#5
            ii = 4'b0010;#5
            ii = 4'b0011;#5
            ii = 4'b0100;#5
            ii = 4'b0101;#5
            ii = 4'b0110;#5
            ii = 4'b0111;#5
            ii = 4'b1000;#5
            ii = 4'b1001;#5
            ii = 4'b0000;
        end
    initial
        begin
            $dumpfile ("seven_segment_test.vcd");
            $dumpvars (0, seven_segment_tb);
        end
endmodule