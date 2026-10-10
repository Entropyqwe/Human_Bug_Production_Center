#include <stdio.h>
#include <math.h> 

int main() {
    int x1, y1, x2, y2;
    
    
    if (scanf("%d %d", &x1, &y1) != 2) {
        return 1;
    }
    
    if (scanf("%d %d", &x2, &y2) != 2) {
        return 1;
    }
    
    
    double dx = fabs(x1 - x2);
    double dy = fabs(y1 - y2);
    
    
    double d_M = dx + dy;
    
    
    double d_E = sqrt(dx * dx + dy * dy);
    
    
    double delta = fabs(d_M - d_E);
    
    
    printf("%.6f\n", delta);
    
    return 0;
}