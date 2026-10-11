//*情景引入：如何使用1角、2角5角的硬币来凑出1元钱的所有组合方式
#include <stdio.h>
int main()
{
    int i, j, k;
    int count = 0;
    for (i = 0; i <= 10; i++) // 1角
    {
        for (j = 0; j <= 5; j++) // 2角
        {
            for (k = 0; k <= 2; k++) // 5角
            {
                if (i + 2 * j + 5 * k == 10) //
                {
                    printf("1角:%d,2角:%d,5角:%d\n", i, j, k);
                    count=1;
                    break; // 退出当前循环，因为已经找到一个组合
                }
            }
            if(count==1)break;
        }  
        if(count==1)break;    
    }
    
    return 0;
}
//*接力break的使用
//*有多少循环就要有多少个break，break只能跳出当前循环体，不能跳出多层循环体，用一个变量来界定是否启用接力break

//*go to语句的使用
/*goto out;


out:*/