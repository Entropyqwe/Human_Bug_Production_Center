#include <stdio.h>

// 定义模数，这是一个常用的大质数
#define MOD 1000000007

// 定义数组大小，题目说 n,m <= 1000，我们开稍微大一点防止越界
// 注意：全局变量数组开在 main 外面，防止栈溢出
long long dp[1005][1005]; 

int main() {
    int n, m;
    // 读取输入
    if (scanf("%d %d", &n, &m) != 2) return 0;

    // 开始填表
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // 情况1：起点
            if (i == 1 && j == 1) {
                dp[i][j] = 1;
            } 
            // 情况2：第一行（只能从左边来）
            else if (i == 1) {
                dp[i][j] = dp[i][j-1];
            } 
            // 情况3：第一列（只能从上面来）
            else if (j == 1) {
                dp[i][j] = dp[i-1][j];
            } 
            // 情况4：中间格子（从上面来 + 从左边来）
            else {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
            }
        }
    }

    // 输出右下角的结果
    printf("%lld\n", dp[n][m]);

    return 0;
}