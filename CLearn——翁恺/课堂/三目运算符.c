#include<stdio.h>
int main(void){
    int a,b;
    printf("请输入两个数：");
    scanf("%d %d",&a,&b);
    printf("最大的数为:%d\n",a>b?a:b);
    return 0;
}