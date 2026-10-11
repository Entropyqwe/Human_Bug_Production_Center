//*引入:输入一个非负整数，正序分别输出他的每一位数字
//*方法一：先整体逆序输出，在整体逆序输出的基础上再逆序输出每一位数字。问题：无法输出末尾有零的数字
//*方法二：交替地进行取余和整除操作
/*int mask=10000
do{
int d=x/mask;
x%=mask;
mask/=10;
}while(mask>=1)
再加上一个计算位数的循环来进行位数判断，界定mask值
for(int i=0;i<digit;i++){
printf("%d ", i);
}
所以mask=10^i
*/
//*方法三：使用数组来存储每一位数字，最后再进行输出
/*int digits[10];
int i=0;
while(x>0){
digits[i++]=x%10;
x/=10;
}
//*for(int j=i-1;j>=0;j--){
printf("%d ", digits[j]); 数组的循环输出
}
*/

//*以方法二为例，进行正序输出每一位数字
#include <stdio.h>
int main()
{
    int x;
    printf("请输入一个非负整数：");
    scanf("%d", &x);
    int mask=1;
    int digit=0;
    while(x/mask>0)//计算位数
    {
        mask*=10;
        digit++;

    }
    mask/=10;//mask的值为10的位数次方，除以10
    for(int i=0;i<digit;i++)
    {
        int d=x/mask;//取出当前位的数字
        printf("%d ", d);
        x%=mask;//去掉当前位的数字
        mask/=10;//mask除以10，进入下一位
    }
    printf("\n");
    return 0;
}
    