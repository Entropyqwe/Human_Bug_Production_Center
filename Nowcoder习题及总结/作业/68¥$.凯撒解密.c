/**
 * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
 *
 * 进行凯撒解密
 * @param password string字符串 旺仔哥哥的密码
 * @param n int整型 每个字符加密过程中错位的次数
 * @return string字符串
 */
char* decodeWangzai(char* password, int n )//表示要求输入两个变量
 {
    for (int i = 0; password[i] != '\0'; i++) {
        // password[i] - 'a' : 把字母变成 0-25 的数字
        //  + 26 : 防止减完变成负数（比如 a 退 1 步变成 -1）
        //  % 26 : 保证结果在 0-25 之间循环
        //  + 'a' : 把数字变回字母
        password[i] = (password[i] - 'a' - n % 26 + 26) % 26 + 'a';
    }
    return password;
}
