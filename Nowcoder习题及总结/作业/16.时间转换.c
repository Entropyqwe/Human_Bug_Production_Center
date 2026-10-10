#include <stdio.h>

int main() {
    int a,b,c,d;
    scanf("%d",&a);
    b=a/3600;
    c=(a-3600*b)/60;
    d=(a-3600*b)%60;

    printf("%d %d %d",b,c,d);
    return 0;
}