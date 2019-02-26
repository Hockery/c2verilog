module simple_register(in, out, clr_n, clk, a);

    //端口声明
    input clr_n;
    input clk;
    input [7:0] in;
    input a;
    output [7:0] out;

    //信号声明
    reg [7:0] out;
    wire a;

    //实现带异步清除的寄存器
    always @(posedge clk or negedge clr_n)
    begin
        if (clr_n==0) // could also be written if (!clr_n)
            out<=0;
        else
            out<=in;
    end

    //连续赋值
    assign a=!out[0];
endmodule