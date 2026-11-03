#include <stdio.h>
int main()
{
    int AMOUNT = 0;
    int price = 0;
    printf("请输入票面（元）:");
    scanf("%d",&AMOUNT);

    printf("请输入金额（元）:");
    scanf("%d",&price);

    int change = AMOUNT-price;

    printf("找您%d元。\n",change);

    return 0;
}