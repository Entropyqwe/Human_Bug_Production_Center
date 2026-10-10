#include <stdio.h>

int main() {
    int L, M;
    scanf("%d %d", &L, &M);

    
    int tree[10001]; 
    for (int i = 0; i <= L; i++) {
        tree[i] = 1; 
    }

    for (int i = 0; i < M; i++) {
        int l, r;
        scanf("%d %d", &l, &r);
        for (int j = l; j <= r; j++) {
            tree[j] = 0;
        }
    }

    int count = 0;
    for (int i = 0; i <= L; i++) {
        if (tree[i] == 1) {
            count++;
        }
    }

    printf("%d\n", count);
    return 0;
}