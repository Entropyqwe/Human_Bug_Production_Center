#include <stdio.h>
#include <stdlib.h>//*引入随机数函数库，rand()函数用于生成随机数，srand()函数用于设置随机数种子，二者均在这个库中
#include <time.h>//*引入时间函数库，time()函数用于获取当前时间，作为随机数种子
int main()
{
    srand(time(0));//*设置随机数种子，以获取一个自1970开始的随机数，即伪随机
    int number=rand()%100+1; //*生成1-100之间的随机数
    int count=0; //*记录猜测次数
    int a=0; //*用户输入的猜测数
    do{ 
        printf("请输入你猜测的数字(1-100）:");
        scanf("%d",&a);
        count++;
        if(a>number){
            printf("你猜的数字太大了，请重新输入");
        }else if(a<number){
            printf("你猜的数字太小了，请重新输入");
        }
    }while(a!=number);

    printf("恭喜你猜对了，你一共猜了%d次",count);

    return 0;
}