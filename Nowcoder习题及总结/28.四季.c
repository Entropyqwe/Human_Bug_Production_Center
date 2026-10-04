#include <stdio.h>

int main() {
    long long A;
    int B;
    scanf("%lld",&A);
    B=A%100;
    if(3<=B&&B<=5){
        printf("spring");
    }else if(6<=B&&B<=8){
        printf("summer");
    }else if(9<=B&&B<=11){;
        printf("autumn");
    }else{
        printf("winter");
    }
    return 0;
}