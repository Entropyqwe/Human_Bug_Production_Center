#include<stdio.h>
int main(void){
    int a,b,c;
    a=5,b=6,c=11;
    printf("%d",(a>b)&&(++b<c));
    printf("%d\n",b);
}