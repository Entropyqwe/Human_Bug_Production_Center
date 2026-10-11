//总值与次数的计算，设置循环，存在的变量有输入值，总值，已经输入的次数
#include<stdio.h>
    int main()
{
    int a=0; //*输入值
    int sum=0; //*总值
    int count=0; //*次数
    do{
        printf("请输入一个整数（输入0结束）：");
        scanf("%d",&a);
        sum+=a;
        count++;
    }while(a!=0);
    printf("总值为：%d\n",sum);
    printf("次数为：%d\n",count-1); //*减去最后一次输入的0
    return 0;
}