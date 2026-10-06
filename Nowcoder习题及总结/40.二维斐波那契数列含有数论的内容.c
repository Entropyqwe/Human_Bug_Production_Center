#include <stdio.h>

// 定义模数，题目要求对 10^9 + 7 取模
#define MOD 1000000007
// 定义最大范围，n,m最大1000，所以 n+m-2 最大约为 2000，我们开大一点防止越界
#define MAXN 2005

long long fact[MAXN];      // 存储阶乘 fact[i] = i! % MOD
long long inv_fact[MAXN];  // 存储阶乘的逆元

// 快速幂函数：计算 (base^exp) % mod
// 用于计算逆元，根据费马小定理，a的逆元是 a^(mod-2)
long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) { // 如果指数是奇数，乘一次底数
            res = (res * base) % MOD;
        }
        base = (base * base) % MOD; // 底数平方
        exp /= 2; // 指数减半
    }
    return res;
}

// 预处理函数：提前算好所有需要的阶乘和逆元
void precompute() {
    // 1. 计算阶乘
    fact[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        fact[i] = (fact[i-1] * i) % MOD;
    }

    // 2. 计算阶乘的逆元
    // 先算出最大数的阶乘逆元
    inv_fact[MAXN-1] = power(fact[MAXN-1], MOD - 2);
    // 倒推回去：(i-1)!的逆元 = i!的逆元 * i
    for (int i = MAXN - 2; i >= 0; i--) {
        inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD;
    }
}

int main() {
    // 先进行预处理，这样后面查询就是 O(1) 复杂度
    precompute();

    int n, m;
    // 读取输入
    if (scanf("%d %d", &n, &m) != 2) return 0;

    // 根据推导公式：结果是 C(n+m-2, n-1)
    int total = n + m - 2; // 组合数的上标 N
    int select = n - 1;    // 组合数的下标 K

    // 利用公式 C(N, K) = N! * inv(K!) * inv((N-K)!) % MOD
    long long ans = fact[total];
    ans = (ans * inv_fact[select]) % MOD;
    ans = (ans * inv_fact[total - select]) % MOD;

    printf("%lld\n", ans);

    return 0;
}
