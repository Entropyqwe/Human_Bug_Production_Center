//目标：将两个变量中的内容交换一下
//*写程序是描述动作的过程,重点的操作是赋值=前面的被赋值为了后面一个
//*参与到赋值操作中的变量将再次变为可赋值状态，例：a=v，此时v空置，可使v=c
#include<stdio.h>
    int main(){
        int a=5;
        int b=6;
        int t;
        t=a;
        a=b;
        b=t;//*此时a已经被赋值为b了，想要将b赋值为原本a的值，应该从t上取，即b=t
        printf("a=%d,b=%d\n",a,b);

        return 0;

    }