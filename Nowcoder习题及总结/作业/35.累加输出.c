#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }
    
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        int current_sum = 0; 
        for (int j = 1; j <= i; j++) {
            current_sum += j; 
        }
        sum += current_sum; 
    }
    
    printf("%d\n", sum);
    
    return 0;
}