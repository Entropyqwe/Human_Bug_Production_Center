#include <stdio.h>
#include <string.h>

int main() {
    int n;

    if (scanf("%d", &n) != 1) return 0;

    char S[2000] = {0}; 
    int len = 0; 

    for (int num = 1; len < n; num++) {
        char temp[10];
        int temp_len = sprintf(temp, "%d", num);

        for (int j = 0; j < temp_len; j++) {
            S[len] = temp[j];
            len++;
        }
    }
    printf("%c\n", S[n - 1]);

    return 0;
}