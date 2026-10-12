#include <stdio.h>
#include <string.h>
#include <ctype.h> // 需要引入这个头文件来使用 tolower

int main() {
    char S[100];
    if (scanf("%s", S) != EOF) {
        int len = strlen(S);
        for (int i = 0; i + 2 < len; i++) {
            if (tolower(S[i]) == 'b' &&
                tolower(S[i+1]) == 'o' &&
                tolower(S[i+2]) == 'b') {

                printf("%d", i);
                return 0; 
            }
        }
        printf("-1");
    }
    return 0;
}