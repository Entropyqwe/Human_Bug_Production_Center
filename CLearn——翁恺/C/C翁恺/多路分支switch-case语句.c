#include<stdio.h>
    int main(){
        int type;
        printf("请输入一个数字：");
        scanf("%d",&type);

        switch(type){
            case 1:
                printf("你好\n");
                break;
            case 2:
                printf("早上好\n");
                break;
            case 3:
                printf("下午好\n\n");
                break;
            case 4:
                printf("晚上好\n");
                break;
            default:
                printf("再见\n");
        }
        return 0;
    }





    /*用来替代if和else，提高代码的可读性和执行效率
    else if 组合，用中文法则翻译，大概为“也可以”，级联写法太浪费时间*/