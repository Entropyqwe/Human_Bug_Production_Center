#include<stdio.h>
int main(void){
    int x;
    int y=0;
    scanf("%d",&x);
    if(x<1){
        y=x;
    }else if(x>=1&&x<10){
        y=2*x-1;
    }else if(x>=10){
        y=3*x-11;
    }
    printf("函数值是：%d\n",y);
    return 0;
}