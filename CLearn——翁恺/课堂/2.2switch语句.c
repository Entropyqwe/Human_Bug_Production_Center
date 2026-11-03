//switch case每一次只针对执行一个语句
#include<stdio.h>

int main(void){
    int num;
    printf("**自动售货机**\n");
    printf("****1.可乐****\n");
    printf("****2.雪碧****\n");
    printf("****3.咖啡****\n");
    printf("***********\n");
    scanf("%d",&num);


    switch(num){
    case 1:
        printf("请享用可乐\n");
        break;
    case 2:
        printf("请享用雪碧\n");
        break;
    case 3:
        printf("请享用咖啡\n");
        break;
    default:
        printf("请享用空气\n");
        break;
    }
}