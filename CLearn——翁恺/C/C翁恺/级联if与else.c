//*情景引入：分段函数的计算
#include <stdio.h>

int main(){
    int X=0, f;//*虽然这里f作为因变量，但是还是要进行变量定义*/
    printf("请输入一个整数X：");
    scanf("%d",&X);
    if(X<0){
        f=1;
    }else if(X==0){
        f=0;
    }else{
        f=-1;
    }
    printf("f的值为：%d\n",f);
    return 0;
}