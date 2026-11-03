#include<stdio.h>

int main(void){
    int n;
    int count=0;
    printf("请输入一个数：");
    scanf("%d",&n);

do{
    if(n%2==0){
        n=n/2;
        printf("%d,%d\n",++count,n);
    }else{
        n=n*3+1;
        printf("%d %d\n",++count,n);
    }
}while (n!=1);
return 0;
}