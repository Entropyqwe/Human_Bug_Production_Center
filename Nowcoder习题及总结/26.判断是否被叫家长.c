#include <stdio.h>

int main() {
    int A, B,C;
    scanf("%d %d %d",&A,&B,&C);
    float Avg;
    Avg=(A+B+C)/3;
    if(Avg>=60){
        printf("NO");
    }else{
        printf("YES");
    }

    
    return 0;
}