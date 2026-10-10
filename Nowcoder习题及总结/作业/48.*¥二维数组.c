#include <stdio.h>

int main() {
    int n, m;
    long long sum = 0; 
    int temp;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {//*从第一行开始
        for (int j = 0; j < m; j++) {//*只有输出一整个数列后才停止
            scanf("%d", &temp);
            sum += temp; 
        }
    }

    printf("%lld\n", sum);

    return 0;
}