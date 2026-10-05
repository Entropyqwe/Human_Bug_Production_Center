#include <stdio.h>
#include <math.h> // 引入数学库以使用 abs 函数，或者手动处理负数

int main() {
    int n; 
    while (scanf("%d", &n) != EOF) {

        if (n < 0) {
            n = -n;
        }

        int sum = 0; // 用于存储数位之和

        if (n == 0) {
            printf("0\n");
        }

        while (n > 0) {
            sum += n % 10; // 取出最后一位加到 sum 中
            n /= 10;       // 去掉最后一位
        }

        // 4. 输出结果
        printf("%d\n", sum);
    }
    return 0;
}