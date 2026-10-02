#include <stdio.h>

int main() 
{
    int a, b,c;
    scanf("%d %d %d",&a,&b,&c);
    int d, e;
    d=2*(a*b+b*c+c*a);
    e=a*b*c;
    printf("%d\n%d",d,e);
    return 0;
}