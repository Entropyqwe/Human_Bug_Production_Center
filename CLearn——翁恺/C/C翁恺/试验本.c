#include <stdio.h>

int main(){
    
    int n;
    int i=1;
    int a;
    a=1;
    printf("请输入一个整数：");
    scanf("%d",&n);
    while(i<=n){
        a=a*i;
        i++;
    }
        printf("%d的阶乘为：%d",n,a);
        return 0;