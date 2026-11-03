//要求输出所有三位的水仙花数
#include<stdio.h>

int main(void){
    int a,b,c;
    for(int n=100;n<=999;n++){
        int z=n;
        a=z%10;
        b=z/10%10;
        c=z/10%10;
        if(n==a*a*a+b*b*b+c*c*c){
            printf("%d\n",n);
        }
    }
    return 0;
}