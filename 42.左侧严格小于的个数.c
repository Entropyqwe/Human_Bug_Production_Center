#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); // 读取序列长度

    int a[105]; // 存储序列 a，下标从 1 开始
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }

    for (int i = 1; i <= n; i++) {
        int count = 0; // 用于统计左侧小于 a[i] 的个数
        // 遍历 i 左侧的所有元素
        for (int j = 1; j < i; j++) {
            if (a[j] < a[i]) {
                count++;
            }
        }
        printf("%d", count);
        if (i < n) {
            printf(" "); // 空格分隔
        }
    }
    printf("\n"); // 换行

    return 0;
}