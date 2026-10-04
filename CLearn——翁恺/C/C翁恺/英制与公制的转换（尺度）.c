#include <stdio.h>
int main(){
    printf("请分别输入身高的英尺和英寸：");
    int foot;
    float inch;

     scanf("%d %f",&foot,&inch);//定义时为什么要加&
     printf("身高是%.2f米。\n",(foot+inch/12)*0.3048);

    return 0;
}
