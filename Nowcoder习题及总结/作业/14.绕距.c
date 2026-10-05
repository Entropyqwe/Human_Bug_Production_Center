#include <stdio.h>
#include <math.h> // 引入数学库，用于 sqrt 和 fabs

int main() {
    int x1, y1, x2, y2;
    
    // 读取起点坐标
    if (scanf("%d %d", &x1, &y1) != 2) {
        return 1;
    }
    // 读取终点坐标
    if (scanf("%d %d", &x2, &y2) != 2) {
        return 1;
    }
    
    // 计算横纵坐标差的绝对值
    double dx = fabs(x1 - x2);
    double dy = fabs(y1 - y2);
    
    // 计算曼哈顿距离
    double d_M = dx + dy;
    
    // 计算欧几里得距离
    double d_E = sqrt(dx * dx + dy * dy);
    
    // 计算绕距
    double delta = fabs(d_M - d_E);
    
    // 输出结果，默认 printf 会输出足够精度
    printf("%.6f\n", delta);
    
    return 0;
}