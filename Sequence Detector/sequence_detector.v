module dffo (D, Q, Qn, C);
input D, C; output Q, Qn;
wire D, C, Q, Qn, n1n3, Cn, n2n4, n3n5, n4n3, n5n7, n6n8;
nand n1(n1n3, D, C);
nand n2(n2n4, n1n3, C);
nand n3(n3n5, n1n3, n4n3);
nand n4(n4n3, n2n4, n3n5);
nand n5(n5n7, n3n5, Cn);
nand n6(n6n8, n5n7, Cn);
nand n7(Q, n5n7, Qn);
nand n8(Qn, n6n8, Q);
not n0(Cn, C);
endmodule

module sequence_detector(X,Y,Clk ,Cout);
input X, Clk; output Y, Cout;
wire X, Clk, Y, dff1i, dff2i, dff3i, Xn, d1n1o, d1n2o, d1n3o, d2n1o, d2n2o, d2n3o, d3n1o, d3n2o, d3n3o, Q1, Qn1, Q2, Qn2, Q3, Qn3, Cout, y1o, y2o; 
dffo ff1(dff1i, Q1, Qn1, Clk);
dffo ff2(dff2i, Q2, Qn2, Clk);
dffo ff3(dff3i, Q3, Qn3, Clk);
not n1(Xn, X);

nand d3n1(d3n1o, Xn, Q3, Qn2, Q1);
nand d3n2(d3n2o, X, Qn3, Q2, Q1);
nand d3n3(d3n3o, X, Q3, Qn1);
nand d3nf(dff3i, d3n1o, d3n2o, d3n3o);

nand d2n1(d2n1o, Qn3, Q2, Qn1);
nand d2n2(d2n2o, Qn2, Q1, Q3);
nand d2n3(d2n3o, Qn2, Q1, X);
nand d2nf(dff2i, d2n1o, d2n2o, d2n3o);

nand d1n1(d1n1o, X, Qn2, Qn1);
nand d1n2(d1n2o, Q3, Q2, Q1, X);
nand d1n3(d1n3o, Xn, Qn3, Q2, Qn1);
nand d1nf(dff1i, d1n1o, d1n2o, d1n3o);

nand y1(y2o, Q3, Q2, Qn1);
nand yf(Y, y2o);

and CO(Cout, Clk, Clk);
endmodule
