#include <stdio.h>

int main() {
    double K,C;
    scanf("%lf",&K);
    C=(K-273.15)*1.8+32;
    printf("%lf",C);
    return 0;
}