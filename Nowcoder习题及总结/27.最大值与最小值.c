/*#include <stdio.h>//多重嵌套


int main() {
    long long a, b,c;
    scanf("%lld %lld %lld",&a,&b,&c);
    if(a>b){
        if(b>c){
            printf("The maximum number is :%lld\n The minimum number is :%lld",a,c);
        }
    }
        else{//a<=b
            if(a>c){
                printf("The maximum number is :%lld\nThe minimum number is :%lld",a,b);
            }else{//a<=c
                printf("The maximum number is :%lld\nThe minimum number is :%lld",c,a);
            }
        }


    return 0;
}*/
//*优化算法
#include <stdio.h>

int main() {
    long long a, b, c;
    // 读取输入
    scanf("%lld %lld %lld", &a, &b, &c);

    // 1. 求最大值
    long long max = a; // 先假设 a 是最大的
    if (b > max) max = b; // 如果 b 更大，更新 max
    if (c > max) max = c; // 如果 c 更大，更新 max

    // 2. 求最小值
    long long min = a; // 先假设 a 是最小的
    if (b < min) min = b; // 如果 b 更小，更新 min
    if (c < min) min = c; // 如果 c 更小，更新 min

    // 3. 输出结果
    // 注意：题目要求冒号后有空格，且分两行输出
    printf("The maximum number is : %lld\n", max);
    printf("The minimum number is : %lld\n", min);

    return 0;
}