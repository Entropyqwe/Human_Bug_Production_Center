#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int sum = 0;
    if (n % 2 == 0) {
        sum = -n / 2;
    } else {
        sum = (n + 1) / 2;
    }

    printf("%d\n", sum);

    return 0;
}