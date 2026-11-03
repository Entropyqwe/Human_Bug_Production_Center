#include <stdio.h>

    int avg(int a,int b,int c){
        return (a+b+c)/3;
    }
    int main(){
        int a,b,c;
        printf("请输入三个整数：");
        scanf("%d %d %d",&a,&b,&c);
        printf("平均数为：%d\n",avg(a,b,c));
        return 0;
    }
