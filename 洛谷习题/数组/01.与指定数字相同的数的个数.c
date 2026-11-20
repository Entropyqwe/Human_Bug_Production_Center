#include <stdio.h>

int main(void) {
    int n, m; 
    int count = 0; 
    int F[105];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &F[i]);
    }
    scanf("%d", &m);

    for (int i = 0; i < n; i++) {
        if (F[i] == m) {
            count++;
        }
    }
    printf("%d", count);

    return 0;
}