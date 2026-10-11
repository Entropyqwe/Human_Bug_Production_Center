#include <stdio.h>

#define MAX_N 1005
#define MAX_M 1005

char map[MAX_N][MAX_M]; 
int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};

int main(void) {
    int n, m;

    if (scanf("%d %d", &n, &m) != 2) {
        return 1;
    }
    for (int i = 0; i < n; i++) {
        scanf("%s", map[i]);
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == '*') {
                printf("*");
            }
            else {
                int count = 0; 
                for (int k = 0; k < 8; k++) {
                    int nx = i + dx[k]; //* 计算邻居的行坐标
                    int ny = j + dy[k]; //*计算邻居的列坐标

                    if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                        //* 如果邻居是雷，计数器 +1
                        if (map[nx][ny] == '*') {
                            count++;
                        }
                    }
                }
                printf("%d", count);
            }
        }
        printf("\n");
    }

    return 0;
}