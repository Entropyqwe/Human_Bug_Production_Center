#include <stdio.h>

int main() {
    int a;
    long long b; // 注意：10^18 超出了 int 范围，必须用 long long
    double c;
    char d;
    char e[100]; // 字符串需要定义为数组

    // 依次读取整数、长整数、浮点数、字符、字符串
    scanf("%d %lld %lf %c %s", &a, &b, &c, &d, &e);
//*e代表的是一个字符串（string),所以%d是专门读取和输出字符串的符号
    // 按要求输出，浮点数保留一位小数
    printf("%d\n%lld\n%.1f\n%c\n%s\n", a, b, c, d, e);

    return 0;
}