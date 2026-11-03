#include<stdio.h>
int main(void){
    int num;
    printf("请输入一个三位数：");
    scanf("%d",&num);
    int a;
    for(int i=0;i<3;i++){
        a=num%10;
        num/=10;
        printf("%d",a);
    }
    printf("\n");
    return 0;
}