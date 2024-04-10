module a_segment(input wire a, b, c, d, output wire out); //a_segment = a + c + bd + b'd'
    wire t0, t1, t2;
    and2 a0(b, d, t1);
    and2 a1(!b, !d, t2);
    or2 o0(a, c, t0);
    or3 o1(t0, t1, t2, out);
endmodule

module b_segment(input wire a, b, c, d, output wire out); //b_segment = b' + c'd' + cd
    wire t0, t1;
    and2 a0(!c, !d, t0);
    and2 a1(c, d, t1);
    or3 o1(!b, t0, t1, out);
endmodule

module c_segment(input wire a, b, c, d, output wire out); //c_segment = b + c' + d
    or3 o0(b, !c, d, out);
endmodule

module d_segment(input wire a, b, c, d, output wire out); //d_segment = b'd' + cd' + bc'd + b'c + a
    wire t0, t1, t2, t3, t4;
    and2 a0(!b, !d, t0);
    and2 a1(c, !d, t1);
    and3 a2(b, !c, d, t2);
    and2 a3(!b, c, t3);
    or3 o0(t0, t1, t2, t4);
    or3 o1(t4, t3, a, out);
endmodule

module e_segment(input wire a, b, c, d, output wire out); //e_segment = b'd' + cd'
    wire t0, t1;
    and2 a0(!b, !d, t0);
    and2 a1(c, !d, t1);
    or2 o0(t0, t1, out);
endmodule

module f_segment(input wire a, b, c, d, output wire out); //f_segment = a + c'd' + bc' + bd'
    wire t0, t1, t2, t3;
    and2 a0(!c, !d, t0);
    and2 a1(b, !c, t1);
    and2 a2(b, !d, t2);
    or3 o0(t0, t1, t2, t3);
    or2 o1(a, t3, out);
endmodule

module g_segment(input wire a, b, c, d, output wire out); //g_segment = a + bc' + b'c + cd'
    wire t0, t1, t2, t3;
    and2 a0(!b, c, t0);
    and2 a1(c, !d, t1);
    and2 a2(b, !c, t2);
    or3 o0(t0, t1, t2, t3);
    or2 o1(a, t3, out);
endmodule

module seven_segment(input wire [0:3] i);
    wire a_out, b_out, c_out, d_out, e_out, f_out, g_out;
    a_segment a_seg(i[0], i[1], i[2], i[3], a_out);
    b_segment b_seg(i[0], i[1], i[2], i[3], b_out);
    c_segment c_seg(i[0], i[1], i[2], i[3], c_out);
    d_segment d_seg(i[0], i[1], i[2], i[3], d_out);
    e_segment e_seg(i[0], i[1], i[2], i[3], e_out);
    f_segment f_seg(i[0], i[1], i[2], i[3], f_out);
    g_segment g_seg(i[0], i[1], i[2], i[3], g_out);
endmodule