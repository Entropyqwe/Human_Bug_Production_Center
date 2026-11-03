#include<stdio.h>
int main(){
    int a;
    float score;
    char  LV;
    printf("请输入小明的学号:"); 
    scanf("%d",&a);
    printf("请输入小明的成绩:"); 
    scanf("%f",&score);
    printf("请输入小明的等级:"); 
    scanf(" %c",&LV);

    printf("小明的学号为：%d,小明的成绩为：%.1f,小明的等级为: %c",a,score,LV);
}
    
    
