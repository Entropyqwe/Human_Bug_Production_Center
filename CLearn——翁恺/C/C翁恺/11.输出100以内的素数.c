//*引入：判断素数（只能被1和自己整除的数）
#include <stdio.h>
int main()
{
    int  x;
    //scanf("%d", &x);
for (x = 1; x <= 100; x++) // 循环从1到100，检查每个数是否为素数
{
    int i;
    int isprime = 1; // 假设x是素数//*告诉计算机以一个变量的0或1来判断结果
    for (i = 2; i < x; i++)
    {
        if (x % i == 0){
           isprime=0; // 如果x能被i整除，则x不是素数
           break; // 退出循环，因为已经确定x不是素数
    }
}
    if (isprime == 1 && x > 1) // 如果isprime为1且x大于1，则x是素数
    {
        printf("%d ", x);
    }
} 
printf("\n"); // 输出换行符，使输出更整洁
    return 0;
}

