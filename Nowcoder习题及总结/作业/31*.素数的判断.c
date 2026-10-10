#include <stdio.h>
#include <math.h> // 引入数学库，用于计算平方根

int isPrime(int n) {
    if (n <= 1) {
        return 0; // 1 及以下的数不是素数
    }
    if (n == 2) {
        return 1; // 2 是素数
    }
    int sqrtN = sqrt(n); // 计算 n 的平方根
    for (int i = 2; i <= sqrtN; i++) {
        if (n % i == 0) {
            return 0; // 找到能整除的数，不是素数
        }
    }
    return 1; // 没有找到能整除的数，是素数
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        if (isPrime(n)) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
    return 0;
}