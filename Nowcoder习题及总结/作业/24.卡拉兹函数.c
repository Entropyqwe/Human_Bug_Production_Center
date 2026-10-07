#include <stdio.h>

int main() {
    int n,a;
    scanf("%d",&n);
    if(n%2==0){
    a=n/2;
    }else{
    a=3*n+1;
    }
    printf("%d\n",a);
    return 0;
}