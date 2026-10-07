#include <stdio.h>

int main() {
    int T;
    scanf("%d",&T);
    while(T--){
        int n,k;
        scanf("%d %d",&n,&k);
        int cnt=0;
        int S=0;
        for(int i=1;i<=n;i++){
            int a;
            scanf("%d",&a);
            if(a>=k){
                S+=a;
            }else if(a==0&&S>=1){
                S-=1;
                cnt+=1;
            }
            }
         printf("%d\n",cnt);
    }
    return 0;
}
