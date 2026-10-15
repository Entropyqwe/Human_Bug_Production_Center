#include <stdio.h>
#include <string.h>

struct Student {
    char name[10]; 
    int c1, c2, c3;
    int total;     
};

int main() {
    int N;
    scanf("%d", &N);


    struct Student current; 
    struct Student best;
    
    int max_total = -1; 

    for (int i = 0; i < N; i++) {
        scanf("%s %d %d %d", current.name, &current.c1, &current.c2, &current.c3);

        current.total = current.c1 + current.c2 + current.c3;

        if (current.total > max_total) {
            max_total = current.total;
 
            best = current; 
        }
    }

    printf("%s %d %d %d\n", best.name, best.c1, best.c2, best.c3);

    return 0;
}