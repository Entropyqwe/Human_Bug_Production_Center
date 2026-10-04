#include <stdio.h>

int main() {
    int n;
    // 读取输入的 n
    if (scanf("%d", &n) != 1) {
        return 1;
    }
    
    int sum = 0; // 总结果
    for (int i = 1; i <= n; i++) {
        int current_sum = 0; // 当前括号内的和
        for (int j = 1; j <= i; j++) {
            current_sum += j; // 累加 1 到 i
        }
        sum += current_sum; // 将当前括号的和加到总结果中
    }
    
    // 输出结果
    printf("%d\n", sum);
    
    return 0;
}