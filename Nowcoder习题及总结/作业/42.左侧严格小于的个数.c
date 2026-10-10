#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); 

    int a[105]; 
    for (int i = 1; i <= n; i++) {
        scanf("%d", &a[i]);
    }

    for (int i = 1; i <= n; i++) {
        int count = 0; 
        for (int j = 1; j < i; j++) {
            if (a[j] < a[i]) {
                count++;
            }
        }
        printf("%d", count);
        if (i < n) {
            printf(" "); 
        }
    }
    printf("\n"); 

    return 0;
}