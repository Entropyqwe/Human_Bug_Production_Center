//*思路：通过假设法定义最大最小值，每一个循环都进行比较，最后输出值即可
#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); // 读取数字个数 n

    int max_val, min_val;
    int a;

    // 读取第一个数，作为初始的最大值和最小值
    scanf("%d", &a);
    max_val = a;
    min_val = a;

    // 循环读取剩下的 n-1 个数
    for (int i = 2; i <= n; i++) {
        scanf("%d", &a);
        if (a > max_val) {
            max_val = a; // 更新最大值
        }
        if (a < min_val) {
            min_val = a; // 更新最小值
        }
    }

    // 输出最大差值
    printf("%d\n", max_val - min_val);

    return 0;
}