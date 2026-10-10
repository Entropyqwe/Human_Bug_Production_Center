#include <stdio.h>

// 将数组定义在 main 外部，防止栈溢出，且大小要满足题目 n<=100000 的要求
int a[100005];

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    while (T--) {
        int n;
        scanf("%d", &n);

        long long sum = 0; 
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]); 
            sum += a[i];
        }

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


        int range = max_val - min_val;

        double average = (double)sum / n;
        double sum = 0.0;

        for (int i = 0; i < n; i++) {
            double diff = a[i] - average;
            sum += diff * diff;
        }

        double var = sum / n;

        printf("%d %.3f\n", range, var);
    }

    return 0;
}