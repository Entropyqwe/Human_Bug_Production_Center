#include<stdio.h>
int main(void){
    int a;
    int b[105];
    scanf("%d",&a);
    for(int i=0;i<a;i++){
        scanf("%d",&b[i]);
    }
    for(int j=a;j>0;j--){
        printf("%d ",b[j]);
    }
    return 0;
}