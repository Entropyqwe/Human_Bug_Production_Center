#include<stdio.h>
    int main(){
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);

        int max=0;
        
        if (a>b)
          if(b>c)
             max=a;
        else 
            max=c;
    else 
        if (b>c)
           max=b;//此处只有在第一个if语句中的两个假设条件都不成立才会这样，所以说只需要给出一份与第一个if语句相反的条件补充即可进行运算
        else 
             max=c;

    printf("最大值为%d\n",max);

    return 0;
    }