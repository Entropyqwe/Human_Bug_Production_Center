#include <stdio.h>

int main() {
    int a, b;
    // 循环读取输入，直到遇到 a = 0 且 b = 0 时结束
    while (scanf("%d %d", &a, &b) != EOF) {
        // 判断结束条件
        if (a == 0 && b == 0) {
            break; // 跳出循环，不再处理该组
        }
        // 计算并输出和
        printf("%d\n", a + b);
    }
    return 0;
}