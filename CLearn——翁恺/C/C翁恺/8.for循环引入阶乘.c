//引入：关于阶乘
/* //*首先是传统的while循环机制 
#include <stdio.h>

int main(){
    
    int n;
    int i=1;
    int a;
    a=1;
    printf("请输入一个整数：");
    scanf("%d",&n);
    while(i<=n){
        a=a*i;
        i++;
    }
        printf("%d的阶乘为：%d",n,a);
        return 0;*/
//*下面是for循环机制,（初试条件，循环条件，每次循环结束后需要做的事情）
//*关于阶乘：对象数字：n，当前阶乘数：i，输出的结果：fact   
#include <stdio.h>

int main(){
    int n;
    int i=1;
    int fact=1;
    printf("请输入一个整数：");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        fact=fact*i;
    }
        printf("%d的阶乘为:%d\n",n,fact);
        return 0;
    }

