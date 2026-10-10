#include <stdio.h>

int main() {
    long long a; //* 使用 long long 防止大数溢出
    scanf("%lld", &a); //* 对应 long long 使用 %lld

    if (a < 10) {
        printf("0\n");
    } else {
        //* 核心算法：先除10去掉个位，再模10取个位
        printf("%lld\n", (a / 10) % 10);
    }

    return 0;
}