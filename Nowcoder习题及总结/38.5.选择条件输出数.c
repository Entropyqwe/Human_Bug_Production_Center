#include <stdio.h>

// 辅助函数：判断数字 n 是否包含 4
// 如果包含返回 1 (真)，否则返回 0 (假)
int hasFour(int n) {
    // 处理负数情况（虽然题目说是正整数，但养成好习惯）
    if (n < 0) n = -n;

    while (n > 0) {
        int digit = n % 10; // 取出最后一位
        if (digit == 4) {
            return 1;       // 发现 4，立即返回真
        }
        n /= 10;            // 去掉最后一位
    }
    return 0;               // 循环结束没发现 4，返回假
}

int main() {
    int n;
    // 1. 读取输入的 n
    if (scanf("%d", &n) != 1) return 0;

    // 2. 遍历 1 到 n
    for (int i = 1; i <= n; i++) {
        // 条件 A: 不是 4 的倍数 (i % 4 != 0)
        // 条件 B: 不包含数字 4 (!hasFour(i))
        // 两个条件必须同时满足 (&&)
        if ((i % 4 != 0) && (!hasFour(i))) {
            printf("%d\n", i);
        }
    }

    return 0;
}