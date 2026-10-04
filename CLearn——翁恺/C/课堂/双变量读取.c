#include <stdio.h>
int main()
{
    int a = 0;
    int b = 0;

    printf("请输入两个整数:");
    scanf("%d %d",&a,&b);//这里输入的就是空格，下方终端运行时也需要做空格处理1 4

    printf("%d+%d = %d\n",a,b,a+b);

    return 0 ;
}