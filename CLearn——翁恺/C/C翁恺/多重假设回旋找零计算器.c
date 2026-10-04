//*程序目的，判断需要找零多少钱或者不够应该再支付多少钱
#include<stdio.h>

int main(){
    float a;//产品售价//*此处也可以换用初始化变量写法进行，例：int price =0;
    float b;//付款金额
    float c;//应该找零的金额
    float d;//应该补充的金额
     //*也可以不用定义这么多变量，可以在最终的输出阶段直接输出变量的运算结果例：printf("应该找您%.2f元"，付款-售价)
    printf("请输入产品售价：");
    scanf("%f",&a);
    printf("请输入您的付款金额：");
    scanf("%f",&b);
    
    if(a<=b){
        c=b-a;
        printf("应找您%.2f元\n",c);
    }else{
        printf("金额不足，还需增添%.2f元\n",a-b);
    }
    return 0;
}
//*此处或用else if形式
/*else if(a>b){
        d=a-b;
        printf("金额不足，还需增添%.2f元\n",d);*/