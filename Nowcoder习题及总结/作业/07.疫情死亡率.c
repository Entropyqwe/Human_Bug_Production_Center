#include <stdio.h>

int main() {
    int c,d;
    printf("请输入数据：");
    scanf("%d %d",&c,&d);
    double a=1.0*d/c*100;
    printf("%.2f%%",a);
    return 0;
}