#include <stdio.h>

int hasFour(int n) {//*定义一个叫做hasfour的函数，这个函数只能用来存储int类型
    //* 处理负数情况
    if (n < 0) n = -n;

    while (n > 0) {
        int digit = n % 10; 
        if (digit == 4) {
            return 1;       
        }
        n /= 10;            
    }
    return 0;               
}

int main() {
    int n;
   
    if (scanf("%d", &n) != 1) return 0;

   
    for (int i = 1; i <= n; i++) {
        if ((i % 4 != 0) && (!hasFour(i))) {
            printf("%d\n", i);
        }
    }

    return 0;
}