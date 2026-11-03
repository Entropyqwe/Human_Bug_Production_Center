#include <stdio.h>

int main() {
    int i;          // 循环变量
    int count = 0;  // 用于统计符合条件的数字个数

    printf("符合条件的数字有：\n");
    for (i = 1; i <= 99; i++) {
        
        if (i % 7 == 0 || i % 10 == 7 || i / 10 == 7) {
            printf("%d ", i); // 输出该数字
            count++;          // 计数器加 1
        }
    }

    printf("\n总共有 %d 个这样的数字。\n", count);

    return 0;
}