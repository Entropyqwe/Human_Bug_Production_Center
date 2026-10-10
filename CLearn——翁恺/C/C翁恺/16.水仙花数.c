#include <stdio.h>

int main() {
    int n;
    printf("请输入位数 (N>=3): ");
    scanf("%d", &n);

    // 1. 校验输入合法性
    if (n < 3) {
        printf("请输入大于等于3的整数\n");
        return 1; // 异常退出
    }

    // 2. 安全计算遍历范围 [start, end]
    // 使用整数累乘，避免 pow 精度丢失
    int start = 1;
    for(int i = 0; i < n - 1; i++) {
        start *= 10; 
    }
    int end = start * 10 - 1;

    printf("%d位数的水仙花数有:\n", n);

    // 3. 遍历每一个数
    for (int num = start; num <= end; num++) {
        int sum = 0;
        int temp = num; // 保护 num 不被修改

        // 4. 拆分每一位并计算 N 次方和
        while (temp > 0) {
            int digit = temp % 10; // 取最后一位
            
            // 手动计算 digit 的 n 次方 (整数运算)
            int power_val = 1;
            for(int k = 0; k < n; k++) {
                power_val *= digit;
            }
            
            sum += power_val; // 累加
            temp /= 10;       // 去掉最后一位，准备下一次循环
        }

        // 5. 判断是否相等
        if (sum == num) {
            printf("%d\n", num);
        }
    }

    return 0;
}