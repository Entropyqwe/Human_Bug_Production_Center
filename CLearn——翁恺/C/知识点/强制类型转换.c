#include <stdio.h>

int main() {
    // 1. 避免整数除法陷阱（最常用）
    int a = 5, b = 2;
    double result;
    result = (double)a / b; 
    printf("1. 避免整数除法陷阱: %d / %d = %.1f\n", a, b, result);

    // 2. 浮点数转整数（注意精度丢失）
    float f = 9.57f; // 加上 f 后缀表示 float 类型，避免编译器警告
    int i;
    i = (int)f; 
    printf("2. 浮点数转整数: %.2f 转换为整数后 = %d\n", f, i);

    // 3. 对表达式进行强制转换（注意括号的使用）
    int x = 10, y = 3;
    double avg;
    // 正确写法：先将(x+y)的结果转换为double，再除以2
    avg = (double)(x + y) / 2; 
    printf("3. 表达式整体转换: (%d + %d) / 2 的正确结果 = %.1f\n", x, y, avg);

    // 4. 演示错误写法（对比参考）
    double avg_wrong;
    avg_wrong = (double)x + y / 2; // 只有x被转换，y/2仍按整数除法计算
    printf("   表达式错误写法对比: (double)%d + %d / 2 的结果 = %.1f\n", x, y, avg_wrong);

    return 0;
}