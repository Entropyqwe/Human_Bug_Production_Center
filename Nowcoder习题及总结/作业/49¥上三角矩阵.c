/*1 2 3 4 5  
  1 2 3 4 5  
  1 2 3 4 5  
  1 2 3 4 5   
  1 2 3 4 5 */


#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    int is_upper = 1; 
    int temp;

    for (int i = 0; i < n; i++) {       
        for (int j = 0; j < n; j++) {   
            scanf("%d", &temp);

            if (i > j) {
                if (temp != 0) {
                    is_upper = 0; 
                }
            }
        }
    }
    if (is_upper) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}