//*题目；给定不超过6的正整数A，考虑从A开始连续的4个数字。请输出所有的由他们组成的无重复数字的三位数
#include <stdio.h>

int main(){
    int i,j,k;
    int n;
    int count=0;
    printf("请输入一个数字:");
    scanf("%d",&n);
    i=n;//设定初始值
    while(i<=n+3){
        j=n;
        while(j<=n+3){
            k=n;
            while(k<=n+3){
            if(i!=j&&i!=k&&j!=k){
                count++;
                printf("%d%d%d",i,j,k);
                if(count==6){
                    printf("\n");
                    count=0;
                }else{
                    printf(" ");
                }
            
    
            }
            k++;
        }
            j++;
        }
        i++;
    }
}