//*数组法
#include <stdio.h>
//数组法：
int main() {
    int A[25];
    int n;
    scanf("%d",&n);
//初始化最初几项
    A[1]=0;
    if(n>=2) A[2]=1;
    if(n>=3) A[3]=1;
    for(int i=4;i<=n;i++){
        A[i]=A[i-3]+2*A[i-2]+A[i-1];
    }
    printf("%d",A[n]);
    return 0;
    }
//*变量迭代法
#include <stdio.h>
int main() {
    int n;
    scanf("%d",&n);
    int a=0;
    int b=1;
    int c=1;
    if(n<=1){
        printf("0");
        return 0;
    }
    if(n==2||n==3){

        printf("1");
        return 0;
    }
    for(int i=4;i<=n;i++){
        c=a+2*b+c;
        a=b;
        b=c;
    }
    printf("%d",c);
    return 0;
    }
    