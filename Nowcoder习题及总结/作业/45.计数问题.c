#include <stdio.h>
//*核心思想：检查每一位上的数字
int main() {
    int n, x;
    scanf("%d %d", &n, &x); 

    int count = 0; 

    for (int i = 1; i <= n; i++) {//遍历思想
        int temp = i; 
        while (temp > 0) {
            if (temp % 10 == x) {//检查每一次变化后的个位数字
                count++; 
            }
            temp /= 10; //赋值算法
        }
    }

    printf("%d\n", count); 

    return 0;
}