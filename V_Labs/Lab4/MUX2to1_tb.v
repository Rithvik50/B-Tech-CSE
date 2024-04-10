module TB;
reg A, B, S;
wire X;
mux2 newMUX(.i0(A), .i1(B), .j(S), .o(X));
initial
    begin
        B = 1'b0; A = 1'b0; S = 1'b0; #5
        B = 1'b0; A = 1'b0; S = 1'b1; #5
        B = 1'b0; A = 1'b1; S = 1'b0; #5
        B = 1'b0; A = 1'b1; S = 1'b1; #5
        B = 1'b1; A = 1'b0; S = 1'b0; #5
        B = 1'b1; A = 1'b0; S = 1'b1; #5
        B = 1'b1; A = 1'b1; S = 1'b0; #5
        B = 1'b1; A = 1'b1; S = 1'b1;
    end
initial
    begin
        $monitor($time, "B = %b, A = %b, S = %b, X = %b", B, A, S, X);
    end
initial 
    begin
        $dumpfile("MUX2to1_test.vcd");
        $dumpvars(0, TB);
    end
endmodule