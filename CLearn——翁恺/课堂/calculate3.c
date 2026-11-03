#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int secret, guess, attempts = 0;

    srand(time(NULL));
    secret = rand() % 100 + 1; // 生成1~100的随机数

    printf("=== 猜数字游戏 ===\n");
    printf("我想了一个1到100之间的数字，猜猜看！\n");

    do {
        printf("请输入你的猜测: ");
        scanf("%d", &guess);
        attempts++;

        if (guess > secret) {
            printf("太大了！再试试。\n");
        } else if (guess < secret) {
            printf("太小了！再试试。\n");
        } else {
            printf("恭喜你，猜对了！答案就是 %d\n", secret);
            printf("你一共猜了 %d 次。\n", attempts);
        }
    } while (guess != secret);

    return 0;
}