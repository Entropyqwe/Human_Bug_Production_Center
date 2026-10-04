//根据原本的关于计算时间差的练习，接下来我们考虑不换算直接进行加减的方式
//直接换用if语句来判定是否借位进行计算
#include<stdio.h>
int main(){
    int hour1,minute1;
    int hour2,minute2;

    scanf("%d %d",&hour1,&minute1);
    scanf("%d %d",&hour2,&minute2);
    
    int ih=hour2-hour1;
    int im=minute2-minute1;
    if(im<0){//给予判断条件
        im=60+im;
        ih--;//小时部分的差值减去一，用于实现借位操作
    }//使用中括号进行位置判断

    printf("时间是%d小时%d分.\n",ih,im);
}