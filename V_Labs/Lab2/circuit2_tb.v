module circuit2_tb;
reg A, B, C;
wire Y;
circuit2 M1(A, B, C, Y);
initial
    begin
        A=1'b0 ; B=1'b0 ; C=1'b0; #20
        A=1'b0 ; B=1'b0 ; C=1'b1; #20
        A=1'b0 ; B=1'b1 ; C=1'b0; #20
        A=1'b0 ; B=1'b1 ; C=1'b1; #20
        A=1'b1 ; B=1'b0 ; C=1'b0; #20
        A=1'b1 ; B=1'b0 ; C=1'b1; #20
        A=1'b1 ; B=1'b1 ; C=1'b0; #20
        A=1'b1 ; B=1'b1 ; C=1'b1;
    end
initial
    begin
    $monitor($time, "A2 = %b B2 = %b C2 = %b Y = %b", A, B, C, Y);
    end
initial
    begin
        $dumpfile ("circuit2_test.vcd");
        $dumpvars (0, circuit2_tb);
    end
endmodule
