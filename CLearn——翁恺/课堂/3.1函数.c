//输入三个整数求平均数
#include <stdio.h>

int main() {
    int a, b, c;
    float average;

    printf("请输入三个整数：");
    scanf("%d %d %d", &a, &b, &c);

    average = (a + b + c) / 3.0;

    printf("这三个数的平均数是：%.2f\n", average);

    return 0;
}