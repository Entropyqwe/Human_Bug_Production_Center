#include <stdio.h>
void f(int *p);
void g(int k);
int main(void)
{
int i= 6;
printf("&i=%p\n",&i);
f(&i);//这两个自定义函数包括了输出部分
g(i);
return 0;
}
void f(int *p)
{//定义函数
printf("p=%p\n",p);
printf("*p=%d\n",p);//针对的是*p这个整体，是整数形式
}
void g(int k)
{//定义函数
printf("k=%d\n",k);
}