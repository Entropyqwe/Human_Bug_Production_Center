#include <math.h>
#include <stdio.h>
#include<string.h>
int main() {
    char S[100]; 
    if(scanf("%s",S)!=EOF){
         int len = strlen(S);
        for(int i=0;i<len;i++){
            if (S[i] == 'B' && S[i+1] == 'o' && S[i+2] == 'b'){
                printf("i");
                return 0;
            }else{
                printf("-1");
                return 0;
            }
        }
    }

    return 0;
}