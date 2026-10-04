//*主要难点：如果单纯用小时减小时，分钟减分钟会出现假如中午十二点点十分减去十一点三十分，分钟会出现负数
#include<stdio.h>
    int main(){
    int hour1,minute1;
    int hour2,minute2;

    scanf("%d %d",&hour1,&minute1);
    scanf("%d %d",&hour2,&minute2);

    int t1=hour1*60+minute1;
    int t2=hour2*60+minute2;
    int t=t1-t2;

    printf("时间差是%d小时%d分\n",t/60,t%60);

    return 0;
    }