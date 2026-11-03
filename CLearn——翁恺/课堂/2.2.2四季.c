#include<stdio.h>

int main(void){
    int num;
    printf("请输入月份（1-12）：");
    scanf("%d",&num);
    switch(num){
    case 1: case 2: case 12:
        printf("冬季\n");
        break;
    case 3: case 4: case 5:
        printf("春季\n");
        break;
    case 6: case 7: case 8:
        printf("夏季\n");
        break;
    case 9: case 10:case 11:
        printf("秋季\n");
        break;
    default:
        printf("输入的月份无效，请输入1-12之间的整数。\n");
        break;
    }
    return 0;
}
