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
    
    scanf("%lld %lld %lld", &a, &b, &c);

    
    long long max = a; 
    if (b > max) max = b; 
    if (c > max) max = c; 

    long long min = a; 
    if (b < min) min = b; 
    if (c < min) min = c;
    
    printf("The maximum number is : %lld\n", max);
    printf("The minimum number is : %lld\n", min);

    return 0;
}