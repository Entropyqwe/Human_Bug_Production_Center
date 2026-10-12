#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char s[1005];

    if (scanf("%d", &n) != 1) return 0;
    scanf("%s", s);

    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        // 映射到 0-25：s[i] - 'a'
        // 加上 n 并取模 26：(s[i] - 'a' + n) % 26
        // 映射回字符：+ 'a'
        char new_char = (s[i] - 'a' + n) % 26 + 'a';
        printf("%c", new_char);
    }
    printf("\n");

    return 0;
}