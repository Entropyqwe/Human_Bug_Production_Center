#include<string.h>
int main() {
    char s[20] = {0};//一定要初始化数组
    scanf("%s", &s);
    int val = strlen(s);
    for (int i = 1; i <= val; i++) { 
        printf("%c", s[i - 1]);
        if ((val - i) % 3 == 0 && i != val) printf(",");
    }
    return 0;
}
