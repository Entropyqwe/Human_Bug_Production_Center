#include <stdio.h>

// 定义一个函数：判断 n 是否包含 4
// 如果包含返回 1 (真)，否则返回 0 (假)
int hasFour(int n) {
    // 1. 处理负数：取绝对值（防止 -42 这种情况漏判）
    if (n < 0) {
        n = -n;
    }

    // 特殊情况：如果输入本身就是 0，肯定不含 4
    if (n == 0) return 0;

    // 2. 循环拆解每一位
    while (n > 0) {
        int digit = n % 10; // 取出最后一位

        if (digit == 4) {   // 检查这一位是不是 4
            return 1;       // 是！直接返回 1，不需要再查了
        }

        n /= 10;            // 去掉最后一位，继续查下一位
    }

    return 0; // 循环结束了都没找到 4，返回 0
}

int main() {
    int num;
    printf("请输入一个整数: ");
    scanf("%d", &num);

    if (hasFour(num==1)) {
        printf("包含数字 4\n");
    } else {
        printf("不包含数字 4\n");
    }

    return 0;
}