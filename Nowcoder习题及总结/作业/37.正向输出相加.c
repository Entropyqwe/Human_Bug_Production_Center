#include <stdio.h>
#include <math.h> 

int main() {
    int n; 
    while (scanf("%d", &n) != EOF) {

        if (n < 0) {
            n = -n;
        }
        int sum = 0; 

        if (n == 0) {
            printf("0\n");
        }
        while (n > 0) {
            sum += n % 10; 
            n /= 10;       
        }
        printf("%d\n", sum);
    }
    return 0;
}