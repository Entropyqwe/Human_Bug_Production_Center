#include <stdio.h>
#include <string.h>

#define MAX_LEN 1000005

char s[MAX_LEN];

int main() {
    if (scanf("%s", s) != 1) {
        return 0;
    }
    int len = strlen(s); 
    for (int i = 0; i < len; i++) {
        if (s[i] == '5') {
            s[i] = '*';
        }
    }

    printf("%s\n", s);

    return 0;
}