#include <stdio.h>

int main() {
    int a, b;
    printf("请输入两个整数:");
    scanf("%d %d",&a,&b);
    int c=a/b;
    int d=a%b;
    printf("%d %d",c,d);

    return 0;
}