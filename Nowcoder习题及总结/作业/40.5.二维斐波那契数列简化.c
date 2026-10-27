#include <stdio.h>

#define MOD 1000000007
//*全局变量必须要设置在主函数以外，防止栈溢出
long long dp[1005][1005]; 

int main() {
    int n, m;
    if (scanf("%d %d", &n, &m) != 2) return 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (i == 1 && j == 1) {
                dp[i][j] = 1;
            } 
            else if (i == 1) {
                dp[i][j] = dp[i][j-1];
            } 
            else if (j == 1) {
                dp[i][j] = dp[i-1][j];
            } 
            else {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
                //*由于只有第四种可能性会产出锌树脂，所以只有最后一种需要取余
            }
        }
    }

    printf("%lld\n", dp[n][m]);

    return 0;
}