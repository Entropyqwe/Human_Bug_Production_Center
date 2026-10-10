/*原本考虑#include <stdio.h>

int main() {
    int n,m;
    int a[n][m];
    if(n<=2&&m<=2)a[n][m]=1;
    int count=0;//*设为每行可以有的数
    scanf("%d",&n);
    //*设i为横，j为纵
    if(n<=2&&m<=2){
        a[n][m]=1;
    }else{
        count=2;
    for(int i=3;i<=n;i++){
        count+=1;

    }
    
    return 0;
}
    */
//*int a[n][m]无法如此定义;
//*直接使用公式代替a[i][j] = a[i-1][j-1] + a[i-1][j];
//*先找到固定的比找到规律好（第一竖列始终为1）

#include <stdio.h>

int main() {
    int n;
    //*  定义二维数组（n≤34，数组大小设为35×35避免越界）
    int a[35][35] = {0}; // 初始化为0，方便后续计算

    scanf("%d", &n);

    //*  遍历每一行（i从0到n-1，对应第1行到第n行）
    for (int i = 0; i < n; i++) {
        a[i][0] = 1; // 每行第一个元素为1（边界条件）

        //*  计算中间元素（从第2个元素开始，j≤i）
        for (int j = 1; j <= i; j++) {
             // 递推公式：上一行左上+上一行同列
             a[i][j] = a[i-1][j-1] + a[i-1][j];
        }


        //* 输出当前行（控制空格格式）
        for (int j = 0; j <= i; j++) {
            printf("%d", a[i][j]);
            if (j < i) { // 非最后一个元素时加空格，a[i][j] = a[i-1][j-1] + a[i-1][j];避免行末多余空格
                printf(" ");
            }
        }
        printf("\n"); // 每行结束后换行
    }

    return 0;
}