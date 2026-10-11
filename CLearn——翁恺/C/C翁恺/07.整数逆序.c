//输入一个整数，通过整除逆序输出该整数的每一位数字
#include <stdio.h>

int main()
{
    int x;
    printf("请输入一个整数：");
    scanf("%d", &x);
    int digit;
    int ret=0;

    while(x!=0)//当x不等于0时，继续循环
    {
        digit=x%10;//取出最后一位数字,此处的意思是取出x的个位数字（即x除以10的余数）
        printf("%d\n", digit);
        ret=ret*10+digit;//采用赋值符号，因为是将数字倒着输出，经过如下
        //例如：1234，第一次循环ret=0*10+4=4，第二次循环ret=4*10+3=43，第三次循环ret=43*10+2=432，第四次循环ret=432*10+1=4321
        printf("x=%d,digit=%d,ret=%d\n", x,digit,ret);
        x/=10;//由于这种出发只会保留整数，当x变为个位数时，输出的只会是0，这种情况下循环结束
    }
    printf("逆序后的整数是：%d\n", ret);
    return 0;
}