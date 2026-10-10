#include <stdio.h>

int main() {
    int n;
    int a[105];
    int count = 0; 

    while (scanf("%d", &n) == 1 && n != 0) {
        a[count] = n; 
        count++;      
    }

    for (int i = count - 1; i >= 0; i--) {
        printf("%d", a[i]);
 
        if (i > 0) {
            printf(" ");
        }
    }

    // 很多在线判题系统要求最后有一个换行符
    printf("\n");

    return 0;
}