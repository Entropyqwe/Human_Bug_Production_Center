#include<stdio.h>
    int main()
{
    int a=0; //*输入值
    int sum=0; //*总值
    int count=0; //*次数
    printf("请输入整数，输入0结束\n");
    scanf("%d",&a);//输入值
    while(a!=0){
        sum+=a;//意思是此处总值等于总值加上输入值
        count++;//意思是此处次数等于次数加1
        scanf("%d",&a);//次数再次输入输入值再次进入到循环
    }
    printf("%.2f\n",1.0*sum/count);//此处乘上1.0位的是强行将式子改为浮点数运算
    /*方式二
    float a=0;
    float sum=0;
    int count=0
    ........
    printf("%.2f",sum/count)*/
    return 0;
}