#include <stdio.h>

// 将数组定义在 main 外部，防止栈溢出，且大小要满足题目 n<=100000 的要求
int a[100005];

int main() {
    int T;
    // 1. 读取测试组数
    if (scanf("%d", &T) != 1) return 0;

    // 2. 循环处理每一组试卷
    while (T--) {
        int n;
        scanf("%d", &n);

        long long sum = 0; // sum 可能会很大，用 long long 并初始化为 0
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]); // 注意这里必须有 &
            sum += a[i];
        }

        // 3. 寻找最大值和最小值
        // 初始化设为第一个元素，避免越界
        int max_val = a[0];
        int min_val = a[0];

        for (int i = 1; i < n; i++) {
            if (a[i] > max_val) {
                max_val = a[i];
            }
            if (a[i] < min_val) {
                min_val = a[i];
            }
        }

        // 4. 计算极差
        int range = max_val - min_val;

        // 5. 计算方差
        // 平均值必须是浮点数，否则整数除法会丢失精度
        double average = (double)sum / n;
        double variance_sum = 0.0;

        for (int i = 0; i < n; i++) {
            double diff = a[i] - average;
            variance_sum += diff * diff;
        }

        double variance = variance_sum / n;

        // 6. 输出结果：极差为整数，方差保留3位小数
        printf("%d %.3f\n", range, variance);
    }

    return 0;
}