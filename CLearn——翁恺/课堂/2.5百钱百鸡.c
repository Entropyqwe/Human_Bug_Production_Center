#include<stdio.h>

int main(void){
    int i,j,k;
    for(i=0;i<21;i++){
        for(j=0;j<31;j++){
            for(k=0;k<101;k++){
                if(5*i+3*j+k*1/3==100&&i+j+k==100){
                    printf("公鸡%d只,母鸡%d只,小鸡%d只\n",i,j,k);
                }
            }
        }
    }
    return 0;
}