#include<stdio.h>
    int main(){
        const int ready=24;
        int code=0;
        int count=0;

        scanf("%d %d",&code,&count);
        if(code==ready){
           if(count<20){
            printf("一切正常\n");
           }else{
           printf("存在问题\n");
           }
        }else{
            printf("存在问题\n");
        }
        return 0;
    }