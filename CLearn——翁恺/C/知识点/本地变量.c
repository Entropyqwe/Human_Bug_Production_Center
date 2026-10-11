//*变量的生存期与作用域
//*生存期：什么时候变量开始出现，到什么时候消亡
//*作用域：在代码什么范围内可以访问这个变量
//*对于本地变量，这两个答案一样，均为大括号内的部分
#include<stdio.h>
void swap(int a,int b)
{
    int t=a;
    a=b;
    b=t;
}
int main(void)
{
    int a=5;
    int b=6;

    swap(a,b);
    printf("a=%d,b=%d\n",a,b);

    return 0;
}