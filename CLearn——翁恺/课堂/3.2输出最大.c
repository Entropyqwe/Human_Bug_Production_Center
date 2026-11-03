//创建一个函数用于比较大小
#include <stdio.h>

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int num1, num2;
    printf("请输入两个整数：");
    scanf("%d %d", &num1, &num2);
    printf("较大的数是：%d\n", max(num1, num2));

    return 0;
}