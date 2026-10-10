//*二维遍历思路
#include <stdio.h>

int main() {
    int n,m;
    int a[11][11];
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%d",&a[i][j]);
        }

    }
    for (int j = 0; j < m; j++) { 
        for (int i = 0; i < n; i++)
        { 
            printf("%d ", a[i][j]); 
        }
        printf("\n"); 
    }
    
    return 0;
}
