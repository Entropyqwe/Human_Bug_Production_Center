#include<stdio.h>

int main(){
    int num1,num2;
    printf("请输入两个整数：");
    scanf("%d%d",&num1,&num2);
    printf("和为：%d\n",num1+num2);
    printf("差为：%d\n",num1-num2);
    printf("积为：%d\n",num1*num2);
    printf("商为：%f\n",(float)num1/(float)num2);//加上float就是强制类型转换
    printf("余为：%d\n",num1%num2);
    
}