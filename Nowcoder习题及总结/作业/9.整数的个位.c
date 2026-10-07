#include <stdio.h>

int main() {
    int a;
    int b;
    scanf("%d",&a);
    
    if(a>=10){
        b=a%10;
    }else{
        b=a;
    }
    
    printf("%d\n",b);
    return 0;
    }