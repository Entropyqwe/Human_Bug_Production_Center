#include <stdio.h>
int main(void){
int a=1,b=2;
a=a^b;
b=b^a;
a=b^a;
printf("%d %d\n",a,b);
return 0;
}

//原理：按照二进制表达数字
/*  a       b       
    01      10
    a 01
    b 10
    a1 00
    b  10
    b1 00
    b2 01
    a2 10
    */