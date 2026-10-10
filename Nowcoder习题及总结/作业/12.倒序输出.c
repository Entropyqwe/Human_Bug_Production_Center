/*#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    printf("%d%d%d%d", n % 10, n / 10 % 10, n / 100 % 10, n / 1000);

    return 0;
}*/
#include <stdio.h> 
#include <string.h> 

int main() {
    char s[100]; 
    scanf("%s", s); 

    int len = strlen(s); 
    //*这个是计算字符串的长度，去过是整数形式，直接使用len就可以了，程序会自动识别

   
    for (int i = len - 1; i >= 0; i--) { 
        printf("%c", s[i]); 
    }

    return 0; 
}