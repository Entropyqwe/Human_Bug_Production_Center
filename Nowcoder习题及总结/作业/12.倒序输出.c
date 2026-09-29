/*#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    printf("%d%d%d%d", n % 10, n / 10 % 10, n / 100 % 10, n / 1000);

    return 0;
}*/
#include <stdio.h> // 引入标准输入输出库，为了使用 scanf 和 printf 函数
#include <string.h> // 引入字符串处理库，为了使用 strlen 函数计算字符串长度

int main() { // 程序的主入口函数
    char s[100]; // 定义一个字符数组，用来存放用户输入的数字字符串（假设最多100位）
    
    scanf("%s", s); // 从键盘读取一串字符存入数组 s（注意：字符串数组名本身就是地址，不需要加 &）

    int len = strlen(s); // 调用 strlen 函数，计算输入的字符串总共有多少个字符（即数字的位数）

    // 使用 for 循环，从字符串的最后一个字符开始，倒序遍历到第一个字符
    // i 初始化为 len - 1（最后一个字符的下标），每次循环 i 减 1，当 i 减到 0 时停止
    for (int i = len - 1; i >= 0; i--) { 
        printf("%c", s[i]); // 使用 %c 格式控制符，逐个打印当前下标对应的字符
    }

    return 0; // 程序正常结束，返回 0
}