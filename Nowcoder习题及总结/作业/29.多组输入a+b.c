#include <stdio.h>

int main() {
    int T; // 用于存储数据组数
    // 读取组数 T
    scanf("%d", &T);
    
    // 循环 T 次，处理每组数据
    for (int i = 0; i < T; i++) {
        int a, b;
        // 读取每组的两个整数 a 和 b
        scanf("%d %d", &a, &b);
        
        // 计算和并输出，结果后加换行符
        printf("%d\n", a + b);
    }
    
    return 0;
}