//*使用字符串的写法实现月份判定
/**
 * @file month_checker.c
 * @brief 通过命令行参数接收月份字符串，判断其所属季节。
 * @usage ./month_checker <MonthName>
 */

#include <stdio.h>   // 提供 printf 函数
#include <string.h>  // 提供 strcmp 字符串比较函数

int main(int argc, char *argv[]) {
    // 1. 参数校验：确保用户传入了且仅传入了一个参数（程序名 + 月份）
    if (argc != 2) {
        printf("用法: %s <月份名称>\n", argv[0]);
        printf("示例: %s March\n", argv[0]);
        return 1; // 返回 1 表示参数数量错误
    }

    // 2. 提取参数：为 argv[1] 起一个语义化的别名
    char *month = argv[1];

    // 3. 核心逻辑：使用 strcmp 进行字符串内容比较
    // 注意：strcmp 返回 0 代表两个字符串完全相同
    if (strcmp(month, "March") == 0 || 
        strcmp(month, "April") == 0 || 
        strcmp(month, "May") == 0) {
        printf("%s 是春季 (Spring)\n", month);
        return 0;
    } 
    else if (strcmp(month, "June") == 0 || 
             strcmp(month, "July") == 0 || 
             strcmp(month, "August") == 0) {
        printf("%s 是夏季 (Summer)\n", month);
        return 0;
    } 
    else if (strcmp(month, "September") == 0 || 
             strcmp(month, "October") == 0 || 
             strcmp(month, "November") == 0) {
        printf("%s 是秋季 (Autumn)\n", month);
        return 0;
    } 
    else if (strcmp(month, "December") == 0 || 
             strcmp(month, "January") == 0 || 
             strcmp(month, "February") == 0) {
        printf("%s 是冬季 (Winter)\n", month);
        return 0;
    } 
    else {
        // 4. 兜底处理：输入了无法识别的月份
        printf("错误: '%s' 不是有效的英文月份名称！\n", month);
        return 2; // 返回 2 表示参数内容非法
    }
}