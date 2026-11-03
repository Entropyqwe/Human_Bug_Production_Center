#include <stdio.h>

int main() {
    int i;            
    int asum = 0;  
    int bsum = 0; 

    for (i = 1; i <= 100; i++) {
        if (i % 2 != 0) { 
            asum += i; 
        } else {
            bsum += i; 
        }
    }
    printf("1到100之间奇数的总和为：%d\n", asum);
    printf("1到100之间偶数的总和为：%d\n", bsum);

    return 0;
}