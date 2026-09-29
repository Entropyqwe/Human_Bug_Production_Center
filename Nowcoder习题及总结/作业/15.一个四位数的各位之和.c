#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int a = n % 10;       
    int b = (n / 10) % 10; 
    int c = (n / 100) % 10; 
    int d = n / 1000;   
    
    int sum = a + b + c + d;
    
    printf("%d\n", sum);
    
    return 0;
}