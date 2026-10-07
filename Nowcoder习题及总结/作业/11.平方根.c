#include <stdio.h>
#include <math.h>

int main() {
    double a;
    double b;
    scanf("%lf",&a);
    b=sqrt(a);
    //int c=b/1;
    int c=(int)b;//直接通过强行类型转换来取到整数部分
    printf("%d\n",c);
    return 0;
}